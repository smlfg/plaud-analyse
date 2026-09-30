"""Download all Plaud transcripts into ./PlaudImport using the `plaud` CLI.

Usage: python3 plaud_download.py
Files are saved as PlaudImport/<date>_<file_id>.txt. Existing files are skipped.
Recordings without a transcript are listed in plaud_fehlgeschlagen.txt (next to
this script, not inside PlaudImport, so it isn't mixed up with the transcripts).
"""

import re
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).parent
OUTPUT_DIR = BASE_DIR / "PlaudImport"
FAILED_FILE = BASE_DIR / "plaud_fehlgeschlagen.txt"
PAGE_SIZE = 100
ROW = re.compile(r"^\s*(of_[0-9a-f]+)\s+.*?(\d{4}-\d{2}-\d{2})\s+(\S+)\s*$")


def list_recordings():
    """Return [(file_id, date, duration), ...] for all recordings, paging until empty."""
    recordings = []
    page = 1
    while True:
        result = subprocess.run(
            ["plaud", "files", "--page", str(page), "--page-size", str(PAGE_SIZE)],
            capture_output=True,
            text=True,
        )
        rows = [m.groups() for line in result.stdout.splitlines() if (m := ROW.match(line))]
        if not rows:
            break
        recordings.extend(rows)
        page += 1
    return recordings


def write_failed_report(failed):
    """Write one line per failed recording: id, date, duration, reason from the CLI."""
    lines = [f"{len(failed)} Aufnahmen ohne Transkript", ""]
    for file_id, date, duration, reason in failed:
        lines.append(f"{file_id}\t{date}\t{duration}\t{reason}")
    FAILED_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    recordings = list_recordings()
    print(f"{len(recordings)} Aufnahmen gefunden")

    failed = []
    for i, (file_id, date, duration) in enumerate(recordings, start=1):
        target = OUTPUT_DIR / f"{date}_{file_id}.txt"
        if target.exists() and target.stat().st_size > 0:
            print(f"[{i}/{len(recordings)}] skip {target.name}")
            continue
        result = subprocess.run(
            ["plaud", "transcript", file_id, "-o", str(target)],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0 or not target.exists():
            output = (result.stdout + "\n" + result.stderr).splitlines()
            messages = [l.strip() for l in output if l.strip() and "Fetching transcript" not in l]
            reason = " ".join(messages) or "unbekannter Fehler"
            failed.append((file_id, date, duration, reason))
            print(f"[{i}/{len(recordings)}] FEHLER {file_id}: {reason}")
        else:
            print(f"[{i}/{len(recordings)}] ok {target.name}")

    write_failed_report(failed)
    print(f"Fertig. Fehlgeschlagen: {len(failed)} (siehe {FAILED_FILE.name})")


if __name__ == "__main__":
    main()

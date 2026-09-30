"""Download all Plaud transcripts into ./PlaudImport using the `plaud` CLI.

Usage: python3 plaud_download.py
Files are saved as PlaudImport/<date>_<file_id>.txt. Existing files are skipped.
"""

import re
import subprocess
from pathlib import Path

OUTPUT_DIR = Path(__file__).parent / "PlaudImport"
PAGE_SIZE = 100
ROW = re.compile(r"^\s*(of_[0-9a-f]+)\s+.*?(\d{4}-\d{2}-\d{2})\s+\S+\s*$")


def list_recordings():
    """Return [(file_id, date), ...] for all recordings, paging until empty."""
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


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)
    recordings = list_recordings()
    print(f"{len(recordings)} Aufnahmen gefunden")

    failed = []
    for i, (file_id, date) in enumerate(recordings, start=1):
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
            failed.append(file_id)
            print(f"[{i}/{len(recordings)}] FEHLER {file_id}: {result.stderr.strip() or result.stdout.strip()}")
        else:
            print(f"[{i}/{len(recordings)}] ok {target.name}")

    print(f"Fertig. Fehlgeschlagen: {len(failed)}")
    for file_id in failed:
        print(" ", file_id)


if __name__ == "__main__":
    main()

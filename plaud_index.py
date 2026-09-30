"""Build plaud_index.csv with title, start time and duration per recording.

Usage: python3 plaud_index.py
Needs the `plaud` CLI (logged in). Reads the transcript file names from
./PlaudImport, so run plaud_download.py first. Already indexed recordings are
skipped, so the script can simply be rerun if the API rate limit interrupts it.
"""

import csv
import re
import subprocess
import time
from pathlib import Path

BASE_DIR = Path(__file__).parent
IMPORT_DIR = BASE_DIR / "PlaudImport"
INDEX_FILE = BASE_DIR / "plaud_index.csv"
HEADER = ["datei", "id", "titel", "start", "dauer_sek"]
DURATION = re.compile(r"(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?")
MAX_RETRIES = 6


def duration_to_seconds(text):
    """'1h14m' -> 4440, '7m27s' -> 447, '21s' -> 21"""
    m = DURATION.fullmatch(text.strip())
    if m is None:
        raise ValueError(f"Ungültige Dauer: {text!r}")
    hours, minutes, seconds = (int(x) if x else 0 for x in m.groups())
    return hours * 3600 + minutes * 60 + seconds


def fetch_details(file_id):
    """Return {'name', 'start_at', 'duration'} or None. Backs off on 429."""
    for attempt in range(MAX_RETRIES):
        result = subprocess.run(["plaud", "file", file_id], capture_output=True, text=True)
        out = result.stdout + result.stderr
        if "429" in out:
            wait = 5 * 2**attempt
            print(f"  429, warte {wait}s ...")
            time.sleep(wait)
            continue
        fields = {}
        for key in ("name", "start_at", "duration"):
            m = re.search(rf"^\s*{key}:\s*(.*)$", out, re.MULTILINE)
            fields[key] = m.group(1).strip() if m else ""
        return fields if fields["start_at"] and fields["duration"] else None
    return None


def load_index():
    if not INDEX_FILE.exists():
        return {}
    with open(INDEX_FILE, newline="", encoding="utf-8") as f:
        return {row["id"]: row for row in csv.DictReader(f)}


def save_index(index):
    rows = sorted(index.values(), key=lambda r: r["start"])
    with open(INDEX_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADER)
        writer.writeheader()
        writer.writerows(rows)


def main():
    transcripts = {p.stem.split("_", 1)[1]: p.name for p in IMPORT_DIR.glob("*.txt")}
    index = {i: r for i, r in load_index().items() if i in transcripts}
    todo = [i for i in sorted(transcripts) if i not in index]
    print(f"{len(transcripts)} Transkripte, {len(index)} schon im Index, {len(todo)} zu holen")

    failed = []
    try:
        for n, file_id in enumerate(todo, start=1):
            d = fetch_details(file_id)
            if d is None:
                failed.append(file_id)
                print(f"[{n}/{len(todo)}] FEHLER {file_id}")
                continue
            try:
                dauer_sek = duration_to_seconds(d["duration"])
            except ValueError as e:
                failed.append(file_id)
                print(f"[{n}/{len(todo)}] FEHLER {file_id}: {e}")
                continue
            index[file_id] = {
                "datei": transcripts[file_id],
                "id": file_id,
                "titel": d["name"],
                "start": d["start_at"],
                "dauer_sek": dauer_sek,
            }
            print(f"[{n}/{len(todo)}] ok {file_id}")
            time.sleep(0.3)
    finally:
        save_index(index)

    print(f"Index: {len(index)} Eintraege, fehlgeschlagen: {len(failed)}")


if __name__ == "__main__":
    main()

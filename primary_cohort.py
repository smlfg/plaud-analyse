"""Primärkohorte: parsebare Monologe mit einzigem Sprecher Samuel Flg."""

from pathlib import Path

from constants import IMPORT_DIR, SAMUEL_FLG
from parse_speakers import parse_speakers


def primary_cohort(import_dir=None):
    src = Path(import_dir) if import_dir else IMPORT_DIR
    paths = []
    for path in sorted(src.glob("*.txt")):
        parsed = parse_speakers(path.read_text(encoding="utf-8"))
        if not parsed:
            continue
        speakers = {spk for spk, _ in parsed}
        if speakers == {SAMUEL_FLG}:
            paths.append(path)
    return paths


if __name__ == "__main__":
    cohort = primary_cohort()
    print(len(cohort), "Samuel-Flg-Monologe")
    for p in cohort[:3]:
        print(" -", p.name)
import csv
from pathlib import Path

from constants import INDEX_FILE


def load_index_by_datei(index_file=None):
    path = Path(index_file) if index_file else INDEX_FILE
    if not path.exists():
        return {}
    with open(path, newline="", encoding="utf-8") as f:
        return {row["datei"]: row for row in csv.DictReader(f)}


if __name__ == "__main__":
    print(len(load_index_by_datei()), "Index-Einträge")

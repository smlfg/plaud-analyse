from pathlib import Path


def file_id_from_datei(datei):
    """2026-06-02_of_abc123.txt → abc123"""
    stem = Path(datei).stem
    if "_of_" in stem:
        return stem.split("_of_", 1)[1]
    return stem


if __name__ == "__main__":
    print(file_id_from_datei("2026-06-02_of_abc123.txt"))

from pathlib import Path

from constants import CLEAN_DIR


def save_clean_text(datei, text, clean_dir=None):
    base = Path(clean_dir) if clean_dir else CLEAN_DIR
    base.mkdir(exist_ok=True)
    out = base / datei
    out.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    save_clean_text("_test.txt", "Hallo Test")

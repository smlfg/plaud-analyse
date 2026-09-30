from pathlib import Path

from constants import IMPORT_DIR
from pipeline import pipeline
from save_clean_text import save_clean_text


def bereinige_alle(import_dir=None, clean_dir=None):
    """Alle .txt aus PlaudImport lesen, bereinigen, in PlaudImportClean speichern."""
    src = Path(import_dir) if import_dir else IMPORT_DIR
    count = 0
    for path in sorted(src.glob("*.txt")):
        text = pipeline(path.read_text(encoding="utf-8"))
        if not text.strip():
            continue
        save_clean_text(path.name, text, clean_dir=clean_dir)
        count += 1
    return count


if __name__ == "__main__":
    print(bereinige_alle(), "Dateien bereinigt")

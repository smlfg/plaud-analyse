from pathlib import Path

from constants import IMPORT_DIR
from date_from_datei import date_from_datei
from load_index_by_datei import load_index_by_datei
from metriken import metriken
from parse_start import parse_start
from pipeline import pipeline
from save_clean_text import save_clean_text
from woerter_pro_minute import woerter_pro_minute


def sammle_records(import_dir=None, index_file=None, clean_dir=None):
    """Pro Transkript ein Dict mit Metriken + start + dauer_sek (falls Index)."""
    src = Path(import_dir) if import_dir else IMPORT_DIR
    index = load_index_by_datei(index_file)
    records = []
    for path in sorted(src.glob("*.txt")):
        datei = path.name
        text = pipeline(path.read_text(encoding="utf-8"))
        if not text.strip():
            continue
        save_clean_text(datei, text, clean_dir=clean_dir)
        m = metriken(text)
        row = index.get(datei, {})
        start_dt = parse_start(row.get("start", "")) if row else None
        if start_dt is None:
            start_dt = date_from_datei(datei)
        dauer = None
        if row.get("dauer_sek"):
            try:
                dauer = int(row["dauer_sek"])
            except ValueError:
                dauer = None
        records.append(
            {
                "datei": datei,
                "start": start_dt,
                "dauer_sek": dauer,
                "titel": row.get("titel", ""),
                "text": text,
                **m,
                "wpm": woerter_pro_minute(text, dauer),
            }
        )
    return records


if __name__ == "__main__":
    rec = sammle_records()
    print(len(rec), "Records")

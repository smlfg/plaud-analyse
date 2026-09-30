import re
from datetime import datetime


def date_from_datei(datei):
    """Datum aus Dateiname, falls kein Index."""
    m = re.match(r"(\d{4}-\d{2}-\d{2})", datei)
    if m:
        return datetime.strptime(m.group(1), "%Y-%m-%d")
    return None


if __name__ == "__main__":
    print(date_from_datei("2026-06-02_of_abc.txt"))

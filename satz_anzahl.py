import re


def satz_anzahl(text) -> int:
    saetze = [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]
    return len(saetze)

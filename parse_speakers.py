"""Rohzeilen sprechererhaltend parsen — eine Zeile = (sprecher, text).

Format: '[hh:mm - hh:mm] Sprecher: text' — fuehrender eckiger Zeitstempel
+ Sprecher zwischen '] ' und ': '. Leerzeilen werden uebersprungen.
Jede nichtleere unparsebare Zeile macht die Datei unparsebar (returnt None
als Signal fuer den Aufrufer)."""


def parse_speakers(raw):
    out = []
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        if ": " not in line:
            return None
        prefix, text = line.split(": ", 1)
        if "] " not in prefix or not prefix.startswith("["):
            return None
        speaker = prefix.split("] ", 1)[1].strip()
        if not speaker:
            return None
        out.append((speaker, text))
    return out


if __name__ == "__main__":
    sample = (
        "[00:00 - 00:05] Samuel Flg: Hallo.\n"
        "[00:05 - 00:10] Speaker 1: Antwort.\n"
    )
    print(parse_speakers(sample))
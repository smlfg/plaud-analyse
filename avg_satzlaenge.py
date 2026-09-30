from constants import SENT_SPLIT
from tokenize_fn import tokenize


def avg_satzlaenge(text, woerter):
    saetze = [s.strip() for s in SENT_SPLIT.split(text) if s.strip()]
    if not saetze:
        return float(len(woerter)) if woerter else 0.0
    laengen = [len(tokenize(s)) for s in saetze]
    return sum(laengen) / len(laengen)


if __name__ == "__main__":
    print(avg_satzlaenge("Erster Satz. Zweiter Satz!", ["Erster", "Satz", "Zweiter", "Satz"]))

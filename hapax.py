from collections import Counter

from tokenize_fn import tokenize


def hapax(text):
    """Anteil Wörter, die im Text genau einmal vorkommen (Hapax legomena)."""
    woerter = tokenize(text)
    if not woerter:
        return 0.0
    counts = Counter(woerter)
    einmal = sum(1 for c in counts.values() if c == 1)
    # Spec: Hapax-Anteil = Wörter die genau 1× vorkommen / Wörter gesamt
    return einmal / len(woerter)


if __name__ == "__main__":
    print(hapax("a b a c d"))

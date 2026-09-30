from constants import STOPWORDS


def inhalt_woerter_anteil(woerter):
    """Anteil Tokens, die keine Füllwörter sind (0–1)."""
    if not woerter:
        return 0.0
    inhalt = sum(1 for w in woerter if w not in STOPWORDS)
    return inhalt / len(woerter)


if __name__ == "__main__":
    print(inhalt_woerter_anteil(["ich", "gehe", "nach", "hause"]))

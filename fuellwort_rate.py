from constants import STOPWORDS
from tokenize_fn import tokenize


def fuellwort_rate(text):
    """Anteil Tokens, die Füllwörter sind (0–1)."""
    woerter = tokenize(text)
    if not woerter:
        return 0.0
    fuell = sum(1 for w in woerter if w in STOPWORDS)
    return fuell / len(woerter)


if __name__ == "__main__":
    print(fuellwort_rate("ich gehe nach hause"))

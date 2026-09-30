from collections import Counter

from constants import STOPWORDS
from tokenize_fn import tokenize


def top_inhalt_woerter(text, n=10):
    """Die n häufigsten Inhaltswörter (ohne Füllwörter) als Liste (wort, count)."""
    woerter = [w for w in tokenize(text) if w not in STOPWORDS]
    return Counter(woerter).most_common(n)


if __name__ == "__main__":
    print(top_inhalt_woerter("haus haus baum haus baum auto", 3))

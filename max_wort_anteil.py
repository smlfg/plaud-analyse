from tokenize_fn import tokenize


def max_wort_anteil(text):
    woerter = tokenize(text)
    if not woerter:
        return 0.0
    h = {}
    for w in woerter:
        h[w] = h.get(w, 0) + 1
    return max(h.values()) / len(woerter)

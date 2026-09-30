from tokenize_fn import tokenize


def wiederholungs_rate(text):
    woerter = tokenize(text)
    if not woerter:
        return 0.0
    vielfalt = len(set(woerter)) / len(woerter)
    return 1.0 - vielfalt

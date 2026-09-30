from tokenize_fn import tokenize


def woerter_pro_minute(text, dauer_sek):
    if dauer_sek is None or dauer_sek <= 0:
        return 0.0
    return len(tokenize(text)) / (dauer_sek / 60)

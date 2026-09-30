from tokenize_fn import tokenize


def varianz(text):
    """Vielfalt = verschiedene Wörter / Wörter gesamt (Projekt-Notiz „varianz vielfalt“)."""
    woerter = tokenize(text)
    if not woerter:
        return 0.0
    return len(set(woerter)) / len(woerter)


if __name__ == "__main__":
    print(varianz("a b a c"))

from constants import WORD_RE


def tokenize(text):
    return WORD_RE.findall(text.lower())


if __name__ == "__main__":
    print(tokenize("Hallo Welt — Test."))

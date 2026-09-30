from tokenize_fn import tokenize


def unique_count(text):
    woerter = tokenize(text)
    if not woerter:
        return 0
    return len(set(woerter))


if __name__ == "__main__":
    print(unique_count("a b a c"))

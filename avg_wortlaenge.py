def avg_wortlaenge(woerter):
    if not woerter:
        return 0.0
    return sum(len(w) for w in woerter) / len(woerter)


if __name__ == "__main__":
    print(avg_wortlaenge(["abcd", "ef"]))

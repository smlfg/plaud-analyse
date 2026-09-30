from clean_line import clean_line


def pipeline(transcript):
    """Roh-Transkript → eine bereinigte Textzeile (Leerzeichen zwischen Segmenten)."""
    lines = [clean_line(line) for line in transcript.splitlines()]
    lines = [ln for ln in lines if ln]
    return " ".join(lines)


if __name__ == "__main__":
    sample = "[00:00] A: Hallo.\n[00:01] A: Welt."
    print(pipeline(sample))

def clean_line(line):
    """Sprecher-Präfix entfernen (alles vor erstem ': ')."""
    if ": " not in line:
        return line.strip()
    return line.split(": ", 1)[1].strip()


if __name__ == "__main__":
    print(clean_line("[00:00] Speaker: Hallo."))

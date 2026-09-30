def filter_records(records, exclude_titel):
    """Entfernt Records, deren Titel eines der Schlagwörter enthält (case-insensitive)."""
    if not exclude_titel:
        return list(records)
    needles = [k.casefold() for k in exclude_titel if k]
    if not needles:
        return list(records)
    out = []
    for r in records:
        titel = (r.get("titel") or "").casefold()
        if any(n in titel for n in needles):
            continue
        out.append(r)
    return out


if __name__ == "__main__":
    sample = [{"titel": "Vorlesung ML"}, {"titel": "Monolog"}]
    print(len(filter_records(sample, ["Vorlesung"])))

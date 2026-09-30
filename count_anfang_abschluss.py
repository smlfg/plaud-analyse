"""Anfangs- gegen Abschluss-Marker pro Transkript zaehlen."""

import re

from constants import ABSCHLUSS_MARKER, ANFANG_MARKER
from tokenize_fn import tokenize


def _count_marker(text, marker):
    pattern = r"(?i)\b" + re.escape(marker) + r"\b"
    return len(re.findall(pattern, text))


def _contexts(text, marker, ctx=40):
    pattern = r"(?i)\b" + re.escape(marker) + r"\b"
    out = []
    for m in re.finditer(pattern, text):
        s = max(0, m.start() - ctx)
        e = min(len(text), m.end() + ctx)
        out.append(text[s:e].replace("\n", " "))
    return out


def count_anfang_abschluss(text):
    woerter = tokenize(text)
    n = len(woerter)
    anfang_raw = sum(_count_marker(text, m) for m in ANFANG_MARKER)
    abschluss_raw = sum(_count_marker(text, m) for m in ABSCHLUSS_MARKER)
    anfang_per_1k = (anfang_raw / n * 1000.0) if n else 0.0
    abschluss_per_1k = (abschluss_raw / n * 1000.0) if n else 0.0
    anfang_kontexte = []
    for m in ANFANG_MARKER:
        anfang_kontexte.extend(f"{m}: {c}" for c in _contexts(text, m))
    abschluss_kontexte = []
    for m in ABSCHLUSS_MARKER:
        abschluss_kontexte.extend(f"{m}: {c}" for c in _contexts(text, m))
    return {
        "woerter_gesamt": n,
        "anfang_raw": anfang_raw,
        "abschluss_raw": abschluss_raw,
        "anfang_per_1k": round(anfang_per_1k, 3),
        "abschluss_per_1k": round(abschluss_per_1k, 3),
        "diff_per_1k": round(anfang_per_1k - abschluss_per_1k, 3),
        "anfang_kontexte": anfang_kontexte,
        "abschluss_kontexte": abschluss_kontexte,
    }


if __name__ == "__main__":
    sample = "Ich will das morgen bauen. Neue Idee: Agent. Ich baue das jetzt. Fertig, geschafft, laeuft, abgeschlossen."
    from pprint import pprint
    pprint(count_anfang_abschluss(sample))
"""Micro-Test: Anfangs-/Abschluss-Marker, parse_speakers, primary_cohort."""

import tempfile
from pathlib import Path

from constants import ABSCHLUSS_MARKER, ANFANG_MARKER
from count_anfang_abschluss import _count_marker, _contexts, count_anfang_abschluss
from parse_speakers import parse_speakers
from primary_cohort import primary_cohort
from constants import SAMUEL_FLG


def test_alle_marker_case_insensitive():
    # jeder der 4 Anfangs- und 4 Abschluss-Marker muss case-insensitive matchen
    samples = {
        "ich will": "ICH WILL los.",
        "man könnte": "Man Könnte auch warten.",
        "neue Idee": "NEUE IDEE da.",
        "ich baue": "Ich BAue gleich.",
        "fertig": "FERTIG.",
        "geschafft": "GeSchaffT.",
        "läuft": "LÄUFT.",
        "abgeschlossen": "ABGESCHLOSSEN.",
    }
    for marker, text in samples.items():
        assert _count_marker(text, marker) == 1, (marker, text)


def test_wortgrenzen():
    # Wortgrenzen: "ich willen" darf NICHT als "ich will" zaehlen
    assert _count_marker("ich willen mehr", "ich will") == 0
    # Wortgrenzen: "ich will" am Satzende schon
    assert _count_marker("ich will.", "ich will") == 1
    # Wortgrenzen: Umlaut im Marker
    assert _count_marker("Man könnte was sagen.", "man könnte") == 1
    # Wortgrenzen: Suffix darf nicht matchen
    assert _count_marker("abgeschlossenheit", "abgeschlossen") == 0
    assert _count_marker("fertigung", "fertig") == 0


def test_leerer_text():
    # leere / fast leere Texte ergeben Nullen, kein Crash
    assert count_anfang_abschluss("")["woerter_gesamt"] == 0
    assert count_anfang_abschluss("")["anfang_raw"] == 0
    assert count_anfang_abschluss("")["abschluss_raw"] == 0
    assert count_anfang_abschluss("")["anfang_per_1k"] == 0.0
    assert count_anfang_abschluss("")["abschluss_per_1k"] == 0.0


def test_mehrere_treffer_ein_kontext_pro_treffer():
    # ein Marker 3x im Text -> 3 Treffer, 3 Kontexte (genau einer pro Treffer)
    text = "Ich will A. Ich will B. Ich will C."
    assert _count_marker(text, "ich will") == 3
    kontexte = _contexts(text, "ich will", ctx=10)
    assert len(kontexte) == 3
    # jeder Kontext enthaelt den Marker (case-insensitive)
    for k in kontexte:
        assert "ich will" in k.lower()


def test_parse_speakers_echte_plaud_zeile():
    # echte Plaud-Zeile: '[hh:mm - hh:mm] Sprecher: text'
    raw = (
        "[00:00 - 00:05] Samuel Flg: Hallo.\n"
        "[00:05 - 00:10] Speaker 1: Antwort.\n"
    )
    parsed = parse_speakers(raw)
    assert parsed is not None
    assert parsed == [("Samuel Flg", "Hallo."), ("Speaker 1", "Antwort.")]


def test_parse_speakers_ohne_timestamp_verworfen():
    # Zeile ohne fuehrenden Timestamp wird verworfen (parse_speakers returnt None)
    raw_no_ts = "Samuel Flg: Hallo.\n"
    assert parse_speakers(raw_no_ts) is None
    raw_kein_prefix = "[00:00 - 00:05] Samuel Flg\n"
    assert parse_speakers(raw_kein_prefix) is None


def test_primary_cohort_samuel_monolog_vs_gemischt():
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        samuel_only = root / "samuel_only.txt"
        samuel_only.write_text(
            "[00:00 - 00:05] Samuel Flg: Ich will das.\n"
            "[00:05 - 00:10] Samuel Flg: Fertig.\n",
            encoding="utf-8",
        )
        mixed = root / "mixed.txt"
        mixed.write_text(
            "[00:00 - 00:05] Samuel Flg: Ich will das.\n"
            "[00:05 - 00:10] Speaker 1: Antwort.\n",
            encoding="utf-8",
        )
        cohort = primary_cohort(import_dir=d)
        names = {p.name for p in cohort}
        assert names == {"samuel_only.txt"}, names
        # Plaud-spezifischer Marker bleibt vorhanden
        assert SAMUEL_FLG == "Samuel Flg"


if __name__ == "__main__":
    test_alle_marker_case_insensitive()
    test_wortgrenzen()
    test_leerer_text()
    test_mehrere_treffer_ein_kontext_pro_treffer()
    test_parse_speakers_echte_plaud_zeile()
    test_parse_speakers_ohne_timestamp_verworfen()
    test_primary_cohort_samuel_monolog_vs_gemischt()
    print("ok")
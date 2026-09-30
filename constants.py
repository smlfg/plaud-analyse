"""Pfade und Regex — nur Daten, keine Funktionen."""

import re
from pathlib import Path

BASE = Path(__file__).parent
IMPORT_DIR = BASE / "PlaudImport"
CLEAN_DIR = BASE / "PlaudImportClean"
PLOTS_DIR = BASE / "plots"
INDEX_FILE = BASE / "plaud_index.csv"
GRAPHIFY_DIR = BASE / "graphify-out"
ANFANG_ABSCHLUSS_CSV = GRAPHIFY_DIR / "anfang_abschluss.csv"
ZEIT_ANFANG_ABSCHLUSS_PNG = PLOTS_DIR / "zeit_anfang_abschluss.png"

SAMUEL_FLG = "Samuel Flg"

EXCLUDE_TITEL_DEFAULTS = ("vorlesung", "vortrag")

ANFANG_MARKER = ("ich will", "man könnte", "neue Idee", "ich baue")
ABSCHLUSS_MARKER = ("fertig", "geschafft", "läuft", "abgeschlossen")

STOPWORDS = {
    "a", "ab", "aber", "alle", "allem", "allen", "aller", "alles", "als", "also", "am", "an",
    "and", "ander", "andere", "anderem", "anderen", "anderer", "anderes", "auch", "auf", "aus",
    "bei", "bin", "bis", "bist", "da", "dadurch", "daher", "darum", "das", "dass", "dein",
    "deine", "dem", "den", "denn", "der", "des", "dessen", "dich", "die", "dies", "diese",
    "diesem", "diesen", "dieser", "dieses", "doch", "du", "durch", "ein", "eine", "einem",
    "einen", "einer", "eines", "er", "es", "euch", "euer", "eure", "für", "gegen", "hab",
    "habe", "haben", "hat", "hatte", "hattest", "hattet", "hier", "hin", "hinter", "ich",
    "ihm", "ihn", "ihr", "ihre", "im", "in", "ist", "ja", "jede", "jedem", "jeden", "jeder",
    "jedes", "jene", "jenem", "jenen", "jener", "jenes", "jetzt", "kann", "kannst", "können",
    "könnt", "machen", "man", "mein", "meine", "mit", "muss", "musst", "nach", "nicht", "noch",
    "nun", "nur", "ob", "oder", "oh", "sehr", "sein", "seine", "sich", "sie", "sind", "so",
    "solche", "solchem", "solchen", "solcher", "solches", "soll", "sollte", "sondern", "sonst",
    "über", "um", "und", "uns", "unse", "unser", "unsere", "unter", "viel", "vom", "von", "vor",
    "war", "waren", "warst", "was", "weg", "weil", "weiter", "welche", "welchem", "welchen",
    "welcher", "welches", "wenn", "wer", "werde", "werden", "werdet", "wie", "wieder", "will",
    "wir", "wird", "wirst", "wo", "wollen", "wollte", "während", "würde", "würden", "zu", "zum",
    "zur", "zwar", "zwischen", "mal", "halt", "eben", "eigentlich", "irgendwie", "quasi",
    "nee", "ne", "okay", "ok", "äh", "ähm", "hm", "mhm",
}

WORD_RE = re.compile(r"\b[\wäöüßÄÖÜ]+\b", re.UNICODE)
SENT_SPLIT = re.compile(r"[.!?]+")

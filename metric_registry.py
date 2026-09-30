def metric_registry():
    """Metrik-Name → {key, needs_dauer, ylabel} (ylabel deutsch, für Plots)."""
    return {
        "vielfalt": {"key": "vielfalt", "needs_dauer": False, "ylabel": "Vielfalt"},
        "hapax": {"key": "hapax", "needs_dauer": False, "ylabel": "Hapax-Anteil"},
        "wpm": {"key": "wpm", "needs_dauer": True, "ylabel": "Wörter pro Minute"},
        "fuellwort_rate": {
            "key": "fuellwort_rate",
            "needs_dauer": False,
            "ylabel": "Füllwort-Anteil",
        },
        "wortlaenge_avg": {
            "key": "wortlaenge_avg",
            "needs_dauer": False,
            "ylabel": "Ø Wortlänge (Zeichen)",
        },
        "satzlaenge_avg": {
            "key": "satzlaenge_avg",
            "needs_dauer": False,
            "ylabel": "Ø Satzlänge (Wörter)",
        },
        "inhalt_anteil": {
            "key": "inhalt_anteil",
            "needs_dauer": False,
            "ylabel": "Anteil Inhaltswörter (ohne Füllwörter)",
        },
        "wiederholungs_rate": {
            "key": "wiederholungs_rate",
            "needs_dauer": False,
            "ylabel": "Wiederholungsrate",
        },
        "woerter_gesamt": {
            "key": "woerter_gesamt",
            "needs_dauer": False,
            "ylabel": "Wörter gesamt",
        },
        "unique_count": {
            "key": "unique_count",
            "needs_dauer": False,
            "ylabel": "Verschiedene Wörter",
        },
        "max_wort_anteil": {
            "key": "max_wort_anteil",
            "needs_dauer": False,
            "ylabel": "Max. Wort-Anteil",
        },
        "satz_anzahl": {"key": "satz_anzahl", "needs_dauer": False, "ylabel": "Satzanzahl"},
        "anfang_per_1k": {
            "key": "anfang_per_1k",
            "needs_dauer": False,
            "ylabel": "Anfangs-Marker pro 1000 Wörter",
        },
        "abschluss_per_1k": {
            "key": "abschluss_per_1k",
            "needs_dauer": False,
            "ylabel": "Abschluss-Marker pro 1000 Wörter",
        },
        "diff_per_1k": {
            "key": "diff_per_1k",
            "needs_dauer": False,
            "ylabel": "Diff. Anfang/Abschluss pro 1000 Wörter",
        },
    }


if __name__ == "__main__":
    for name in sorted(metric_registry()):
        print(name)

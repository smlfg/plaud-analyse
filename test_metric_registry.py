from metric_registry import metric_registry


def test_metric_registry_keys():
    reg = metric_registry()
    documented = [
        "vielfalt",
        "hapax",
        "wpm",
        "fuellwort_rate",
        "wortlaenge_avg",
        "satzlaenge_avg",
        "inhalt_anteil",
        "wiederholungs_rate",
        "woerter_gesamt",
        "unique_count",
        "max_wort_anteil",
        "satz_anzahl",
        "anfang_per_1k",
        "abschluss_per_1k",
        "diff_per_1k",
    ]
    for name in documented:
        assert name in reg, name
        spec = reg[name]
        assert "key" in spec and "needs_dauer" in spec and "ylabel" in spec
        assert spec["key"] == name


if __name__ == "__main__":
    test_metric_registry_keys()
    print("ok")

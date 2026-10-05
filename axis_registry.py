def axis_registry():
    """Achsen-Name → {key, label, needs_index} (zeit, uhrzeit, dauer, woerter)."""
    return {
        "zeit": {"key": "start", "label": "Aufnahmedatum", "needs_index": False},
        "uhrzeit": {
            "key": "uhrzeit",
            "label": "Uhrzeit (Stunden 0–24)",
            "needs_index": True,
        },
        "dauer": {
            "key": "dauer_sek",
            "label": "Aufnahmedauer (Sekunden)",
            "needs_index": True,
        },
        "woerter": {"key": "woerter_gesamt", "label": "Wörter gesamt", "needs_index": False},
    }


if __name__ == "__main__":
    for name in sorted(axis_registry()):
        print(name)

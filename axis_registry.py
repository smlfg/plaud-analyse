def axis_registry():
    """Achsen-Name → {key, label, needs_index} (nur zeit / dauer / woerter)."""
    return {
        "zeit": {"key": "start", "label": "Aufnahmezeit", "needs_index": False},
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

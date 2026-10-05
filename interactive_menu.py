import argparse

from dimension_names import dimension_names
from metric_registry import metric_registry


def _empty_namespace():
    return argparse.Namespace(
        metrics=None,
        x=None,
        ys=[],
        all=False,
        list_only=False,
        terminal=False,
        exclude_titel=[],
        quit=False,
    )


def _quit_namespace():
    return argparse.Namespace(
        metrics=None,
        x=None,
        ys=[],
        all=False,
        list_only=False,
        terminal=False,
        exclude_titel=[],
        quit=True,
    )


def _xy_plot_interactive():
    """X/Y per questionary wählen; bei Fehler einfacher input()-Fallback."""
    dims = dimension_names()
    x = None
    ys = []
    try:
        import questionary

        x = questionary.autocomplete(
            "X-Dimension:",
            choices=dims,
            validate=lambda t: t in dims or "Unbekannte Dimension",
        ).ask()
        if x is None:
            return _empty_namespace()
        y_choices = [d for d in dims if d != x]
        ys = questionary.checkbox(
            "Y-Dimension(en) (mind. eine):",
            choices=y_choices,
            validate=lambda sel: len(sel) > 0 or "Mindestens eine Y-Dimension wählen",
        ).ask()
        if not ys:
            return _empty_namespace()
    except Exception:
        print("Hinweis: questionary nicht verfügbar — Eingabe per Tastatur.")
        print(f"Dimensionen: {', '.join(dims)}")
        x = input("X-Dimension: ").strip()
        if x not in dims:
            print(f"Unbekannte Dimension: {x!r}")
            return _empty_namespace()
        y_raw = input("Y-Dimension(en), kommagetrennt: ").strip()
        for part in y_raw.split(","):
            name = part.strip()
            if name and name in dims and name != x:
                ys.append(name)
        if not ys:
            print("Keine gültige Y-Dimension gewählt.")
            return _empty_namespace()

    terminal = input("Im Terminal anzeigen statt PNG? (j/N): ").strip().lower() in (
        "j",
        "ja",
        "y",
    )
    return argparse.Namespace(
        metrics=None,
        x=x,
        ys=ys,
        all=False,
        list_only=False,
        terminal=terminal,
        exclude_titel=[],
        quit=False,
    )


def interactive_menu():
    """Interaktive Auswahl; Namespace wie parse_analyse_args (ohne sys.argv)."""
    print("Analyse-CLI (interaktiv)")
    print("  1) Metriken-Tabelle")
    print("  2) XY-Plot")
    print("  3) Alles (--all)")
    print("  4) Achsen/Metriken listen")
    print("  5) Beenden")
    choice = input("Auswahl [1-5, q=Beenden]: ").strip()
    choice_lc = choice.lower()
    if choice == "5" or choice_lc in ("q", "quit"):
        return _quit_namespace()

    metrics = None
    x = None
    ys = []
    all_flag = False
    list_only = False
    terminal = False

    if choice == "4":
        list_only = True
    elif choice == "3":
        all_flag = True
    elif choice == "2":
        return _xy_plot_interactive()
    elif choice == "1":
        reg = metric_registry()
        y_names = ", ".join(sorted(reg))
        print(f"Metriken: {y_names}")
        raw = input("Metriken (kommagetrennt): ").strip()
        metrics = []
        for p in raw.split(","):
            name = p.strip()
            if not name:
                continue
            if name not in reg:
                print(f"Unbekannte Metrik (ignoriert): {name!r}")
                continue
            metrics.append(name)
    else:
        print("Unbekannte Auswahl.")
        return _empty_namespace()

    return argparse.Namespace(
        metrics=metrics if metrics else None,
        x=x or None,
        ys=ys,
        all=all_flag,
        list_only=list_only,
        terminal=terminal,
        exclude_titel=[],
        quit=False,
    )


if __name__ == "__main__":
    print(interactive_menu())

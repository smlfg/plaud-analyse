import argparse

from axis_registry import axis_registry
from metric_registry import metric_registry


def interactive_menu():
    """Interaktive Auswahl; Namespace wie parse_analyse_args (ohne sys.argv)."""
    print("Analyse-CLI (interaktiv)")
    print("  1) Metriken-Tabelle")
    print("  2) XY-Plot")
    print("  3) Alles (--all)")
    print("  4) Achsen/Metriken listen")
    choice = input("Auswahl [1-4]: ").strip()

    metrics = None
    x = None
    ys = []
    all_flag = False
    list_only = False
    exclude_titel = []

    ex = input("Titel ausschließen (Komma-getrennt, leer=keiner): ").strip()
    if ex:
        exclude_titel = [p.strip() for p in ex.split(",") if p.strip()]

    if choice == "4":
        list_only = True
    elif choice == "3":
        all_flag = True
    elif choice == "2":
        ax_names = ", ".join(sorted(axis_registry()))
        y_names = ", ".join(sorted(metric_registry()))
        print(f"Achsen: {ax_names}")
        x = input("X-Achse: ").strip()
        if x not in axis_registry():
            print(f"Unbekannte Achse: {x!r}")
            return argparse.Namespace(
                metrics=None,
                x=None,
                ys=[],
                all=False,
                list_only=False,
                exclude_titel=exclude_titel,
            )
        print(f"Metriken: {y_names}")
        y_raw = input("Y-Metrik(en), kommagetrennt: ").strip()
        for part in y_raw.split(","):
            name = part.strip()
            if name and name in metric_registry():
                ys.append(name)
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
        return argparse.Namespace(
            metrics=None,
            x=None,
            ys=[],
            all=False,
            list_only=False,
            exclude_titel=exclude_titel,
        )

    return argparse.Namespace(
        metrics=metrics if metrics else None,
        x=x or None,
        ys=ys,
        all=all_flag,
        list_only=list_only,
        exclude_titel=exclude_titel,
    )


if __name__ == "__main__":
    print(interactive_menu())

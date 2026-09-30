import sys

from constants import IMPORT_DIR, PLOTS_DIR
from filter_records import filter_records
from interactive_menu import interactive_menu
from metric_registry import metric_registry
from axis_registry import axis_registry
from parse_analyse_args import parse_analyse_args
from plot_xy import plot_xy
from run_analyse import run_analyse
from sammle_records import sammle_records


def run_analyse_cli(argv=None):
    """Einstieg: interaktiv (TTY), --list, --metric, --x/--y, oder --all."""
    if argv is None and len(sys.argv) <= 1:
        if not sys.stdin.isatty():
            print(
                "Keine Argumente und keine interaktive Eingabe (stdin ist keine TTY).\n"
                "Beispiele:\n"
                "  python run_analyse_cli.py --list\n"
                "  python run_analyse_cli.py --x zeit --y vielfalt\n"
                "  python run_analyse_cli.py --all",
                file=sys.stderr,
            )
            sys.exit(2)
        ns = interactive_menu()
    else:
        ns = parse_analyse_args(argv)

    if ns.list_only:
        print("Achsen (--x):")
        for name, spec in sorted(axis_registry().items()):
            idx = " (Index/Dauer nötig)" if spec["needs_index"] else ""
            print(f"  {name}: {spec['label']}{idx}")
        print("\nMetriken (--y / --metric):")
        for name, spec in sorted(metric_registry().items()):
            dauer = " (Dauer nötig)" if spec["needs_dauer"] else ""
            print(f"  {name}: {spec['ylabel']}{dauer}")
        return 0

    if ns.all:
        run_analyse()
        return 0

    if not IMPORT_DIR.is_dir():
        print(f"Ordner fehlt: {IMPORT_DIR}")
        return 1

    records = filter_records(sammle_records(), ns.exclude_titel)
    if ns.exclude_titel:
        print(f"{len(records)} Records nach Titel-Filter.")

    if ns.metrics:
        reg = metric_registry()
        unknown = [c for c in ns.metrics if c not in reg]
        if unknown:
            print(f"Unbekannte Metrik(en): {', '.join(unknown)}")
            return 1
        cols = ns.metrics
        header = ["datei"] + cols
        print("\t".join(header))
        for r in records:
            row = [r.get("datei", "")]
            for c in cols:
                v = r.get(reg[c]["key"])
                if isinstance(v, float):
                    row.append(f"{v:.3f}")
                else:
                    row.append(str(v) if v is not None else "")
            print("\t".join(row))
        if not ns.x and not ns.ys:
            return 0

    if ns.x and ns.ys:
        PLOTS_DIR.mkdir(exist_ok=True)
        ok = 0
        for y_name in ns.ys:
            if plot_xy(records, ns.x, y_name, plots_dir=PLOTS_DIR):
                ok += 1
        print(f"{ok}/{len(ns.ys)} Plot(s) in {PLOTS_DIR}/")
        return 0 if ok == len(ns.ys) else 1

    if ns.x and not ns.ys:
        print("Für einen Plot mindestens ein --y angeben.")
        return 1

    if not ns.metrics:
        print("Nichts zu tun — --list, --metric, --x/--y oder --all wählen.")
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(run_analyse_cli())

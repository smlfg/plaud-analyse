import argparse

from axis_registry import axis_registry
from constants import EXCLUDE_TITEL_DEFAULTS
from metric_registry import metric_registry


def parse_analyse_args(argv=None):
    """CLI-Argumente für run_analyse_cli (Namespace mit metrics, x, ys, all, list_only, exclude_titel)."""
    metric_keys = sorted(metric_registry())
    axis_keys = sorted(axis_registry())
    p = argparse.ArgumentParser(
        description="Plaud-Transkript-Analyse: Metriken tabellarisch oder XY-Plots.",
        epilog=(
            "Mehrere --y erzeugen je eine PNG (kein Multi-Trace in einem Bild). "
            f"Titel-Filter z. B.: --exclude-titel Vorlesung --exclude-titel Vortrag "
            f"(Vorschläge: {', '.join(EXCLUDE_TITEL_DEFAULTS)})."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument(
        "--list",
        action="store_true",
        dest="list_only",
        help="Verfügbare Achsen und Metriken auflisten.",
    )
    p.add_argument(
        "--all",
        action="store_true",
        help="Vollständige Analyse wie run_analyse.py (alle Plots, CSV, Statuszeilen).",
    )
    p.add_argument(
        "--metric",
        type=str,
        default=None,
        help="Kommagetrennte Metriken für die Tabelle (z. B. vielfalt,hapax).",
    )
    p.add_argument("--x", choices=axis_keys, default=None, help="X-Achse für Plot.")
    p.add_argument(
        "--y",
        action="append",
        choices=metric_keys,
        default=[],
        dest="ys",
        help="Y-Metrik (mehrfach = mehrere PNGs, je ein Plot pro --y).",
    )
    p.add_argument(
        "--exclude-titel",
        action="append",
        default=[],
        dest="exclude_titel",
        metavar="KEYWORD",
        help="Records auslassen, wenn Titel KEYWORD enthält (wiederholbar).",
    )
    ns = p.parse_args(argv)
    metrics = None
    if ns.metric:
        metrics = [m.strip() for m in ns.metric.split(",") if m.strip()]
        bad = [m for m in metrics if m not in metric_registry()]
        if bad:
            p.error(f"Unbekannte Metrik(en): {', '.join(bad)}")
    ns.metrics = metrics
    return ns


if __name__ == "__main__":
    print(parse_analyse_args(["--list"]))

from pathlib import Path

from axis_registry import axis_registry
from constants import PLOTS_DIR
from metric_registry import metric_registry
from scatter_save import scatter_save


def plot_xy(records, x_name, y_name, plots_dir=None, title=None, out_name=None):
    """Scatter-Plot einer Metrik über eine Achse; True wenn PNG geschrieben."""
    axes = axis_registry()
    metrics = metric_registry()
    if x_name not in axes:
        print(f"Unbekannte X-Achse: {x_name!r}")
        return False
    if y_name not in metrics:
        print(f"Unbekannte Metrik: {y_name!r}")
        return False

    x_spec = axes[x_name]
    y_spec = metrics[y_name]
    x_key = x_spec["key"]
    y_key = y_spec["key"]
    xlabel = x_spec["label"]
    ylabel = y_spec["ylabel"]

    rows = []
    for r in records:
        xv = r.get(x_key)
        yv = r.get(y_key)
        if xv is None or yv is None:
            continue
        if x_spec["needs_index"] and xv is None:
            continue
        if y_spec["needs_dauer"] and r.get("dauer_sek") is None:
            continue
        rows.append(r)

    if not rows:
        if x_spec["needs_index"]:
            print(
                f"Keine Datenpunkte für {x_name} vs. {y_name}: "
                "plaud_index.csv mit Dauer nötig (python3 plaud_index.py)."
            )
        elif y_spec["needs_dauer"]:
            print(
                f"Keine Datenpunkte für {x_name} vs. {y_name}: "
                "Metrik braucht Aufnahmedauer aus dem Index."
            )
        else:
            print(f"Keine Datenpunkte für {x_name} vs. {y_name}.")
        return False

    plot_title = title if title is not None else f"{ylabel} über {xlabel}"
    out = Path(plots_dir) if plots_dir else PLOTS_DIR
    out.mkdir(exist_ok=True)
    fname = out_name if out_name else f"{x_name}_vs_{y_name}.png"
    path = out / fname

    return scatter_save(
        [r[x_key] for r in rows],
        [r[y_key] for r in rows],
        xlabel,
        ylabel,
        plot_title,
        path,
    )


if __name__ == "__main__":
    from sammle_records import sammle_records

    plot_xy(sammle_records(), "zeit", "vielfalt")

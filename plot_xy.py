from pathlib import Path

from constants import PLOTS_DIR
from plot_rows import plot_rows
from scatter_save import scatter_save


def plot_xy(records, x_name, y_name, plots_dir=None, title=None, out_name=None):
    """Scatter-Plot einer Metrik über eine Achse; True wenn PNG geschrieben."""
    spec = plot_rows(records, x_name, y_name)
    if spec is None:
        return False

    x_key = spec["x_key"]
    y_key = spec["y_key"]

    plot_title = title if title is not None else spec["title"]
    out = Path(plots_dir) if plots_dir else PLOTS_DIR
    out.mkdir(exist_ok=True)
    fname = out_name if out_name else f"{x_name}_vs_{y_name}.png"
    path = out / fname

    return scatter_save(
        [r[x_key] for r in spec["rows"]],
        [r[y_key] for r in spec["rows"]],
        spec["xlabel"],
        spec["ylabel"],
        plot_title,
        path,
    )


if __name__ == "__main__":
    from sammle_records import sammle_records

    plot_xy(sammle_records(), "zeit", "vielfalt")
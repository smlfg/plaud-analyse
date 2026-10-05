"""Terminal-Plot mit plotext — kein PNG, direkt im Terminal."""

from plot_rows import plot_rows

MARKER = "braille"
DATUM_FORM = "%Y-%m-%d"


def plot_terminal(records, x_name, y_name, title=None, colorless=False):
    """Scatter-Plot einer Metrik über eine Achse im Terminal; True wenn gezeichnet."""
    spec = plot_rows(records, x_name, y_name)
    if spec is None:
        return False

    import plotext as plt

    fig = plt.figure
    fig.clear()
    if spec["x_is_date"]:
        fig.date().activate(DATUM_FORM)
    signal = fig.signal(
        [r[spec["x_key"]] for r in spec["rows"]],
        [r[spec["y_key"]] for r in spec["rows"]],
        marker=MARKER,
    )
    signal.lines(False)
    fig.draw(signal)
    fig.title(title if title is not None else spec["title"])
    fig.label(spec["xlabel"], "x")
    fig.label(spec["ylabel"], "y")
    fig.show(colorless=colorless)
    return True


if __name__ == "__main__":
    from sammle_records import sammle_records

    plot_terminal(sammle_records(), "zeit", "vielfalt")
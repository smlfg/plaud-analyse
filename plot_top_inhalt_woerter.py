from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from top_inhalt_woerter import top_inhalt_woerter


def plot_top_inhalt_woerter(records, plots_dir=None, n=25):
    """Häufigste Inhaltswörter über alle Records aggregieren und als barh-PNG speichern."""
    parts = []
    for r in records:
        text = r.get("text") or r.get("clean") or ""
        if not str(text).strip():
            continue
        parts.append(text)
    if not parts:
        return False
    top = top_inhalt_woerter("\n".join(parts), n=n)
    if not top:
        return False
    labels, values = zip(*top)
    out = Path(plots_dir) if plots_dir else Path(__file__).parent / "plots"
    path = out / "top_inhalt_woerter.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    fig_h = max(4.0, len(labels) * 0.28)
    plt.figure(figsize=(8, fig_h))
    plt.barh(list(labels), list(values))
    plt.gca().invert_yaxis()
    plt.xlabel("Häufigkeit")
    plt.ylabel("Inhaltswort")
    plt.title(f"Top {n} Inhaltswörter (ohne Füllwörter, alle Aufnahmen)")
    plt.tight_layout()
    plt.savefig(path, dpi=120)
    plt.close()
    return True

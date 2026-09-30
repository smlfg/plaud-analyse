"""Plot: Anfangsrate, Abschlussrate und Differenz pro 1000 Woerter ueber die Zeit."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


def plot_zeit_anfang_abschluss(records, plots_dir=None):
    timed = [r for r in records if r.get("start") is not None]
    out = Path(plots_dir) if plots_dir else Path(__file__).parent / "plots"
    out.mkdir(parents=True, exist_ok=True)
    if not timed:
        return False
    x = [r["start"] for r in timed]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(x, [r["anfang_per_1k"] for r in timed], alpha=0.7,
               label="Anfangsrate (pro 1000 Wörter)", marker="o")
    ax.scatter(x, [r["abschluss_per_1k"] for r in timed], alpha=0.7,
               label="Abschlussrate (pro 1000 Wörter)", marker="s")
    ax.scatter(x, [r["diff_per_1k"] for r in timed], alpha=0.7,
               label="Differenz (Anfang − Abschluss)", marker="^")
    ax.set_xlabel("Aufnahmezeit")
    ax.set_ylabel("Treffer pro 1000 Wörter")
    ax.set_title("Anfangs- vs. Abschluss-Sprache über die Zeit")
    ax.legend(loc="best")
    fig.tight_layout()
    fig.savefig(out / "zeit_anfang_abschluss.png", dpi=120)
    plt.close(fig)
    return True


if __name__ == "__main__":
    from primary_cohort import primary_cohort
    from sammle_records import sammle_records

    cohort = {p.name for p in primary_cohort()}
    records = [r for r in sammle_records() if r["datei"] in cohort]
    for r in records:
        from count_anfang_abschluss import count_anfang_abschluss

        r.update(count_anfang_abschluss(r["text"]))
    plot_zeit_anfang_abschluss(records)
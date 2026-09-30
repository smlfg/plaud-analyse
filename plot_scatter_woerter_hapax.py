from plot_xy import plot_xy


def plot_scatter_woerter_hapax(records, plots_dir=None):
    return plot_xy(
        records,
        "woerter",
        "hapax",
        plots_dir=plots_dir,
        out_name="scatter_woerter_hapax.png",
        title="Hapax-Anteil vs. Transkriptlänge (Wörter)",
    )


if __name__ == "__main__":
    from sammle_records import sammle_records

    plot_scatter_woerter_hapax(sammle_records())

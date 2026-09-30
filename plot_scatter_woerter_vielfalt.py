from plot_xy import plot_xy


def plot_scatter_woerter_vielfalt(records, plots_dir=None):
    return plot_xy(
        records,
        "woerter",
        "vielfalt",
        plots_dir=plots_dir,
        out_name="scatter_woerter_vielfalt.png",
        title="Vielfalt vs. Transkriptlänge (Wörter)",
    )


if __name__ == "__main__":
    from sammle_records import sammle_records

    plot_scatter_woerter_vielfalt(sammle_records())

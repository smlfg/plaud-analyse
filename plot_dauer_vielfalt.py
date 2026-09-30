from plot_xy import plot_xy


def plot_dauer_vielfalt(records, plots_dir=None):
    return plot_xy(
        records,
        "dauer",
        "vielfalt",
        plots_dir=plots_dir,
        out_name="dauer_vielfalt.png",
        title="Vielfalt vs. Aufnahmedauer",
    )


if __name__ == "__main__":
    from sammle_records import sammle_records

    plot_dauer_vielfalt(sammle_records())

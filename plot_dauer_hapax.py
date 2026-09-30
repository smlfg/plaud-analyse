from plot_xy import plot_xy


def plot_dauer_hapax(records, plots_dir=None):
    return plot_xy(
        records,
        "dauer",
        "hapax",
        plots_dir=plots_dir,
        out_name="dauer_hapax.png",
        title="Hapax-Anteil vs. Aufnahmedauer",
    )


if __name__ == "__main__":
    from sammle_records import sammle_records

    plot_dauer_hapax(sammle_records())

from plot_xy import plot_xy


def plot_dauer_inhalt(records, plots_dir=None):
    return plot_xy(
        records,
        "dauer",
        "inhalt_anteil",
        plots_dir=plots_dir,
        out_name="dauer_inhalt_woerter.png",
        title="Inhaltswort-Anteil vs. Aufnahmedauer",
    )


if __name__ == "__main__":
    from sammle_records import sammle_records

    plot_dauer_inhalt(sammle_records())

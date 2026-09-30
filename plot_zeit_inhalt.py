from plot_xy import plot_xy


def plot_zeit_inhalt(records, plots_dir=None):
    return plot_xy(
        records,
        "zeit",
        "inhalt_anteil",
        plots_dir=plots_dir,
        out_name="zeit_inhalt_woerter.png",
        title="Inhaltswort-Anteil über die Zeit",
    )


if __name__ == "__main__":
    from sammle_records import sammle_records

    plot_zeit_inhalt(sammle_records())

from plot_xy import plot_xy


def plot_dauer_wortlaenge(records, plots_dir=None):
    return plot_xy(
        records,
        "dauer",
        "wortlaenge_avg",
        plots_dir=plots_dir,
        out_name="dauer_wortlaenge.png",
        title="Ø Wortlänge vs. Aufnahmedauer",
    )


if __name__ == "__main__":
    from sammle_records import sammle_records

    plot_dauer_wortlaenge(sammle_records())

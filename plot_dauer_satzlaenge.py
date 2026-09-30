from plot_xy import plot_xy


def plot_dauer_satzlaenge(records, plots_dir=None):
    return plot_xy(
        records,
        "dauer",
        "satzlaenge_avg",
        plots_dir=plots_dir,
        out_name="dauer_satzlaenge.png",
        title="Ø Satzlänge vs. Aufnahmedauer",
    )


if __name__ == "__main__":
    from sammle_records import sammle_records

    plot_dauer_satzlaenge(sammle_records())

from plot_xy import plot_xy


def plot_zeit_satzlaenge(records, plots_dir=None):
    return plot_xy(
        records,
        "zeit",
        "satzlaenge_avg",
        plots_dir=plots_dir,
        out_name="zeit_satzlaenge.png",
        title="Durchschnittliche Satzlänge über die Zeit",
    )


if __name__ == "__main__":
    from sammle_records import sammle_records

    plot_zeit_satzlaenge(sammle_records())

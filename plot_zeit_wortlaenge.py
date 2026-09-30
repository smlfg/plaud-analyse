from plot_xy import plot_xy


def plot_zeit_wortlaenge(records, plots_dir=None):
    return plot_xy(
        records,
        "zeit",
        "wortlaenge_avg",
        plots_dir=plots_dir,
        out_name="zeit_wortlaenge.png",
        title="Durchschnittliche Wortlänge über die Zeit",
    )


if __name__ == "__main__":
    from sammle_records import sammle_records

    plot_zeit_wortlaenge(sammle_records())

from plot_xy import plot_xy


def plot_zeit_wiederholung(records, plots_dir=None):
    return plot_xy(
        records,
        "zeit",
        "wiederholungs_rate",
        plots_dir=plots_dir,
        out_name="zeit_wiederholung.png",
        title="Wiederholungsrate über die Zeit",
    )


if __name__ == "__main__":
    from sammle_records import sammle_records

    plot_zeit_wiederholung(sammle_records())

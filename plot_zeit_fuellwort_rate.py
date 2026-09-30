from plot_xy import plot_xy


def plot_zeit_fuellwort_rate(records, plots_dir=None):
    return plot_xy(
        records,
        "zeit",
        "fuellwort_rate",
        plots_dir=plots_dir,
        out_name="zeit_fuellwort_rate.png",
        title="Füllwort-Anteil über die Zeit",
    )


if __name__ == "__main__":
    from sammle_records import sammle_records

    plot_zeit_fuellwort_rate(sammle_records())

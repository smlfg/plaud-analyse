from plot_xy import plot_xy


def plot_zeit_vielfalt(records, plots_dir=None):
    return plot_xy(
        records,
        "zeit",
        "vielfalt",
        plots_dir=plots_dir,
        out_name="zeit_vielfalt.png",
        title="Vielfalt über die Zeit",
    )


if __name__ == "__main__":
    from sammle_records import sammle_records

    plot_zeit_vielfalt(sammle_records())

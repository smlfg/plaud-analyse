from plot_xy import plot_xy


def plot_zeit_hapax(records, plots_dir=None):
    return plot_xy(
        records,
        "zeit",
        "hapax",
        plots_dir=plots_dir,
        out_name="zeit_hapax.png",
        title="Hapax-Anteil über die Zeit",
    )


if __name__ == "__main__":
    from sammle_records import sammle_records

    plot_zeit_hapax(sammle_records())

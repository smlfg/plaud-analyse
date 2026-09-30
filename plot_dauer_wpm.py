from plot_xy import plot_xy


def plot_dauer_wpm(records, plots_dir=None):
    return plot_xy(
        records,
        "dauer",
        "wpm",
        plots_dir=plots_dir,
        out_name="dauer_wpm.png",
        title="Wörter pro Minute vs. Aufnahmedauer",
    )


if __name__ == "__main__":
    from sammle_records import sammle_records

    plot_dauer_wpm(sammle_records())

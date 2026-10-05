from datetime import datetime
from pathlib import Path

from plot_xy import plot_xy


def test_plot_xy_zeit_vielfalt():
    plots = Path(__file__).parent / "plots"
    plots.mkdir(exist_ok=True)
    records = [
        {
            "start": datetime(2026, 1, 1),
            "dauer_sek": None,
            "vielfalt": 0.5,
            "titel": "",
        },
        {
            "start": datetime(2026, 2, 1),
            "dauer_sek": 120,
            "vielfalt": 0.7,
            "titel": "",
        },
    ]
    out = plots / "_test_zeit_vs_vielfalt.png"
    if out.exists():
        out.unlink()
    assert plot_xy(records, "zeit", "vielfalt", plots_dir=plots, out_name="_test_zeit_vs_vielfalt.png")
    assert out.is_file()
    out.unlink()


def test_plot_xy_dauer_without_index_message():
    records = [{"start": datetime(2026, 1, 1), "dauer_sek": None, "vielfalt": 0.5, "titel": ""}]
    ok = plot_xy(records, "dauer", "vielfalt", plots_dir=Path(__file__).parent / "plots")
    assert ok is False


def test_plot_xy_metric_vs_metric():
    plots = Path(__file__).parent / "plots"
    plots.mkdir(exist_ok=True)
    records = [
        {"vielfalt": 0.4, "hapax": 0.2, "titel": ""},
        {"vielfalt": 0.6, "hapax": 0.35, "titel": ""},
        {"vielfalt": 0.5, "hapax": None, "titel": ""},
    ]
    out = plots / "_test_vielfalt_vs_hapax.png"
    if out.exists():
        out.unlink()
    assert plot_xy(
        records,
        "vielfalt",
        "hapax",
        plots_dir=plots,
        out_name="_test_vielfalt_vs_hapax.png",
    )
    assert out.is_file()
    out.unlink()


def test_plot_xy_uhrzeit_wpm():
    plots = Path(__file__).parent / "plots"
    plots.mkdir(exist_ok=True)
    records = [
        {
            "uhrzeit": 9.5,
            "wpm": 120.0,
            "dauer_sek": 60,
            "titel": "",
        },
        {
            "uhrzeit": 14.25,
            "wpm": 95.0,
            "dauer_sek": 120,
            "titel": "",
        },
        {
            "uhrzeit": None,
            "wpm": 80.0,
            "dauer_sek": 60,
            "titel": "",
        },
    ]
    out = plots / "_test_uhrzeit_vs_wpm.png"
    if out.exists():
        out.unlink()
    assert plot_xy(
        records,
        "uhrzeit",
        "wpm",
        plots_dir=plots,
        out_name="_test_uhrzeit_vs_wpm.png",
    )
    assert out.is_file()
    out.unlink()


def test_plot_xy_axis_as_y():
    plots = Path(__file__).parent / "plots"
    plots.mkdir(exist_ok=True)
    records = [
        {
            "woerter_gesamt": 100,
            "dauer_sek": 60.0,
            "titel": "",
        },
        {
            "woerter_gesamt": 250,
            "dauer_sek": 120.0,
            "titel": "",
        },
    ]
    out = plots / "_test_woerter_vs_dauer.png"
    if out.exists():
        out.unlink()
    assert plot_xy(
        records,
        "woerter",
        "dauer",
        plots_dir=plots,
        out_name="_test_woerter_vs_dauer.png",
    )
    assert out.is_file()
    out.unlink()


if __name__ == "__main__":
    test_plot_xy_zeit_vielfalt()
    test_plot_xy_dauer_without_index_message()
    test_plot_xy_metric_vs_metric()
    test_plot_xy_uhrzeit_wpm()
    test_plot_xy_axis_as_y()
    print("ok")

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


if __name__ == "__main__":
    test_plot_xy_zeit_vielfalt()
    test_plot_xy_dauer_without_index_message()
    print("ok")

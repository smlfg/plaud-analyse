"""Kompatibilität — delegiert an run_analyse."""

from run_analyse import run_analyse


def run_plots():
    run_analyse()


if __name__ == "__main__":
    run_analyse()

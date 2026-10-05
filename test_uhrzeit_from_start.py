from datetime import datetime

from uhrzeit_from_start import uhrzeit_from_start


def test_uhrzeit_from_start_afternoon():
    assert uhrzeit_from_start(datetime(2026, 3, 1, 14, 30, 0)) == 14.5


def test_uhrzeit_from_start_with_seconds():
    assert uhrzeit_from_start(datetime(2026, 3, 1, 0, 0, 30)) == 30 / 3600


def test_uhrzeit_from_start_none():
    assert uhrzeit_from_start(None) is None


def test_uhrzeit_from_start_not_datetime():
    assert uhrzeit_from_start("2026-01-01") is None


if __name__ == "__main__":
    test_uhrzeit_from_start_afternoon()
    test_uhrzeit_from_start_with_seconds()
    test_uhrzeit_from_start_none()
    test_uhrzeit_from_start_not_datetime()
    print("ok")

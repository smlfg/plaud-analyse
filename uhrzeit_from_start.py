from datetime import datetime


def uhrzeit_from_start(start_dt):
    """datetime → Stunden float 0–24 (hour+minute/60+second/3600), sonst None."""
    if start_dt is None or not isinstance(start_dt, datetime):
        return None
    return start_dt.hour + start_dt.minute / 60 + start_dt.second / 3600


if __name__ == "__main__":
    from datetime import datetime as dt

    print(uhrzeit_from_start(dt(2026, 1, 1, 14, 30, 0)))

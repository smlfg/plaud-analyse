from datetime import datetime


def parse_start(start_str):
    if not start_str:
        return None
    for fmt in (
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%SZ",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
    ):
        try:
            return datetime.strptime(start_str.replace("+00:00", "Z"), fmt)
        except ValueError:
            continue
    try:
        cleaned = start_str.replace("Z", "+00:00")
        return datetime.fromisoformat(cleaned)
    except ValueError:
        return None


if __name__ == "__main__":
    print(parse_start("2026-06-02T14:30:00Z"))

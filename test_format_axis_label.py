from format_axis_label import format_axis_label


def test_format_axis_label_splits_on_whitespace():
    assert format_axis_label("Wörter pro Minute") == "Wörter\npro\nMinute"


def test_format_axis_label_empty():
    assert format_axis_label("") == ""
    assert format_axis_label(None) is None

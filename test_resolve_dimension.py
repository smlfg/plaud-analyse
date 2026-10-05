from resolve_dimension import resolve_dimension


def test_resolve_dimension_axis():
    spec = resolve_dimension("zeit")
    assert spec is not None
    assert spec["kind"] == "axis"
    assert spec["key"] == "start"
    assert spec["label"] == "Aufnahmedatum"
    assert spec["needs_index"] is False
    assert spec["needs_dauer"] is False


def test_resolve_dimension_metric():
    spec = resolve_dimension("vielfalt")
    assert spec is not None
    assert spec["kind"] == "metric"
    assert spec["key"] == "vielfalt"
    assert spec["label"] == "Vielfalt"
    assert spec["needs_index"] is False
    assert spec["needs_dauer"] is False


def test_resolve_dimension_metric_needs_dauer():
    spec = resolve_dimension("wpm")
    assert spec is not None
    assert spec["needs_dauer"] is True


def test_resolve_dimension_unknown():
    assert resolve_dimension("nicht_da") is None


if __name__ == "__main__":
    test_resolve_dimension_axis()
    test_resolve_dimension_metric()
    test_resolve_dimension_metric_needs_dauer()
    test_resolve_dimension_unknown()
    print("ok")

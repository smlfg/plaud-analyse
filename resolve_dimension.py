from axis_registry import axis_registry
from metric_registry import metric_registry


def resolve_dimension(name):
    """Name → {key, label, needs_index, needs_dauer, kind} oder None bei unbekannt/Kollision."""
    axes = axis_registry()
    metrics = metric_registry()
    in_axis = name in axes
    in_metric = name in metrics
    if in_axis and in_metric:
        print(f"Dimensions-Kollision: {name!r} ist Achse und Metrik zugleich.")
        return None
    if in_axis:
        spec = axes[name]
        return {
            "key": spec["key"],
            "label": spec["label"],
            "needs_index": spec["needs_index"],
            "needs_dauer": False,
            "kind": "axis",
        }
    if in_metric:
        spec = metrics[name]
        return {
            "key": spec["key"],
            "label": spec["ylabel"],
            "needs_index": False,
            "needs_dauer": spec["needs_dauer"],
            "kind": "metric",
        }
    return None

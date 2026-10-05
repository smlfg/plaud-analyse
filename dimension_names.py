from axis_registry import axis_registry
from metric_registry import metric_registry


def dimension_names():
    """Sortierte Vereinigung aller Achsen- und Metrik-Namen (für CLI/Autocomplete)."""
    return sorted(set(axis_registry()) | set(metric_registry()))

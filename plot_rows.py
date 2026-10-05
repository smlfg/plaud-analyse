from datetime import datetime

from format_axis_label import format_axis_label
from resolve_dimension import resolve_dimension


def plot_rows(records, x_name, y_name):
    """Gültige (x, y)-Punkte für einen XY-Plot; None bei unbekannt/leer (mit Meldung)."""
    x_spec = resolve_dimension(x_name)
    y_spec = resolve_dimension(y_name)
    if x_spec is None:
        print(f"Unbekannte Dimension (X): {x_name!r}")
        return None
    if y_spec is None:
        print(f"Unbekannte Dimension (Y): {y_name!r}")
        return None

    x_key = x_spec["key"]
    y_key = y_spec["key"]

    rows = []
    for r in records:
        xv = r.get(x_key)
        yv = r.get(y_key)
        if xv is None or yv is None:
            continue
        if x_spec["needs_dauer"] and r.get("dauer_sek") is None:
            continue
        if y_spec["needs_dauer"] and r.get("dauer_sek") is None:
            continue
        rows.append(r)

    if not rows:
        print(_kein_daten_hinweis(records, x_name, y_name, x_spec, y_spec))
        return None

    return {
        "rows": rows,
        "x_key": x_key,
        "y_key": y_key,
        "xlabel": x_spec["label"],
        "ylabel": format_axis_label(y_spec["label"]),
        "title": f"{y_spec['label']} über {x_spec['label']}",
        "x_is_date": any(isinstance(r[x_key], datetime) for r in rows),
    }


def _kein_daten_hinweis(records, x_name, y_name, x_spec, y_spec):
    needs_dauer = x_spec["needs_dauer"] or y_spec["needs_dauer"]
    if needs_dauer and all(r.get("dauer_sek") is None for r in records):
        return (
            f"Keine Datenpunkte für {x_name} vs. {y_name}: "
            "Mindestens eine Dimension braucht Aufnahmedauer aus dem Index."
        )
    if x_spec["needs_index"] and all(r.get(x_spec["key"]) is None for r in records):
        return (
            f"Keine Datenpunkte für {x_name} vs. {y_name}: "
            "plaud_index.csv mit Dauer nötig (python3 plaud_index.py)."
        )
    if y_spec["needs_index"] and all(r.get(y_spec["key"]) is None for r in records):
        return (
            f"Keine Datenpunkte für {x_name} vs. {y_name}: "
            "plaud_index.csv mit Dauer nötig (python3 plaud_index.py)."
        )
    return f"Keine Datenpunkte für {x_name} vs. {y_name}."


if __name__ == "__main__":
    from sammle_records import sammle_records

    print(plot_rows(sammle_records(), "zeit", "vielfalt"))

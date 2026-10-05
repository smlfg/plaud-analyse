def format_axis_label(text):
    """Achsenbeschriftung: Wörter mit Newline trennen (matplotlib/plotext)."""
    if not text:
        return text
    return "\n".join(text.split())

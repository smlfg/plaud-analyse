"""Micro-Test: Hapax = einmal vorkommende Wörter / Wörter gesamt."""

from hapax import hapax


def test_hapax():
    # a=2, b=1, c=1, d=1 → 3 Hapaxe / 5 Tokens
    assert hapax("a b a c d") == 0.6
    assert hapax("") == 0.0
    assert hapax("x x x") == 0.0


if __name__ == "__main__":
    test_hapax()
    print("ok")

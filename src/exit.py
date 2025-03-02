"""Modul för utgång."""

class Exit:
    """Representerar utgång."""
    def __init__(self, symbol="E"):
        self.symbol = symbol

    def __str__(self):
        return self.symbol

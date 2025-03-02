"""Modul för utgång."""

class Exit:
    """Representerar utgång."""
    def __init__(self, name, symbol="E"):
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return self.symbol

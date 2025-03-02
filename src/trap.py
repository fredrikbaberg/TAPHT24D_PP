"""Fälla som kan finnas på kartan."""

class Trap:
    """ Fälla. Ska ligga kvar på kartan. """
    def __init__(self, symbol="T"): # Tecknet 🕳️ tar för mycket plats, använder T för "Trap".
        self.name = 'trap'
        self.value = -10
        self.symbol = symbol
        self.disarmed = False

    def __str__(self):
        return self.symbol

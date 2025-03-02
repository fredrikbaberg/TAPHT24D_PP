"""Kista som kan finnas på kartan."""
# pylint: disable=too-few-public-methods

class Chest:
    """ Kista, kräver nyckel för att öppnas. """
    def __init__(self, symbol="C"): # Tecknet 💼 tar för mycket plats, använder C för "Chest".
        self.name = 'chest'
        self.symbol = symbol

    def __str__(self):
        return self.symbol

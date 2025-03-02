"""Olika typer av föremål att plocka upp."""
#pylint: disable=too-few-public-methods # Ingorera varning att klasser har för få publika metoder.
import random

class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=10, symbol="?", original=True):
        self.name = name
        self.value = value
        self.symbol = symbol
        self.original = original # För att hålla koll på om det fanns från början.

    def __str__(self):
        return self.symbol

class Fruit(Item):
    """ Frukt, ett Item med värde 20 poäng. """
    def __init__(self, name, symbol='?', original=True):
        super().__init__(name=name, value=20, symbol=symbol, original=original)

class Shovel(Item):
    """ Spade. Inga poäng, kan ta bort en vägg en gång. """
    def __init__(self, symbol='?'):
        super().__init__(name='shovel', value=0, symbol=symbol)

class Key(Item):
    """ Nyckel, krävs för att öppna kista. """
    def __init__(self):
        super().__init__(name='key', value=0, symbol='🗝') # Symbolen tar 1.5 ruta, men ser trevligare ut.

class Treasure(Item):
    """ Skatt. Ligger i skattkista. """
    def __init__(self):
        super().__init__(name='treasure', value=100, symbol='👑')


# DONE: D. Fruktsallad - alla frukter ska vara värda 20 poäng i stället för 10.
pickups = [
    Item("carrot"),
    Fruit("apple"),
    Fruit("strawberry"),
    Fruit("cherry"),
    Fruit("watermelon"),
    Item("radish"),
    Item("cucumber"),
    Item("meatball"),
    Shovel()
]


def randomize(grid, items=pickups): #pylint: disable=dangerous-default-value
    """Slumpa föremål på kartan."""
    for item in items:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen

def get_random_extra_item():
    """Hämta slumpmässigt föremål. Se till att original=False"""
    random_item = random.choice(
        [
            Item("carrot", original=False, symbol='¿'),
            Fruit("apple", original=False, symbol='¿'),
            Fruit("strawberry", original=False, symbol='¿'),
            Fruit("cherry", original=False, symbol='¿'),
            Fruit("watermelon", original=False, symbol='¿'),
            Item("radish", original=False, symbol='¿'),
            Item("cucumber", original=False, symbol='¿'),
            Item("meatball", original=False, symbol='¿'),
        ]
    )
    return random_item

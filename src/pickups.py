"""Olika typer av föremål att plocka upp."""

class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=10, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol

class Fruit(Item):
    """ Frukt, ett Item med värde 20 poäng. """
    def __init__(self, name, symbol='?'):
        super().__init__(name=name, value=20, symbol=symbol)

class Shovel(Item):
    """ Spade. Inga poäng, kan ta bort en vägg en gång. """
    # TODO: J. Spade - en ny sak man kan plocka upp. När man går in i en vägg nästa gång,\n
    # förbrukas spaden för att ta bort väggen.
    def __init__(self):
        super().__init__(name='shovel', value=0, symbol='🥄')

class Trap(Item):
    """ Fälla. Ska ligga kvar på kartan. """
    # TODO: I. Fällor - introducera valfri fälla till spelplanen. Om man går på en ruta med en\n
    # fälla ska man förlora 10 poäng. Fällan ska ligga kvar så att man kan falla i den flera gånger.
    def __init__(self):
        super().__init__(name='trap', value=-10, symbol='🕳️')

class Chest(Item):
    """ Kista, kräver nyckel för att öppnas. """
    # TODO: K. Nycklar och kistor - slumpa minst en nyckel och lika många kistor på spelplanen.\n
    # När man går på en ruta med en nyckel plockar man upp den i sitt inventory. Om man kommer\n
    # till en kista och har minst en nyckel, öppnar man kistan och plockar upp en skatt som är\n
    # värd 100 poäng. (Nyckeln är förbrukad.)
    def __init__(self):
        super().__init__(name='chest', value=0, symbol='💼')

class Key(Item):
    """ Nyckel, krävs för att öppna kista. """
    # TODO: K. Nycklar och kistor - slumpa minst en nyckel och lika många kistor på spelplanen.\n
    # När man går på en ruta med en nyckel plockar man upp den i sitt inventory.\n
    # Om man kommer till en kista och har minst en nyckel, öppnar man kistan och plockar upp en\n
    # skatt som är värd 100 poäng. (Nyckeln är förbrukad.)
    def __init__(self):
        super().__init__(name='key', value=0, symbol='🗝')

class Treasure(Item):
    """ Skatt. Ligger i skattkista. """
    # TODO: K. Nycklar och kistor - slumpa minst en nyckel och lika många kistor på spelplanen.\n
    # När man går på en ruta med en nyckel plockar man upp den i sitt inventory.\n
    # Om man kommer till en kista och har minst en nyckel, öppnar man kistan och plockar upp en\n
    # skatt som är värd 100 poäng. (Nyckeln är förbrukad.)
    def __init__(self):
        super().__init__(name='treasure', value=100, symbol='👑')

class Exit(Item):
    """ Utgång. Kräver att alla ursprungliga saker är upplockade. """
    # TODO: M. Exit - slumpa ett "E" på kartan. När man har plockat upp alla ursprungliga saker,\n
    # kan man gå till exit för att vinna spelet. Men innan man tagit upp alla har inte Exit någon\n
    # effekt.
    def __init__(self):
        super().__init__(name='exit', value=0, symbol='E')

# DONE: D. Fruktsallad - alla frukter ska vara värda 20 poäng i stället för 10.
pickups = [
    Item("carrot"),
    Fruit("apple"),
    Fruit("strawberry"),
    Fruit("cherry"),
    Fruit("watermelon"),
    Item("radish"),
    Item("cucumber"),
    Item("meatball")
]


def randomize(grid, pickups): #pylint: disable=dangerous-default-value
    """Slumpa föremål på kartan."""
    for item in pickups:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen

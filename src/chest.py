"""Kista som kan finnas på kartan."""

class Chest:
    """ Kista, kräver nyckel för att öppnas. """
    # TODO: K. Nycklar och kistor - slumpa minst en nyckel och lika många kistor på spelplanen.\n
    # När man går på en ruta med en nyckel plockar man upp den i sitt inventory. Om man kommer\n
    # till en kista och har minst en nyckel, öppnar man kistan och plockar upp en skatt som är\n
    # värd 100 poäng. (Nyckeln är förbrukad.)
    def __init__(self):
        super().__init__(name='chest', value=0, symbol='💼')

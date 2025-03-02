"""Fälla som kan finnas på kartan."""

class Trap:
    """ Fälla. Ska ligga kvar på kartan. """
    # TODO: I. Fällor - introducera valfri fälla till spelplanen. Om man går på en ruta med en\n
    # fälla ska man förlora 10 poäng. Fällan ska ligga kvar så att man kan falla i den flera gånger.
    def __init__(self):
        super().__init__(name='trap', value=-10, symbol='🕳️')

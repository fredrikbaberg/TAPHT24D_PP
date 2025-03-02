"""Modul för att hitta punkt nära centrum på grid."""
from .coordinate_helpers import add_coordinates


def get_empty_near_center(grid):
    """Returnerar koordinater för en tom ruta nära centrum.
    Lyfter Exception om ingen av de första 9 rutorna fungerar.
    """
    # Ungefärlig mittpunkt.
    position = [int(grid.width/2), int(grid.height/2)]
    # Ta fram första 9 kombinationerna av startpositioner.
    offsets = []
    for row in [0, 1, -1]:
        for col in [0, 1, -1]:
            offsets.append([row,col])
    for offset in offsets:
        test_position = add_coordinates(position, offset)
        if grid.is_empty(test_position[0], test_position[1]):
            return test_position
    # Hittade inget mer specifikt felmeddelande som passar, så använder Exception.
    raise Exception("Kunde inte hitta en kombination som fungerar.") #pylint: disable=broad-exception-raised

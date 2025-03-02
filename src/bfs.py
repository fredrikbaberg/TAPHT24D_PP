"""Bredd först sökning."""

from src.coordinate_helpers import add_coordinates


def check_no_isolated_rooms(grid):
    """Kolla att det går att nå alla rum.

    Använder bredd-först-sökning."""
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    visited = []
    start = None
    # Hitta en punkt att börja från.
    for col in range(0, grid.width):
        for row in range(0, grid.height):
            if grid.is_empty(col, row):
                start = (row, col)
                break
        if start:
            break
    # Lägg till startpunkten och alla grannar i en kö för att kollas.
    queue = [start]
    while queue:
        to_check = queue.pop() # Hämta en punkt som ska besökas.
        visited.append(to_check)
        for direction in directions: # Försök lägga till grannar.
            new_point = tuple(add_coordinates(to_check, direction))
            # Kontrollera att koordinaten går att nå.
            if 0 <= new_point[0] < grid.width and 0 <= new_point[1] < grid.height:
                if grid.is_empty(new_point[0], new_point[1]) and new_point not in visited:
                    queue.append(new_point)
    # Skapa en lista med alla koordinater som borde ha besökts
    expected = []
    for col in range(0, grid.width):
        for row in range(0, grid.height):
            if grid.is_empty(col, row):
                expected.append((col, row))
    # Ta bort kopior genom att göra om till set och tillbaka till tuple.
    visited = tuple(set(visited))
    expected = tuple(set(expected))
    return expected == visited

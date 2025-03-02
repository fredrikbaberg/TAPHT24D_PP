"""Test av modulen find_empty_near_center."""

import pytest

from src.find_empty_near_center import get_empty_near_center


def test_grid__get_empty_near_center_empty():
    """Spelaren börjar i mittpunkten."""
    grid = FakeGrid(10, 10)
    position = get_empty_near_center(grid)
    assert position == [5, 5]

def test_grid__get_empty_near_center_not_possible_use_ninth():
    """Spelaren kan inte starta i mittpunkten, använd en senare position (9:e)."""
    grid = FakeGrid(10, 10)
    for row in [0,1,-1]:
        for col in [0,1,-1]:
            grid.set(5+row, 5+col, grid.wall)
    grid.set(5-1,5-1,grid.empty) # Vald för att endast sista kombinationen ska fungera.
    position = get_empty_near_center(grid)
    assert position == [4, 4]

def test_grid__get_empty_near_center_not_possible_raises_exception():
    """Exception om ingen position fungerar."""
    grid = FakeGrid(10, 10)
    for row in [0,1,-1]:
        for col in [0,1,-1]:
            grid.set(5+row, 5+col, grid.wall)
    with pytest.raises(Exception):
        get_empty_near_center(grid)


class FakeGrid:
    """Fake av Grid."""
    empty = "."  # Tecken för en tom ruta
    wall = "■"   # Tecken för en ogenomtränglig vägg

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]

    def set(self, x, y, value):
        """Ändra vad som finns på en viss position"""
        self.data[y][x] = value

    def is_empty(self, x, y):
        """Returnerar True om det inte finns något på aktuell ruta"""
        return self.data[y][x] == self.empty

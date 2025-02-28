"""Test av modulen grid"""
import pytest
from src.grid import Grid


def test_grid__get_empty_near_center_empty():
    """Spelaren börjar i mittpunkten."""
    grid = Grid(10, 10)
    position = grid.get_empty_near_center()
    assert position == [5, 5]

def test_grid__get_empty_near_center_not_possible_use_ninth():
    """Spelaren kan inte starta i mittpunkten, använd en senare position (9:e)."""
    grid = Grid(10, 10)
    for row in [0,1,-1]:
        for col in [0,1,-1]:
            grid.set(5+row, 5+col, grid.wall)
    grid.set(5-1,5-1,grid.empty) # Vald för att endast sista kombinationen ska fungera.
    position = grid.get_empty_near_center()
    assert position == [4, 4]

def test_grid__get_empty_near_center_not_possible_raises_exception():
    """Exception om ingen position fungerar."""
    grid = Grid(10, 10)
    for row in [0,1,-1]:
        for col in [0,1,-1]:
            grid.set(5+row, 5+col, grid.wall)
    with pytest.raises(Exception):
        grid.get_empty_near_center()

def test_grid__can_print_when_player_not_set():
    """Se till att Grid kan skrivas ut, tom karta utan spelare.
    Ökar code coverage, då det finns ganska mycket kod i __str__."""
    grid = Grid(5,5)
    grid_as_text = str(grid)
    assert grid_as_text.count(grid.empty) == 25

def test_grid__can_print_player():
    """Se till att om Grid skrivs ut finns spelarens position om den är satt.
    Ökar code coverage, då det finns ganska mycket kod i __str__."""
    grid = Grid(5,5)
    grid.set_player(FakePlayer)
    grid_as_text = str(grid)
    assert grid_as_text.count('@') == 1

def test_grid__make_walls__outer():
    """Kontrollera att yttre väggar skapas."""
    grid = Grid(5, 5)
    grid.make_walls()
    expected = 16
    actual = 0
    # Summera ihop ytterväggar, horizontellt, första och sista raden.
    for col in range(5):
        actual += 0 if grid.get(col, 0) is grid.empty else 1
        actual += 0 if grid.get(col, 4) is grid.empty else 1
    # Summera ihop ytterväggar, vertialt, hoppa över första och sista raden (täcks av föregående).
    for row in range(1,4):
        actual += 0 if grid.get(0, row) is grid.empty else 1
        actual += 0 if grid.get(4, row) is grid.empty else 1
    assert expected == actual

class FakePlayer: #pylint: disable=too-few-public-methods
    """Fake av klassen Player."""
    pos_x = 3
    pos_y = 3

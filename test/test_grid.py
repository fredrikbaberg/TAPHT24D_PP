import pytest
from src.grid import Grid


def test_grid__set_player_center():
    # Spelaren börjar i mittpunkten.
    grid = Grid(10, 10)
    position = grid.get_empty_near_center()
    assert position == [5, 5]

def test_grid__set_player_center_not_possible_use_ninth():
    # Spelaren kan inte starta i mittpunkten, gå igenom listan med kombinationer.
    grid = Grid(10, 10)
    for row in [0,1,-1]:
        for col in [0,1,-1]:
            grid.set(5+row, 5+col, grid.wall)
    grid.set(5-1,5-1,grid.empty)
    position = grid.get_empty_near_center()
    assert position == [4, 4]

def test_grid__set_player_center_not_possible_raises_exception():
    # Spelaren kan inte starta i mittpunkten, ingen kombination fungerar.
    grid = Grid(10, 10)
    for row in [0,1,-1]:
        for col in [0,1,-1]:
            grid.set(5+row, 5+col, grid.wall)
    with pytest.raises(Exception):
        grid.get_empty_near_center()

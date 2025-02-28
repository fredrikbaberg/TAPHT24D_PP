"""Tester för modulen player"""
from src.player import Player

add_coordinates = lambda x, y: [x[0]+y[0], x[1]+y[1]] #pylint: disable=unnecessary-lambda-assignment


def test_player__move_x_positive():
    """Kontrollera att spelaren kan röra sig i positivt y-led"""
    start = [2, 1]
    movement = [1, 0]
    expected = add_coordinates(start, movement)
    player = Player(start[0], start[1])
    player.move(movement[0], movement[1])
    assert [player.pos_x, player.pos_y] == expected

def test_player__move_x_negative():
    """Kontrollera att spelaren kan röra sig i negativt x-led"""
    start = [2, 2]
    movement = [-1, 0]
    expected = add_coordinates(start, movement)
    player = Player(start[0], start[1])
    player.move(movement[0], movement[1])
    assert [player.pos_x, player.pos_y] == expected

def test_player__move_y_positive():
    """Kontrollera att spelaren kan röra sig i positivt y-led"""
    start = [2, 2]
    movement = [0, 1]
    expected = add_coordinates(start, movement)
    player = Player(start[0], start[1])
    player.move(movement[0], movement[1])
    assert [player.pos_x, player.pos_y] == expected

def test_player__move_y_negative():
    """Kontrollera att spelaren kan röra sig i negativt y-led"""
    start = [2, 2]
    movement = [0, -1]
    expected = add_coordinates(start, movement)
    player = Player(start[0], start[1])
    player.move(movement[0], movement[1])
    assert [player.pos_x, player.pos_y] == expected

def test_player__can_move_to_empty():
    """Kontrollera att spelaren kan röra sig till en tom ruta."""
    player = Player(0, 0)
    grid = FakeGrid(1, 1)
    expected = True
    assert player.can_move(0, 0, grid) == expected

def test_player__can_move_to_non_empty():
    """Kontrollera om spelaren kan gå till en icke-tom ruta."""
    player = Player(0, 0)
    grid = FakeGrid(2, 2)
    grid.set(1, 0, grid.wall)
    expected = False
    assert player.can_move(1, 0, grid) == expected

def test_player__move_outside_grid():
    """Testa om spelaren kan röra sig utanför kartan."""
    player = Player(0, 0)
    grid = FakeGrid(1, 1)
    assert player.can_move(1, 0, grid) is False

class FakeItem:
    """Fake av Item"""
    pass #pylint: disable=unnecessary-pass

class FakeGrid:
    """Fake av Grid"""
    empty = '.'
    wall = "■"
    item = FakeItem()

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]

    def is_empty(self, x, y):
        """Kontrollera om en koordinat är tom."""
        if self.data[y][x] == self.empty:
            return True
        return False

    def set(self, x, y, value):
        """Sätt värde för koordinat"""
        self.data[y][x] = value

    def get(self, x, y):
        """Hämta koordinat"""
        return self.data[y][x]

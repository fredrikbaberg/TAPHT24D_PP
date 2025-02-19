from src.player import Player

add_coordinates = lambda x, y: [x[0]+y[0], x[1]+y[1]]


def test_player__move_x_positive():
    start = [2, 1]
    movement = [1, 0]
    expected = add_coordinates(start, movement)
    player = Player(start[0], start[1])
    player.move(movement[0], movement[1])
    assert [player.pos_x, player.pos_y] == expected

def test_player__move_x_negative():
    start = [2, 2]
    movement = [-1, 0]
    expected = add_coordinates(start, movement)
    player = Player(start[0], start[1])
    player.move(movement[0], movement[1])
    assert [player.pos_x, player.pos_y] == expected

def test_player__move_y_positive():
    start = [2, 2]
    movement = [0, 1]
    expected = add_coordinates(start, movement)
    player = Player(start[0], start[1])
    player.move(movement[0], movement[1])
    assert [player.pos_x, player.pos_y] == expected

def test_player__move_y_negative():
    start = [2, 2]
    movement = [0, -1]
    expected = add_coordinates(start, movement)
    player = Player(start[0], start[1])
    player.move(movement[0], movement[1])
    assert [player.pos_x, player.pos_y] == expected

def test_player__can_move_to_empty():
    player = Player(0, 0)
    grid = FakeGrid(1, 1)
    expected = True
    assert player.can_move(0, 0, grid) == expected

def test_player__can_move_to_non_empty():
    player = Player(0, 0)
    grid = FakeGrid(2, 2)
    grid.set(1, 0, grid.wall)
    expected = False
    assert player.can_move(1, 0, grid) == expected

def test_player__move_outside_grid():
    player = Player(0, 0)
    grid = FakeGrid(1, 1)
    assert player.can_move(1, 0, grid) == False

class FakeItem:
    pass

class FakeGrid:
    empty = '.'
    wall = "■"
    item = FakeItem()

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]

    def is_empty(self, x, y):
        if self.data[y][x] == self.empty:
            return True
        return False

    def set(self, x, y, value):
        self.data[y][x] = value

    def get(self, x, y):
        return self.data[y][x]

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
    player = Player(1, 1)
    grid = FakeGrid()
    expected = True
    assert player.can_move(0, 0, grid) == expected

def test_player__can_move_to_non_empty():
    player = Player(1, 1)
    grid = FakeGrid()
    expected = False
    assert player.can_move(1, 0, grid) == expected

class FakeGrid:
    def is_empty(self, x, y):
        """ During testing of Player, returns False if x is odd. """
        if x%2==0:
            return True
        return False

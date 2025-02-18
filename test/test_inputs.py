from src.inputs import move


class FakePlayer:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move(self, dx, dy):
        self.pos_x += dx
        self.pos_y += dy

class FakeGrid:
    def get(self, x, y):
        pass

def test_move_left():
    move_x = -1
    move_y = 0
    grid = FakeGrid()
    player = FakePlayer(0, 0)
    expected_x = player.pos_x + move_x
    expected_y = player.pos_y + move_y
    move(move_x, move_y, grid, player)
    actual_x = player.pos_x
    actual_y = player.pos_y
    assert actual_x == expected_x
    assert actual_y == expected_y

def test_move_right():
    pass

def test_move_up():
    pass

def test_move_down():
    pass


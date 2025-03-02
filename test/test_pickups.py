"""Test för modulen pickups."""
from src.pickups import Fruit, randomize, Item, count_pickups


def test_pickups__randomize_adds_item():
    """Se till att Items kan läggas till med randomize-funktionen."""
    grid = FakeGrid()
    pickups = [
        Item('Test'),
        Fruit('Test'),
        Item('Test'),
        Fruit("Test"),
        Item('Test 2')
    ]
    randomize(grid, pickups)
    number_of_items = 0
    for row in range(0, len(grid.data)):
        for col in range(0, len(grid.data[0])):
            if isinstance(grid.data[col][row], Item):
                number_of_items+=1
    print(f"{grid.data}")
    assert number_of_items == len(pickups)

def test_pickups__count_items_empty_grid():
    """Räkna antal Item på en tom karta."""
    expected = 0
    grid = FakeGrid()
    actual = count_pickups(grid, Item)
    assert actual == expected

def test_pickups__count_items_full_grid():
    """Räkna antal Item på en fylld karta."""
    expected = 25
    grid = FakeGrid()
    for i in range(0, grid.width):
        for j in range(0, grid.height):
            grid.set(i, j, Item(''))
    actual = count_pickups(grid, Item)
    assert actual == expected

class FakeGrid:
    """Fake av Grid"""
    def __init__(self, width=5, height=5):
        self.empty = '.'
        self.width = width
        self.height = height
        self.data = [[self.empty for y in range(self.width)] for z in range(
            self.height)]
        self.selected_x = 0
        self.selected_y = 0

    def get_random_x(self):
        """"Slumpa" en position genom att gå från höger till vänster."""
        random_x = len(self.data[1]) - self.selected_x - 1
        self.selected_x += 1
        return random_x

    def get_random_y(self):
        """"Slumpa" en position genom att gå från höger till vänster."""
        random_y = len(self.data[0]) - self.selected_y - 1
        self.selected_y += 1
        return random_y

    def is_empty(self, x, y):
        """Kontrollera om koordinaten är tom."""
        if self.data[y][x] != self.empty:
            return False
        return True

    def set(self, x, y, item):
        """Sätt ett värde för koordinaten."""
        self.data[y][x] = item

    def get(self, x, y):
        """Hämta värde för en viss koordinat."""
        return self.data[y][x]

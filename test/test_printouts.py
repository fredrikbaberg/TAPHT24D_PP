from src.printouts import print_inventory, print_status

class FakeGrid:
    pass

def test__print_status__callable():
    # Kontrollera att det går att anropa print_status.
    fake_grid = FakeGrid()
    print_status(fake_grid, 0)

def test__print_inventory__calable():
    # Kontrollera att det går att skriva ut inventory.
    inventory = []
    print_inventory(inventory)

"""Utskrifter av spelplan, inventory."""

def print_status(game_grid, score):
    """Visa spelvärlden och antal poäng."""
    print("--------------------------------------")
    print(f"You have {score} points.")
    print(game_grid)

def print_inventory(inventory):
    """Skriv ut inventory."""
    print("--------------------------------------")
    items = [i.name for i in inventory]
    print(f"Your inventory contains: {", ".join(items)}")

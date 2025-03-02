"""Hjälpfunktioner för koordinater."""

def add_coordinates(x, y):
    """Summera två listor elementvis."""
    if len(x) != len(y):
        raise IndexError("Listorna har olika längd.")
    # Använder map och lambda.
    new_list = list(map(lambda list1, list2: list1+list2, x, y))
    return new_list

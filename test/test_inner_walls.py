"""Enhetstester för att skapa inre väggar."""

from src.inner_walls import get_coordinates_for_randomized_wall


def test_inner_walls__empty_map_zero_length():
    """Returnerar en tom lista om inga väggar ska skapas."""
    expected = []
    actual = get_coordinates_for_randomized_wall(36, 12, 0)
    assert actual == expected

def test_inner_walls__returns_multiple_walls():
    """Returnerar flera koordinater när längden är större än noll."""
    expected = 10
    actual = len(get_coordinates_for_randomized_wall(36, 12, 10))
    assert actual == expected

def test_inner_walls__walls_within_limits__single_empty():
    """Minskar antalet väggar om det inte får plats på kartan."""
    expected = [[1,1]]
    walls = get_coordinates_for_randomized_wall(3, 3, 10)
    # Ta bort kopior från listan
    pruned_walls = list(set([tuple(x) for x in walls]))
    actual = [list(x) for x in pruned_walls]
    assert actual == expected

def test_inner_walls__walls_within_limits__single_corridor():
    """Minskar antalet väggar om det inte får plats på kartan."""
    expected = 8
    walls = get_coordinates_for_randomized_wall(10, 3, 15)
    # Ta bort kopior från listan
    pruned_walls = list(set([tuple(x) for x in walls]))
    actual = len([list(x) for x in pruned_walls])
    assert actual == expected

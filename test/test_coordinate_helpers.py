"""Enhetstester för coordinate_helpers."""
import pytest

from src.coordinate_helpers import add_coordinates

def test_coordinate_helpers__add_coordinates_unequal_length_fails():
    """Vid två olika långa listor kommer exception."""
    with pytest.raises(Exception):
        add_coordinates([1], [2, 3])

def test_coordinate_helpers__add_coordinates_equal_length_succeeds():
    """Vid två lika långa listor returneras summan av de två listorna."""
    expected = [4, 6, 7]
    actual = add_coordinates([1,2,5], [3,4,2])
    assert expected == actual

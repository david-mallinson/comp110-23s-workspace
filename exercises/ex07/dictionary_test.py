"""Dictionary Test."""


__author__ = "730572335"


from typing import ByteString
from dictionary import invert, favorite_color, count


def test_invert_1() -> None:
    """Test."""
    with ByteString.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_case_invert_1() -> None:
    """Test."""
    colors: dict[str, str] = {'purple': 'gold', 'blue': 'red'}
    assert invert(colors) == {'gold': 'purple', 'red': 'blue'}


def test_case_invert_2() -> None:
    """Tests if invert works with 4 values."""
    colors: dict[str, str] = {'purple': 'gold', 'blue': 'red', 'orange': 'green', 'pink': 'white'}
    assert invert(colors) == {'gold': 'purple', 'red': 'blue', 'green': 'orange', 'white': 'pink'}


def test_edge_fav_color() -> None:
    """Tests the return when there is a reoccuring color value."""
    colors: dict[str, str] = {"David": "Green", "Davis": "Green", "Jackson": "Blue"}
    assert favorite_color(colors) == "Green"


def test_case_fav_color_1() -> None:
    """Tests the return when 4 colors are inputted and there is a reoccuring color value."""
    colors: dict[str, str] = {"David": "Green", "Davis": "Green", "Jackson": "Blue", "Jack": "Pink"}
    assert favorite_color(colors) == "Green"


def test_case_fav_color_2() -> None:
    """Tests what happens when 6 colors are inputted."""
    colors: dict[str, str] = {"David": "Green", "Davis": "Green", "Jackson": "Blue", "Jack": "Pink", "Daniel": "White", "Raymond": "Blue"}
    assert favorite_color(colors) == "Blue"


def test_count() -> None:
    """Tests what happens to an edge case by using the count function."""
    color: list[str] = []
    assert count(color) == {}
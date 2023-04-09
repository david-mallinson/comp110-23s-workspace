"""File used to test three different functions."""


___author___ = "730572335"


from utils import only_evens, sub, concat


def test_evens() -> None:
    """This will test if the function works properly with a single negative even number."""
    xs: list[int] = [-6]
    assert only_evens(xs) == [-6]


def test_evens_2() -> None:
    """This tests if the function works with multible types of numbers, positive, negative, odd and even."""
    xs: list[int] = [-12, 5, 8, 14]
    assert only_evens(xs) == [-12, 8, 14]


def test_combine() -> None:
    """This tests if the function will properly concat an empty list."""
    xs_a: list[int] = [5, 6, 7]
    xs_b: list[int] = []
    assert concat[xs_a, xs_b] == [5, 6, 7]


def test_combine_2() -> None:
    """This function tests if the function concats two lists of equal lengths."""
    xs_a: list[int] = [7, 9]
    xs_b: list[int] = [34, -4]
    assert concat(xs_a, xs_b) == [7, 9, 34, -4]


def test_combine_3() -> None:
    """This fucntion tests if the function properly concats two lists of different lengths."""
    xs_a: list[int] = [10, -120, 7]
    xs_b: list[int] = [5, 404]
    assert concat(xs_a, xs_b) == [10, -120, 7, 5, 404]


def test_sub() -> None:
    """This function tests if the function will properly evaluate and return an empty list."""
    xs: list[int] = []
    assert sub(xs, 0, 10) == []


def test_sub_2() -> None:
    """This function tests if the function performs correctly with a negative starting index."""
    xs: list[int] = [2, 3, 4, 5, 6]
    assert sub(xs, -5, 4) == [2, 3, 4, 5]


def test_sub_3() -> None:
    """This function tests if the function performs correctly with an ending index thats greater than the lists length."""
    xs: list[int] = [3, 4, 5, 6, 7, 8]
    assert sub(xs, 2, 20) == [5, 6, 7, 8]
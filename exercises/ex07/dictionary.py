"""EX07, Dictionary Functions."""

__author__ = "730572335"


def invert(original: dict[str, str]) -> dict[str, str]:
    """Reverses the input and returns a list."""
    reverse: dict[str, str] = {}
    for i in original:
        if original[i] not in reverse:
            reverse[original[i]] = i
        else:
            raise KeyError("There are duplicate values in the user's dictionary.")
    return reverse


def favorite_color(color: dict[str, str]) -> str:
    """Retunrs the most frequent color imputted by the user."""
    output: dict[str, int] = {}
    for i in color:
        if color[i] in output:
            output[color[i]] += 1
        else:
            output[color[i]] = 1
    r_color: str = ""
    counter: int = 0
    for i in output:
        if counter < output[i]:
            counter = output[i]
            r_color = i
    return r_color


def count(counter: list[str]) -> dict[str, int]:
    """Return a dict that keeps track of how many times a value shows up in the inputted dict."""
    output: dict[str, int] = {}
    for i in counter:
        if i in output:
            output[i] += 1
        else:
            output[i] = 1
    return output
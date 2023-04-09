def all(list_1: list[int], number: int) -> bool:
    """Returns true if all values in a list are the same."""
    elem: int = 0
    correct: bool = True
    if len(list_1) == 0:
        return False
    while elem < len(list_1) and correct is True:
        if number == list_1[elem]:
            correct = True
            elem += 1
        else:
            return False
    return True


def max(list_3: list[int]) -> int:
    """Returns the max value of a list."""
    if len(list_3) == 0:
        raise ValueError("max () arg is an empty list")
    n: int = 1
    number: int = list_3[0]
    while n < len(list_3):
        if number > list_3[n]:
            n += 1
        elif number < list_3[n]:
            number = list_3[n]
            n += 1
        else:
            n += 1
    return number


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Returns true if every element of the lists are equal to their corresponding indices."""
    elem: int = 0
    equal: bool = True
    if len(list_1) != len(list_2):
        return False
    while equal is True and (elem < len(list_1) or elem < (list_2)):
        if list_1[elem] == list_2[elem]:
            equal = True
            elem += 1
        else:
            equal = False
    return equal
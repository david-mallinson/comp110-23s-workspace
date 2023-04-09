"""Three functions designed to preform different opperations on lists."""


___author___ = "730572335"


def only_evens(list_1: list[int]) -> list[int]:
    """This function creates and returns another list containing even numbers from the first list."""
    final_list: list[int] = []
    i: int = 0
    while i < len(list_1):
        if list_1[i] % 2 == 0:
            final_list.append(list_1[i])
            i += 1
        else:
            i += 1
    return final_list


def concat(list_1: list[int], list_2: list[int]) -> list[int]:
    """This function returns the first list and the second list appended."""
    final_list: list[int] = []
    for items in (list_1):
        final_list.append(items)
    for items in (list_2):
        final_list.append(items)
    return final_list


def sub(list_1: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns a part of a list based around the user's inputs for the beginning and ending inputs."""
    sub_list: list[int] = []
    if len(list_1) == 0:
        return sub_list
    if start_index > len(list_1) or end_index <= 0:
        return list_1
    if start_index < 0:
        start_index = 0
    if end_index > len(list_1):
        end_index = list_1[len(list_1) - 1]
    i: int = start_index
    while i < (end_index) and i < (len(list_1)):
        sub_list.append(list_1[i])
        i += 1
    return sub_list
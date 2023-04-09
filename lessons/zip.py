"""Challenge question 04"""



def zip(list_1: list[str], list_2: list[int]) -> dict[str, int]:
    """Returns dictonary."""

    zip_dict: dict[str, int] = {}
    i: int = 0

    if len(list_1) < len(list_2):
        return {}
    
    if len(list_2) < len(list_1):
        return {}

    if len(list_1) == 0 or len(list_2) == 0:
        return {}

    for item in list_1:
        zip_dict[item] = list_2[i]
        i += 1

    return zip_dict
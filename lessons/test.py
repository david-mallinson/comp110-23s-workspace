def concat(dict_1: dict[str, list[str]], dict_2: dict[str. list[str]]) -> dict[str, list[str]]:
    """Concatenates 2 dictionaries into one new dictionary."""
    result: dict[str, list[str]] = dict()
    for column in dict_1:
        result[column] = dict_1[column]
    for column in dict_2:
        if column in result:
            result[column] += dict_2[column]
        else:
            result[column] = dict_2[column]
    return result

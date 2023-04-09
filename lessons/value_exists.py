def value_exists(dictionary, integer):
    """
    Given a dictionary and an integer, returns True if the integer is a value in the dictionary,
    and False otherwise.
    """
    for value in dictionary.values():
        if value == integer:
            return True
    return False

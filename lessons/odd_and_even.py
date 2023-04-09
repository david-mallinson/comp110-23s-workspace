def odd_and_even(lst: list[int]) -> list[int]:
    """
    Returns a new list containing the odd elements with even index from the input list.
    
    Args:
    lst -- a list of integers
    
    Returns:
    a new list of integers
    """
    new_lst = []
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            new_lst.append(lst[i])
    return new_lst

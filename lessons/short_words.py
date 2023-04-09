def short_words(words: list[str]) -> list[str]:
    """
    Returns a list of words that are shorter than 5 characters.
    
    Args:
        words (list[str]): A list of words to filter.
    
    Returns:
        list[str]: A new list of words that are shorter than 5 characters.
    """
    short_list = []
    for word in words:
        if len(word) < 5:
            short_list.append(word)
        else:
            print(f"{word} is too long")
    return short_list.copy()

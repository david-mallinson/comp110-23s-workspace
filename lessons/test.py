def mimic_letter(my_words: str, letter_index: int) -> str:
"""Outputs the charcter of my_words at index letter_idx"""

    if len(my_words) <= letter_index:
        return("Too high of an index")

    if len(my_words) > letter_index:
        return my_words[letter_index]



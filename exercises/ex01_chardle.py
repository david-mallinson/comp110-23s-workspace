"""EX01 - Chardle - A cute step toward Wordle"""

__author__ = "730572335"

wordle_word: str = input("Enter a 5-character word: ")
if len(wordle_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
input_letter: str = input("Enter a single character: ")
letter_counter: int = 0

if len(input_letter) != 1:
    print("Error: Character must be a single character.")
    exit()

if len(wordle_word) == 5:
    print("Searching for " + input_letter + " in " + wordle_word)
    if input_letter == wordle_word[0]:
        print(input_letter + " found at index 0")
        letter_counter = letter_counter + 1
    if input_letter == wordle_word[1]:
        print(input_letter + " found at index 1")
        letter_counter = letter_counter + 1
    if input_letter == wordle_word[2]:
        print(input_letter + " found at index 2")
        letter_counter = letter_counter + 1
    if input_letter == wordle_word[3]:
        print(input_letter + " found at index 3")
        letter_counter = letter_counter + 1
    if input_letter == wordle_word[4]:
        print(input_letter + " found at index 4")
        letter_counter = letter_counter + 1
    if letter_counter == 0:
        print("No instances of " + input_letter + " found in " + wordle_word)
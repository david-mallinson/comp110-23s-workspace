"""EX02 - One-Shot Wordle - Another step toward Wordle."""

__author__ = "730572335"

GREEN: str = ("\U0001F7E9")
YELLOW: str = ("\U0001F7E8")
WHITE: str = ("\U00002B1C")

word: str = "python"
wordle_word: str = input("What is your 6-letter guess? ")
letter_counter: int = 0
result_string: str = ""
x: int = 0
s: int = 0
match: bool = False


while len(wordle_word) != 6:
    wordle_word = input("That was not 6 letters! Try again: ")

while x < len(word):
    if wordle_word[x] == word[x]:
        result_string = result_string + GREEN
        x = x + 1
    else:
        while s < len(word) and match is not True:
            if wordle_word[x] == word[s]:
                match = True
            else:
                s = s + 1
        if match == True:
            result_string = result_string + YELLOW
            x = x + 1
            match = False
            s = 0
        else:
            result_string = result_string + WHITE
            x = x + 1
            match = False
            s = 0

if wordle_word == word:
    print((result_string) + "\nWoo! You got it!")
else:
    print((result_string) + "\nNot quite. Play again soon!")
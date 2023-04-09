"""EX03 - Wordle"""
__author__ = "730572335"
GREEN: str = ("\U0001F7E9")
YELLOW: str = ("\U0001F7E8")
WHITE: str = ("\U00002B1C")

def contains_char (search: str, single_char: str) -> bool:
    """Sorts through each letter of the string and returns True or False"""
    assert len(single_char) == 1
    counter: int = 0
    while counter < len(search):
        if search[counter] == single_char:
            return True
        else:
            counter = counter + 1
    return False


def  main () -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    secret_word_length: int = len(secret_word)
    counter: int = 1
    correct: bool = False
    print(f"=== Turn {counter}/6 ===")
    while counter < 7 and correct is False:
        guess = input_guess(secret_word_length)
        print(emojified(guess, secret_word))
        if guess == secret_word:
            correct = True
        else:
            counter = counter + 1
            print(f"=== Turn {counter}/6 ===")
    if correct is True:
        print(f"You won in {counter}/6 turns!")
    else:
        print("X/6 - You lost, try again tomorrow.")


def emojified (wordle_word: str, input_guess: str) -> str:
    """Compares values between secret word and guess, printing out blocks"""
    assert len(input_guess) == len(wordle_word)
    counter: int = 0
    
    result_str: str = ""

    while counter < len(wordle_word):
        if input_guess[counter] == wordle_word[counter]:
            result_str = result_str + GREEN
            counter = counter + 1
        elif contains_char(wordle_word, input_guess[counter]) is True:
            result_str = result_str + YELLOW
            counter = counter + 1
        else:
            result_str = result_str + WHITE
            counter = counter + 1
    return result_str



def input_guess (guess_length: int) -> str:
    """Check the length of the users input and check if their guess is of equal length."""
    equal_length: bool = False
    input_guess: str = input(f"Enter a {guess_length} letter word: ")
    while equal_length is False:
        if guess_length == len(input_guess):
            equal_length = True
        else:
            input_guess = input(f"Your guess was not {guess_length} characters. Try again: ")
        return input_guess


if __name__ == "__main__":
    main()
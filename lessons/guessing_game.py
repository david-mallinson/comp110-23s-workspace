"""ask for a number, goes until they get it right"""

SECRET: int = 4

"""constant variables should be in ALL CAPS to signify they will never change, lower case variables change"""

guess: int = int(input("Guess a number!!!"))
playing: bool = True
number_of_guessess: int = 1

while playing:
    if number_of_guesses == 3:
        playing = False
    if guess == SECRET:
        print("Yay! You got it right!!!!!! Believe in ur dreams.")
        playing = False
    else:
        print("wrong number :(")
        if guess % 2 == 1: #guess is odd
            print("Your guess is odd, dumbass. The answer is even. ")
        if guess > SECRET:
                print("Your guess is too high!! ")
        else: #guess < secret
            print("Your guess is too low!!!")
        guess = int(input("Make another guess!!!!! "))
    number_of_guessess = number_of_guessess+ 1
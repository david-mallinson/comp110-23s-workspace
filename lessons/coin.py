import random

def coinflip_game():
    print("Welcome to the coinflip guessing game!")
    print("Guess heads or tails and see how many you can guess in a row correctly.")
    
    num_correct_guesses = 0
    while True:
        # Generate a random coin flip (0 is heads, 1 is tails)
        coinflip = random.randint(0, 1)
        
        # Ask the user to guess heads or tails
        user_guess = input("Guess heads or tails: ")
        
        # Check if the user's guess matches the coin flip
        if user_guess.lower() == "heads" and coinflip == 0:
            print("You guessed correctly!")
            num_correct_guesses += 1
        elif user_guess.lower() == "tails" and coinflip == 1:
            print("You guessed correctly!")
            num_correct_guesses += 1
        else:
            print("Sorry, you guessed wrong. Game over!")
            break
            
    print(f"You guessed {num_correct_guesses} in a row correctly.")



"""To play the game, simply call the coinflip_game() function:"""

coinflip_game()

"""The game will continue until the user 
makes an incorrect guess and then display 
the number of consecutive correct guesses 
the user had."""
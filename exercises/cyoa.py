"""Code Your Own Adventure! Coin Flipping Game."""


___author___ = "730572335"


import random


points: int = 0
player: str = ""
lives: int = 1
dawg: str = "\U0001F436"
xd_face: str = "\U0001F61D"
cowboy_emoj: str = "\U0001F920"
smiley_emoj: str = "\U0001F603"
money_emoj: str = "\U0001F911"
laughing_emoj: str = "\U0001F923"


def greet() -> None:
    """Sends a welcome message to the player."""
    global player
    player = input("What is your player name?\n")
    print(f"Welcome to the coin flipping guessing game {player}! Guess heads or tails and see how many you can guess in a row!")
  

def main() -> None:
    """Allows the user to choose what to play, then runs the procedure or function selected."""
    global points
    global lives
    greet()
    
    mode: str = input("Do you want to play on easy or hard mode? Easy mode gives you an additional life. Input 1 for easy and 2 for hard: ")
    if mode == "1":
        lives += 1

    user_first = input("Do you want to:\n1. Play the game\n2. Exit the game\n3. Have the computer play against itself? \nRespond by typing 1, 2 or 3: \n") 
    if user_first == "1":
        solo_play()
        print(". . .\n. . .\nYOUR HIGH SCORE WAS : ")
    if user_first == "2":
        print("Aw ok, hope you'll play next time!")
        quit()
    else:
        comp_play()


def solo_play(score: int = 0) -> int:
    """Flips a coin and prompts the user for a guess."""
    global points
    global lives
    while True:
        # Generate a random coin flip (0 is heads, 1 is tails)
        flip = random.randint(0, 1)
        
        # Ask the user to guess heads or tails
        guess = input(cowboy_emoj + "Guess heads or tails: ")
        
        # Check if the user's guess matches the coin flip
        if guess.lower() == "heads" and flip == 0:
            print("You guessed correctly!" + smiley_emoj)
            points += 1
            score += 1
            print(f"Dawg... {xd_face} {dawg} you... just... GAINED A PLAYER POINT!")
        elif guess.lower() == "tails" and flip == 1:
            print("You guessed correctly!" + smiley_emoj)
            points += 1
            score += 1
            print(f"Dawg... {xd_face} {dawg} you... just... GAINED A PLAYER POINT!")
        else:
            print("Sorry " + player + ", you guessed wrong... no player point for you... ")
            lives -= 1
            if lives == 0:
                print(f"You reached 0 lives! Game over! {laughing_emoj}")
                print(f"You guessed {points} in a row correctly!" + money_emoj)
                play_again: str = input("Do you want to play again? Press 1 for yes and 2 for no: ")
                if play_again == "1":
                    main()
                else:
                    quit()
            print(f"You just lost a life {player}...\nLives remaining: 1")


def comp_play() -> None:
    """Has the computer flip a coin and the computer randomly generates guesses, interacting with itself."""
    global points
    global lives
    global player
    while True:
        # Generate a random coin flip (0 is heads, 1 is tails)
        flip = random.randint(0, 1)
        
        # Ask the user to guess heads or tails
        guess = random.randint(0, 1)

        if guess == 0:
            print("The computers guess was: Heads!\n")

        if guess == 1:
            print("The computers guess was: Tails!\n")
        
        # Check if the user's guess matches the coin flip
        if guess == 0 and flip == 0:
            print("You guessed correctly!" + smiley_emoj)
            points += 1
            print(f"Dawg... {xd_face} {dawg} you... just... GAINED A PLAYER POINT!")
        elif guess == 1 and flip == 1:
            print("You guessed correctly!" + smiley_emoj)
            points += 1
            print(f"Dawg... {xd_face} {dawg} you... just... GAINED A PLAYER POINT!")
        else:
            print("Sorry " + player + ", you guessed wrong... no player point for you... ")
            lives -= 1
            if lives == 0:
                print(f"You reached 0 lives! Game over! {laughing_emoj}")
                print(f"You guessed {points} in a row correctly!" + money_emoj)
                quit()
            print(f"You just lost a life {player}...\nLives remaning: 1")


def end_screen(detr: int = 0) -> int:
    """Prints end screen"""
    print("Game over...")
            

if __name__ == "__main__":
    main()
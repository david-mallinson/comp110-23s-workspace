import random

# Define the list of possible words to guess
word_list = ["apple", "banana", "cherry", "donut", "elephant", "fossil", "guitar", "hamster", "island", "jacket"]

# Choose a random word from the list
word = random.choice(word_list)

# Define the maximum number of attempts
max_attempts = 6

# Create a set to track the guessed letters
guessed_letters = set()

# Create a set to track the correct letters
correct_letters = set(word)

# Define a function to display the current state of the game
def display_game_state():
    # Display the word with the correct letters filled in
    for letter in word:
        if letter in correct_letters:
            print(letter, end="")
        else:
            print("_", end="")
    print()
    
    # Display the list of guessed letters
    print("Guessed letters:", " ".join(sorted(guessed_letters)))
    
    # Display the remaining number of attempts
    print("Attempts remaining:", max_attempts - len(guessed_letters))
    
    # Display a separator
    print("-" * 20)

# Start the game loop
while True:
    # Display the current state of the game
    display_game_state()
    
    # Check if the player has won
    if correct_letters.issubset(guessed_letters):
        print("Congratulations, you won!")
        break
    
    # Check if the player has run out of attempts
    if len(guessed_letters) >= max_attempts:
        print("Sorry, you lost. The word was", word)
        break
    
    # Prompt the player to guess a letter
    guess = input("Guess a letter: ")
    
    # Check if the guess is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input, please enter a single letter.")
        continue
    
    # Check if the guess has already been made
    if guess in guessed_letters:
        print("You already guessed that letter, try again.")
        continue
    
    # Add the guess to the guessed letters set
    guessed_letters.add(guess)
    
    # Check if the guess is correct
    if guess in correct_letters:
        print("Correct!")
    else:
        print("Incorrect.")

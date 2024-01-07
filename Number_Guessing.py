# Welcome to Number Guessing Game
from random import randint  # Importing the randint function from the random module
from art import art  # Importing ASCII art from a module called art

EASY_LEVEL_TURNS = 10  # Constant for the number of turns in easy mode
HARD_LEVEL_TURNS = 5  # Constant for the number of turns in hard mode

# Function to check the player's guess against the actual number
def check_answer(guess, number, turns):
    """Checks the guess against the number. Returns the number of turns remaining."""
    if guess > number:
        print("Too high")
        return turns - 1
    elif guess < number:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The correct answer was {number}.")

# Function to set the game difficulty level
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Main game function
def game():
    print(art)  # Print ASCII art for a nice visual welcome
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 to 100.")
    
    number = randint(1, 100)  # Generate a random number between 1 and 100
    print(f"The correct answer is {number}.")

    turns = set_difficulty()  # Set the game difficulty
    
    guess = 0
    while guess != number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Guess a number: "))
        turns = check_answer(guess, number, turns)  # Check the guess and update the turns
        
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != number:
            print("Guess again!")

# Call the main game function
game()

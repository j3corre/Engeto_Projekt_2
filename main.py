"""
main.py: Druhý projekt do Engeto Online Python Akademie

author: Jan Bláha
email: jan.blaha@bcas.cz
"""

import random

DIGIT_COUNT = 4         # Length of number to guess.
DIVIDER = "-" * 47      # The divider line in listing.

def make_game() -> list:
    """
    Prepares four digits to guess.
    """
    choices = set(range(1,10))  # The first digit can't be 0.

    game = list()

    for index in range(DIGIT_COUNT):
        chosen_digit = random.choice(list(choices))
        choices.discard(chosen_digit) # Digits can't repeat, therefore discard already chosen ones.
        game.append(str(chosen_digit))
        
        if index == 0:          # Add digit 0 to choices for the next 3 digits.
            choices.add(0)

    return game

def welcome_user():
    """
    Prints welcome message on the beginning of the game.
    """
    print(f"Hi there!")
    print(DIVIDER)
    print(f"I've generated a random {DIGIT_COUNT} digit number for you.")
    print(f"Let's play a bulls and cows game.")
    print(DIVIDER)
    print(f"Enter a number:")
    print(DIVIDER)

def get_guess() -> str:
    """
    Returns valid game guess only. Helps user to know what was wrong on his input.
    """
    correct_guess = False

    while not(correct_guess):
        guess = input(">>>> ")
        if len(guess) != DIGIT_COUNT:     # Guess has not allowed length.
            print(f"Your guess has to be exactly {DIGIT_COUNT} digits long. Try it again.")
            print(DIVIDER)
        elif guess[0] == "0":   # Guess starts with degit 0.
            print(f"Your guess can't start with digit 0. Try it again.")
            print(DIVIDER)
        elif len([digit for digit in guess if digit.isdecimal()]) < DIGIT_COUNT:  # Guess has non digit characters.
            print(f"Your guess has to have digit characters only. Try it again.")
            print(DIVIDER)
        elif len(set(guess)) < DIGIT_COUNT:   # Check for all digits different.
            print(f"You guess contains some digit multiple times, that is not allowed. Try it again.")
            print(DIVIDER)
        else: 
            correct_guess = True    # We get correct guess, return it.
                
    return guess

def main():
    bulls, guesses = 0, 0
    game = make_game()

    welcome_user()
#    print(game)    # Uncomment for debug purposes.

    while bulls < DIGIT_COUNT:    # Play until user finds DIGIT_COUNT bulls (all digits on its positions).
        bulls, cows = 0, 0
        guess = get_guess()
        
        for index in range(DIGIT_COUNT):
            if game[index] == guess[index]:
                bulls += 1
            elif guess[index] in game:
                cows += 1

        print(f"{guess}: bulls: {bulls}, cows: {cows}")
        print(DIVIDER)
                
        guesses += 1

    print(f"Correct, you've guessed the right number")
    print(f"in {guesses} guesses!")
    print(DIVIDER)
    print(f"That's amazing!")

main()
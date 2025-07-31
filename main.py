"""
main.py: Druhý projekt do Engeto Online Python Akademie

author: Jan Bláha
email: jan.blaha@bcas.cz
"""

import random

def make_game() -> list:
    """
    Prepares four digits to guess.
    """
    choices = set(range(1,10))  # The first digit can't be 0.

    game = list()

    for index in range(4):
        vytahl = random.choice(list(choices))
        choices.discard(vytahl) # Digits can't repeat, therefore discard already chosen ones.
        game.append(str(vytahl))
        
        if index == 0:          # Add digit 0 to chices for the next 3 digits.
            choices.add(0)

    return(game)

def welcome_user():
    """
    Prints welcome message on the beginning of the game.
    """
    print(f"Hi there!")
    print(f"-----------------------------------------------")
    print(f"I've generated a random 4 digit number for you.")
    print(f"Let's play a bulls and cows game.")
    print(f"-----------------------------------------------")
    print(f"Enter a number:")
    print(f"-----------------------------------------------")

def get_guess() -> str:
    """
    Returns valid game guess only. Helps user to know what was wrong on his input.
    """
    correct_guess = False

    while not(correct_guess):
        guess = input(">>>> ")
        if len(guess) != 4:     # Guess has not allowed length.
            print(f"Your guess has to be exactly 4 digits long. Try it again.")
            print(f"-----------------------------------------------")
        elif guess[0] == "0":   # Guess starts with degit 0.
            print(f"Your guess can't start with digit 0. Try it again.")
            print(f"-----------------------------------------------")
        elif len([digit for digit in guess if digit.isdecimal()]) < 4:  # Guess has non digit characters.
            print(f"Your guess has to have digit characters only. Try it again.")
            print(f"-----------------------------------------------")
        else:   # Check for all digits different.
            digits = dict()
            for char in guess:
                if char in digits.keys():
                    digits[char] += 1
                else:
                    digits[char] = 1
            if len(digits) == 4:
                correct_guess = True    # We get correct guess, return it.
            else:
                print(f"You guess contains some digit multiple times, that is not allowed. Try it again.")
                print(f"-----------------------------------------------")
    return guess

def main():
    bulls, guesses = 0, 0
    game = make_game()

    welcome_user()
#    print(game)    # Uncomment out for debug purposes.

    while bulls < 4:    # Play until user finds 4 bulls (all digits on its positions).
        bulls, cows = 0, 0
        guess = get_guess()
        
        for index in range(4):
            if game[index] == guess[index]:
                bulls += 1
            elif set(guess[index]) <= set(game):
                cows += 1

        print(f"{guess}: bulls: {bulls}, cows: {cows}")
        print(f"-----------------------------------------------")
                
        guesses += 1

    print(f"Correct, you've guessed the right number")
    print(f"in {guesses} guesses!")
    print(f"-----------------------------------------------")
    print(f"That's amazing!")

main()
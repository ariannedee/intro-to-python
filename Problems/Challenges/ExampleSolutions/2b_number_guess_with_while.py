"""
Number guessing game
The number to guess will be from 1 to 20 (inclusive).
The user will have 4 guesses to guess the number correctly.
After each wrong guess, the user will be told whether to
guess higher or lower next time.
If the user doesn't win, tell them the number.
"""
import random


def run_game():
    number = random.randint(1, 21)
    max_guesses = 4
    current_guess = 1

    print("I'm thinking of a number between 1 and 20")

    while current_guess <= max_guesses:
        guess = int(input("Guess a number: "))
        if guess == number:
            print("That's right!")
            return
        elif current_guess == max_guesses:
            print("Nope! It was " + str(number))
            return
        elif number < guess:
            print("Lower")
        else:
            print("Higher")
        current_guess += 1


run_game()

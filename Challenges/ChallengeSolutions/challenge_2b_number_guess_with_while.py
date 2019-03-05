"""
Number guessing game
The number to guess will be from 1 to 20 (inclusive).
The user will have 3 guesses to guess the number correctly.
After each wrong guess, the user will be told whether to
guess higher or lower next time.
If the user doesn't win, tell them the number.
"""
import random


def run_game():
    number = random.randint(1, 20)
    max_guesses = 4
    current_guess = 0

    print("I'm thinking of a number between 1 and 20")

    while True:
        guess = int(input("Guess a number: "))
        current_guess += 1
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
        print('You have {} guesses left'.format(max_guesses - current_guess))


run_game()

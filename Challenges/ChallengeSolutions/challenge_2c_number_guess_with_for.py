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
    # Write code here
    answer = random.randint(1, 20)
    guess = int(input("guess a number between 1 and 20: "))

    for i in range(4):
        if guess == answer:
            print("That's right!")
            break
        if guess < answer:
            print("Higher")
        else:
            print("Lower")
        print('You have {} guesses left'.format(4-i))

        guess = int(input("guess a number between 1 and 20: "))

    print("the answer is {}".format(answer))


run_game()

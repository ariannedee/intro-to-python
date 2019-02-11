"""
Word guess refactored to use list comprehensions, perform input validation,
and test functions.

display_word uses a list comprehension.
get_guess does some validation.
Tests are in challenge_3e_word_guess_tests.py
"""
import random


def display_word(word, guessed_letters):
    letters = [letter if letter in guessed_letters else '_' for letter in word]
    return ' '.join(letters)


def guess_is_correct(guess, word):
    return guess in word


def game_won(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True


def game_lost(guesses_left):
    return guesses_left == 0


def get_guess():
    guess = input('Guess a letter: ')
    valid = len(guess) == 1 and guess.isalpha()
    return guess.lower(), valid


def word_game(word):
    word = word.lower()
    guessed_letters = []
    wrong_guesses_left = 6

    while True:
        # Display current state of the game
        print(display_word(word, guessed_letters))
        print(f'Guessed letters: {" ".join(guessed_letters)}')
        print(f'Guesses left: {wrong_guesses_left}\n')

        # Get a guess from the user
        guess, valid = get_guess()
        if not valid:
            print('Invalid guess. Please enter a single letter')

        # Handle the user's guess
        guessed_letters.append(guess)
        if guess_is_correct(guess, word):
            print('Correct!')
        else:
            wrong_guesses_left -= 1
            print('Nope!')

        # Check to see if they won or lost
        if game_won(word, guessed_letters):
            print(f'You won :) The word was "{word}"')
            return
        elif game_lost(wrong_guesses_left):
            print(f'You lost :( The word was "{word}"')
            return


# Choose a random word
with open('words.txt', 'r') as file:
    words = file.readlines()
    answer = random.choice(words).strip()

word_game(answer)

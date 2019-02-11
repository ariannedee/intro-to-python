"""
Refactored word guessing game that gets a random word from the file 'words.txt'
"""
import random


def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
        displayed_word += ' '
    return displayed_word


def guess_is_correct(guess, word):
    return guess in word


def game_won(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True


def game_lost(guesses_left):
    return guesses_left == 0


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
        guess = input('Guess a letter: ')
        print()

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


with open('words.txt', 'r') as file:
    words = file.readlines()
    answer = random.choice(words).strip()

word_game(answer)

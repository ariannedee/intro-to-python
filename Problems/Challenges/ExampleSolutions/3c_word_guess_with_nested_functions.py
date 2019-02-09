"""
Word guessing game (hangman)
Choose a word for the user to guess.
The user can have 6 wrong guesses before they lose the game.
After each guess, display the correct guesses, the wrong guesses,
and the number of wrong guesses left.
If the user doesn't win, tell them the answer.
"""
import random


def word_game(word):
    word = word.lower()
    guessed_letters = []
    wrong_guesses_left = 6

    def display_word():
        displayed_word = ''
        for letter in word:
            if letter in guessed_letters:
                displayed_word += letter
            else:
                displayed_word += '_'
            displayed_word += ' '
        return displayed_word

    def guess_is_correct(guess):
        return guess in word

    def game_won():
        for letter in word:
            if letter not in guessed_letters:
                return False
        return True

    def game_lost():
        return wrong_guesses_left == 0

    while True:
        # Display current state of the game
        print(display_word())
        print(f'Guessed letters: {" ".join(guessed_letters)}')
        print(f'Guesses left: {wrong_guesses_left}\n')

        # Get a guess from the user
        guess = input('Guess a letter: ')
        print()

        # Handle the user's guess
        guessed_letters.append(guess)
        if guess_is_correct(guess):
            print('Correct!')
        else:
            wrong_guesses_left -= 1
            print('Nope!')

        # Check to see if they won or lost
        if game_won():
            print(f'You won :) The word was "{word}"')
            return
        elif game_lost():
            print(f'You lost :( The word was "{word}"')
            return


# Choose a random word
with open('words.txt', 'r') as file:
    words = file.readlines()
    answer = random.choice(words).strip()

word_game(answer)

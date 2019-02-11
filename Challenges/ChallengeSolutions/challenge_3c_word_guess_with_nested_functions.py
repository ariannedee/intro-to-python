"""
Word guess game refactored so to use nested functions.
The inner functions can use variables from the outer function's scope.
You no longer have to pass 'word' and 'guessed_letters' around.
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

    def guess_is_correct(letter):
        return letter in word

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

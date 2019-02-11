"""
Word guess refactored to use classes.

Some explanation:
__init__ is the default function that gets called when you instantiate
a new object, e.g. game = WordGame()

Classes have properties (e.g. word) that can be accessed within the
class by calling self.property_name (e.g. self.word).

Methods are functions that belong to an object (e.g. game_won) and are
run by calling self.method_name (e.g. self.game_won() ).

In this case, display_word is a method that acts like a property
because it uses a property decorator (@property), so it can be accessed
by calling self.display_word, not self.display_word() <- no parentheses.
"""
import random


# Choose a random word
def random_word():
    with open('words.txt', 'r') as file:
        words = file.readlines()
        word = random.choice(words).strip()
    return word


class WordGame(object):
    def __init__(self):
        self.word = random_word().lower().strip()
        self.guessed_letters = []
        self.wrong_guesses_left = 6

    @property
    def display_word(self):
        displayed_word = ''
        for letter in self.word:
            if letter in self.guessed_letters:
                displayed_word += letter
            else:
                displayed_word += '_'
            displayed_word += ' '
        return displayed_word

    def guess_is_correct(self, guess):
        return guess in self.word

    def game_won(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True

    def game_lost(self):
        return self.wrong_guesses_left == 0

    def play_game(self):
        while True:
            # Display current state of the game
            print(self.display_word)
            print(f'Guessed letters: {" ".join(self.guessed_letters)}')
            print(f'Guesses left: {self.wrong_guesses_left}\n')

            # Get a guess from the user
            guess = input('Guess a letter: ')
            print()

            # Handle the user's guess
            self.guessed_letters.append(guess)
            if self.guess_is_correct(guess):
                print('Correct!')
            else:
                self.wrong_guesses_left -= 1
                print('Nope!')

            # Check to see if they won or lost
            if self.game_won():
                print(f'You won :) The word was "{self.word}"')
                return
            elif self.game_lost():
                print(f'You lost :( The word was "{self.word}"')
                return


game = WordGame()
game.play_game()

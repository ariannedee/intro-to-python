"""
Word guessing game (hangman)
Choose a word for the user to guess.
The user can have 6 wrong guesses before they lose the game.
After each guess, display the correct guesses, the wrong guesses,
and the number of wrong guesses left.
If the user doesn't win, tell them the answer.
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

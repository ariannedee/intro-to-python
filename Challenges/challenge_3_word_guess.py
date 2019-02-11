words = ['account', 'addition', 'adjustment', 'advertisement', 'agreement',
         'amount', 'amusement', 'animal', 'answer', 'apparatus', 'approval',
         'argument', 'attack', 'attempt', 'attention', 'attraction',
         'authority', 'balance', 'behavior', 'belief', 'breath', 'brother',
         'building', 'business', 'butter', 'canvas', 'chance', 'change',
         'comfort', 'committee', 'company', 'comparison', 'competition',
         'condition', 'connection', 'control', 'copper', 'cotton', 'country',
         'credit', 'current', 'damage', 'danger', 'daughter', 'decision',
         'degree', 'design', 'desire', 'destruction', 'detail', 'development',
         'digestion', 'direction', 'discovery', 'discussion', 'disease',
         'disgust', 'distance', 'distribution', 'division', 'driving',
         'education', 'effect', 'example', 'exchange', 'existence', 'expansion',
         'experience', 'expert', 'family', 'father', 'feeling', 'fiction',
         'flight', 'flower', 'friend', 'government', 'growth', 'harbor',
         'harmony', 'hearing', 'history', 'impulse', 'increase', 'industry',
         'insect', 'instrument', 'insurance', 'interest', 'invention',
         'journey', 'knowledge', 'language', 'learning', 'leather', 'letter',
         'liquid', 'machine', 'manager', 'market', 'measure', 'meeting',
         'memory', 'middle', 'minute', 'morning', 'mother', 'motion',
         'mountain', 'nation', 'number', 'observation', 'operation', 'opinion',
         'organisation', 'ornament', 'payment', 'person', 'pleasure', 'poison',
         'polish', 'porter', 'position', 'powder', 'process', 'produce',
         'profit', 'property', 'protest', 'punishment', 'purpose', 'quality',
         'question', 'reaction', 'reading', 'reason', 'record', 'regret',
         'relation', 'religion', 'representative', 'request', 'respect',
         'reward', 'rhythm', 'science', 'secretary', 'selection', 'servant',
         'silver', 'sister', 'sneeze', 'society', 'statement', 'stitch',
         'stretch', 'structure', 'substance', 'suggestion', 'summer', 'support',
         'surprise', 'system', 'teaching', 'tendency', 'theory', 'thought',
         'thunder', 'transport', 'trouble', 'vessel', 'weather', 'weight',
         'winter', 'writing']
hard_words = ['Awkward', 'Bagpipes', 'Banjo', 'Bungler', 'Croquet', 'Crypt',
              'Dwarves', 'Fervid', 'Fishhook', 'Fjord', 'Gazebo', 'Gypsy',
              'Haiku', 'Haphazard', 'Hyphen', 'Ivory', 'Jazzy', 'Jiffy', 'Jinx',
              'Jukebox', 'Kayak', 'Kiosk', 'Klutz', 'Memento', 'Mystify',
              'Numbskull', 'Ostracize', 'Oxygen', 'Pajama', 'Phlegm', 'Pixel',
              'Polka', 'Quad', 'Quip', 'Rhythmic', 'Rogue', 'Sphinx', 'Squawk',
              'Swivel', 'Toady', 'Twelfth', 'Unzip', 'Waxy', 'Wildebeest',
              'Yacht', 'Zealous', 'Zigzag', 'Zippy', 'Zombie']

"""
Word guessing game (hangman)
Choose a word for the user to guess.
The user can have 6 wrong guesses before they lose the game.
After each guess, display the correct guesses, the wrong guesses,
and the number of wrong guesses left.
If the user doesn't win, tell them the answer.
"""


# Fill out function so it returns the current state of the game

def display_word(word, guessed_letters):
    """
    :param word: The correct word
    :param guessed_letters: The letters guessed so far
    :return: The word with letters that have been guessed and underscores for
             un-guessed letters

    Test cases:
    display_word('mom', ['o', 'a', 'm'])  =>  'm o m'
    display_word('mom', ['m']  =>  'm _ m'
    display_word('mom', ['a']  =>  '_ _ _'
    """
    return word


assert display_word('hello', []) == '_ _ _ _ _'
assert display_word('hello', ['l']) == '_ _ l l _'
assert display_word('hello', ['e', 'h', 'o', 'l']) == 'h e l l o'


def guess_is_correct(guess, word):
    return False


def game_won(word, guessed_letters):
    return False


def game_lost(wrong_guesses_left):
    return False


def word_game(word):
    guessed_letters = []
    wrong_guesses_left = 6

    while True:
        # Display current state of the game
        print(display_word(word, guessed_letters))
        print(f'Guessed letters: {guessed_letters}')
        print(f'Guesses left: {wrong_guesses_left}\n')

        # Get a guess from the user
        guess = input('Guess a letter: ')
        guessed_letters.append(guess)

        # Handle the user's guess
        if guess_is_correct(guess, word):
            print('Correct!')
        else:
            print('Nope!')

        # Check to see if they won or lost
        if game_won(word, guessed_letters):
            print(f'You won :) The word was "{word}"')
            return
        elif game_lost(wrong_guesses_left):
            print(f'You lost :( The word was "{word}"')
            return


# Choose a random word
word_game('hello')

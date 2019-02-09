import random

words = ['account', 'act', 'addition', 'adjustment', 'advertisement', 'agreement', 'air', 'amount', 'amusement',
         'animal', 'answer', 'apparatus', 'approval', 'argument', 'art', 'attack', 'attempt', 'attention', 'attraction',
         'authority', 'back', 'balance', 'base', 'behavior', 'belief', 'birth', 'bit', 'bite', 'blood', 'blow', 'body',
         'brass', 'bread', 'breath', 'brother', 'building', 'burn', 'burst', 'business', 'butter', 'canvas', 'care',
         'cause', 'chalk', 'chance', 'change', 'cloth', 'coal', 'color', 'comfort', 'committee', 'company',
         'comparison', 'competition', 'condition', 'connection', 'control', 'cook', 'copper', 'copy', 'cork', 'cotton',
         'cough', 'country', 'cover', 'crack', 'credit', 'crime', 'crush', 'cry', 'current', 'curve', 'damage',
         'danger', 'daughter', 'day', 'death', 'debt', 'decision', 'degree', 'design', 'desire', 'destruction',
         'detail', 'development', 'digestion', 'direction', 'discovery', 'discussion', 'disease', 'disgust', 'distance',
         'distribution', 'division', 'doubt', 'drink', 'driving', 'dust', 'earth', 'edge', 'education', 'effect', 'end',
         'error', 'event', 'example', 'exchange', 'existence', 'expansion', 'experience', 'expert', 'fact', 'fall',
         'family', 'father', 'fear', 'feeling', 'fiction', 'field', 'fight', 'fire', 'flame', 'flight', 'flower',
         'fold', 'food', 'force', 'form', 'friend', 'front', 'fruit', 'glass', 'gold', 'government', 'grain', 'grass',
         'grip', 'group', 'growth', 'guide', 'harbor', 'harmony', 'hate', 'hearing', 'heat', 'help', 'history', 'hole',
         'hope', 'hour', 'humor', 'ice', 'idea', 'impulse', 'increase', 'industry', 'ink', 'insect', 'instrument',
         'insurance', 'interest', 'invention', 'iron', 'jelly', 'join', 'journey', 'judge', 'jump', 'kick', 'kiss',
         'knowledge', 'land', 'language', 'laugh', 'law', 'lead', 'learning', 'leather', 'letter', 'level', 'lift',
         'light', 'limit', 'linen', 'liquid', 'list', 'look', 'loss', 'love', 'machine', 'man', 'manager', 'mark',
         'market', 'mass', 'meal', 'measure', 'meat', 'meeting', 'memory', 'metal', 'middle', 'milk', 'mind', 'mine',
         'minute', 'mist', 'money', 'month', 'morning', 'mother', 'motion', 'mountain', 'move', 'music', 'name',
         'nation', 'need', 'news', 'night', 'noise', 'note', 'number', 'observation', 'offer', 'oil', 'operation',
         'opinion', 'order', 'organisation', 'ornament', 'owner', 'page', 'pain', 'paint', 'paper', 'part', 'paste',
         'payment', 'peace', 'person', 'place', 'plant', 'play', 'pleasure', 'point', 'poison', 'polish', 'porter',
         'position', 'powder', 'power', 'price', 'print', 'process', 'produce', 'profit', 'property', 'prose',
         'protest', 'pull', 'punishment', 'purpose', 'push', 'quality', 'question', 'rain', 'range', 'rate', 'ray',
         'reaction', 'reading', 'reason', 'record', 'regret', 'relation', 'religion', 'representative', 'request',
         'respect', 'rest', 'reward', 'rhythm', 'rice', 'river', 'road', 'roll', 'room', 'rub', 'rule', 'run', 'salt',
         'sand', 'scale', 'science', 'sea', 'seat', 'secretary', 'selection', 'self', 'sense', 'servant', 'sex',
         'shade', 'shake', 'shame', 'shock', 'side', 'sign', 'silk', 'silver', 'sister', 'size', 'sky', 'sleep', 'slip',
         'slope', 'smash', 'smell', 'smile', 'smoke', 'sneeze', 'snow', 'soap', 'society', 'son', 'song', 'sort',
         'sound', 'soup', 'space', 'stage', 'start', 'statement', 'steam', 'steel', 'step', 'stitch', 'stone', 'stop',
         'story', 'stretch', 'structure', 'substance', 'sugar', 'suggestion', 'summer', 'support', 'surprise', 'swim',
         'system', 'talk', 'taste', 'tax', 'teaching', 'tendency', 'test', 'theory', 'thing', 'thought', 'thunder',
         'time', 'tin', 'top', 'touch', 'trade', 'transport', 'trick', 'trouble', 'turn', 'twist', 'unit', 'use',
         'value', 'verse', 'vessel', 'view', 'voice', 'walk', 'war', 'wash', 'waste', 'water', 'wave', 'wax', 'way',
         'weather', 'week', 'weight', 'wind', 'wine', 'winter', 'woman', 'wood', 'wool', 'word', 'work', 'wound',
         'writing', 'year']

hard_words = ['Awkward', 'Bagpipes', 'Banjo', 'Bungler', 'Croquet', 'Crypt', 'Dwarves', 'Fervid', 'Fishhook', 'Fjord',
              'Gazebo', 'Gypsy', 'Haiku', 'Haphazard', 'Hyphen', 'Ivory', 'Jazzy', 'Jiffy', 'Jinx', 'Jukebox', 'Kayak',
              'Kiosk', 'Klutz', 'Memento', 'Mystify', 'Numbskull', 'Ostracize', 'Oxygen', 'Pajama', 'Phlegm', 'Pixel',
              'Polka', 'Quad', 'Quip', 'Rhythmic', 'Rogue', 'Sphinx', 'Squawk', 'Swivel', 'Toady', 'Twelfth', 'Unzip',
              'Waxy', 'Wildebeest', 'Yacht', 'Zealous', 'Zigzag', 'Zippy', 'Zombie']

"""
Word guessing game (hangman)
Choose a word for the user to guess.
The user can have 6 wrong guesses before they lose the game.
After each guess, display the correct guesses, the wrong guesses,
and the number of wrong guesses left.
If the user doesn't win, tell them the answer.
"""


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


# Choose a random word
word_game(random.choice(words))

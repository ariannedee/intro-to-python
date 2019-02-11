"""
Tests some of the functions in word_guessing_game
Look into unittest, pytest, and mock libraries for more advanced tests
"""
from .challenge_3e_word_guess_refactored import (
    display_word,
    game_won,
    guess_is_correct
)


assert display_word('hello', []) == '_ _ _ _ _'
assert display_word('hello', ['l']) == '_ _ l l _'
assert display_word('hello', ['e', 'h', 'o', 'l']) == 'h e l l o'


assert not game_won('hello', [])
assert not game_won('hello', ['h', 'a', 'e', 'l', 'b'])
assert game_won('hello', ['h', 'a', 'e', 'l', 'b', 'o'])
assert game_won('', [])


assert not guess_is_correct('a', 'hello')
assert guess_is_correct('e', 'hello')

from unittest.mock import patch
from guess_the_word import GuessGame

def test_random_word_from_list():
    game = GuessGame()
    game.startup()
    random_word = game.get_current_random_word()
    assert random_word in game.get_words_list()

@patch('builtins.input', return_value='') # Mock input to return an empty string between inputs
def test_correct_guesses(mock_input):
    game = GuessGame()
    game.startup()
    random_word = game.get_current_random_word()

    for letter in random_word:
        game.register_guess(letter)

    assert game.is_over == True
    assert game.get_guess_word() == random_word

@patch('builtins.input', return_value='') # Mock input to return an empty string between inputs
def test_incorrect_guesses(mock_input):
    game = GuessGame()
    game.startup()

    guesses_left = game.default_guesses

    for guess in range(0, guesses_left):
        game.register_guess("z")

    assert game.is_over == True
    assert game.can_guess() == False
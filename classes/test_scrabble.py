from scrabble import word_created   # reimport word_score
# import pytest

# @pytest.mark.parametrize("test_word, expected_score",
# [
#     ("HAPPY", 15),
#     ("FOG", 7),
#     ("FROG", 8),
#     ("SPARTA", 8),
#     ("GLOBAL", 9),
#     ("", 0),
#     ("A", 1),
# ])
# def test_word_score(test_word, expected_score):
#     assert word_score(test_word) == expected_score
#
# @pytest.fixture
# def example_word():
#     return "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#
# def test_count_score_fixture(example_word):
#     assert word_score(example_word) == 87


def test_word_created():
    assert word_created("ABC", "ABCDEFG") is True
    assert word_created("XYZ", "EUNSOWR") is False

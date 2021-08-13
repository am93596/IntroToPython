# Scrabble Hand

# Randomly generate a hand
# (or complete a hand)
# Check a word can be played
# Get a word score

from new_scrabble import ScrabbleHand
s = ScrabbleHand()

def test_hand_inits_with_7_tiles():
    assert len(s.tiles) == 7

def test_tiles_is_a_string():
    assert type(s.tiles) is str

def test_get_tiles():
    assert s.get_tiles() == s.tiles

def test_get_tiles_length():
    assert len(s.get_tiles()) == 7

def test_get_tiles_string():
    assert type(s.get_tiles()) is str

def test_valid_word():
    s2 = ScrabbleHand()
    s2.tiles = "CJTUDSI"
    assert s2.is_valid_word("JITSU") is True

def test_invalid_word():
    s3 = ScrabbleHand()
    s3.tiles = "CJTUDSI"
    assert s3.is_valid_word("JIUJITSU") is False

def test_get_score():
    s = ScrabbleHand()
    assert s.get_score("FACE") == 9

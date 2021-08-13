# Scrabble Hand

# Randomly generate a hand
# (or complete a hand)
# Check a word can be played
# Get a word score
import random
import string


class ScrabbleHand:
    def __init__(self):
        self.tiles = ""
        for x in range(7):
            self.tiles += random.choice(string.ascii_uppercase)
        self.score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
                      "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
                      "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
                      "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
                      "x": 8, "z": 10}

    def get_tiles(self):
        return self.tiles

    def is_valid_word(self, word_check):
        word_check_list = list(word_check)
        tile_list = list(self.tiles)
        for char in word_check_list:
            if char not in tile_list:
                return False
            else:
                tile_list.remove(char)
        return True

    def get_score(self, word):
        total_score = 0
        for letter in word:
            total_score += self.score[letter.lower()]
        return total_score


if __name__ == "__main__":
    s = ScrabbleHand()
    print(s.get_tiles())

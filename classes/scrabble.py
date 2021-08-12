# Scrabble Checker Object
# Initialise it with a string of 7 random letters - Done!
    # Option of providing some letters, and the rest randomly generated
# A method to check that a submitted word can be made from those tiles - Done!
# A method to return the score for a submitted word
# A method to use the methods above to check a word is valid
# and if it is, return the score for that word
# import random
#
#
# class ScrabbleChecker:
#     def __init__(self):
#         alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         list_of_random_letters = random.choices(alphabet, k=7)
#         self.random_letters = ''.join(list_of_random_letters)
#
#     def check_if_word_can_be_created(self, input_word):
#         input_word = input_word.upper()
#         letters_present = 0
#         word_made = False
#         for letter in input_word:
#             if letter in self.random_letters:
#                 print(f"Letter {letter} is present!")
#                 letters_present += 1
#             else:
#                 print(f"Letter {letter} not found")
#         if letters_present == len(input_word):
#             word_made = True
#         print(f"Finished checking word {input_word} against {self.random_letters}!")
#         print(f"Letters present: {letters_present}")
#         print(f"Word made: {word_made}")
#
#
#     def word_score(word: str) -> int:
#         one = "AEILNORSTU"
#         two = "DG"
#         three = "BCMP"
#         four = "FHVWY"
#         five = "K"
#         eight = "JX"
#         ten = "ZQ"
#
#         score = 0
#
#         for letter in word:
#             if letter in one:
#                 score += 1
#             elif letter in two:
#                 score += 2
#             elif letter in three:
#                 score += 3
#             elif letter in four:
#                 score += 4
#             elif letter in five:
#                 score += 5
#             elif letter in eight:
#                 score += 8
#             elif letter in ten:
#                 score += 10
#         return score
#
# sc = ScrabbleChecker()
# print(sc.random_letters)
# sc.check_if_word_can_be_created("eta")

def word_score(word: str) -> int:
    one = "AEILNORSTU"
    two = "DG"
    three = "BCMP"
    four = "FHVWY"
    five = "K"
    eight = "JX"
    ten = "ZQ"

    score = 0

    for letter in word:
        if letter in one:
            score += 1
        elif letter in two:
            score += 2
        elif letter in three:
            score += 3
        elif letter in four:
            score += 4
        elif letter in five:
            score += 5
        elif letter in eight:
            score += 8
        elif letter in ten:
            score += 10
    return score

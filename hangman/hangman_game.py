import random
from hangman_words import word_list


# FUNCTION DEFINITIONS


# function that randomly selects a word
def randomly_select_word():
    return random.choice(word_list)


def find_letters_in_word(letter_guess, game_word):
    letter_positions = []
    for index, char in enumerate(game_word):
        if char == letter_guess:
            letter_positions.append(index)
    return letter_positions


def process_guess(letter, game_word, updated_board):
    positions = find_letters_in_word(letter, game_word)
    if positions:
        for p in positions:
            updated_board = updated_board[:p] + letter + updated_board[p+1:]
        return updated_board
    else:
        print("Wrong! Guess again.")
        return updated_board


# function that takes input guesses
def input_guess(used_guesses):
    input_verified = False
    guess = None
    while not input_verified:
        guess = input("What is your guess?\n")
        if verify_input(guess) and not already_used(guess, used_guesses):
            input_verified = True
            guess = guess.upper()
    return guess


# function that verifies the input is 1 letter
def verify_input(guess):
    print("Checking input...\n")
    if len(guess) != 1 or guess.isalpha() is False:
        print("Please enter a single letter as your guess\n")
        return False
    else:
        return True


# function that checks if letter has already been guessed
def already_used(guess, used_guesses):
    if guess.upper() in used_guesses:
        print("Sorry, you've already guessed that letter. Try again\n")
        return True
    else:
        print("Great! That letter hasn't been guessed yet!\n")
        return False


# function that reduces lives when a guess is wrong
def reduce_lives(current_lives):
    return current_lives - 1


# GAME RUNS FROM HERE
word = randomly_select_word()
board = '_' * len(word)
lives = 3
already_guessed = []
print(board)

next_guess = input_guess(already_guessed)
board = process_guess(next_guess, word, board)
print(f"Board: {board}")
print(f"Lives: {lives}")
print(word)

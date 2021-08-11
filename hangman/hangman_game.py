import random
from hangman_words import word_list


# function that randomly selects a word
def randomly_select_word():
    return random.choice(word_list)


# TODO: function that outputs game
# might want to put the main function calls in here,
# then call this through main?
def output_game(word):
    print("_" * (len(word)))


# function that takes input guesses
def input_guesses():
    guess = input("What is your guess?\n")
    verify_input(guess)
    return guess


# function that verifies the input is 1 letter
def verify_input(guess):
    print("Checking input...")
    if len(guess) != 1 or guess.isalpha() is False:
        print("Please enter a single letter as your guess")
    else:
        print("Thanks!")


# function that identifies where a given letter appears in a given word
# and returns either False or a list of locations
def find_letter_in_word(guess, word):
    guess_locations = []
    index = 0
    for letter in word:
        if letter == guess.upper():
            guess_locations.append(index)
        index += 1
    if len(guess_locations) < 1:
        return False
    else:
        return guess_locations


# function that checks if letter has already been guessed
def already_used(guess, used_guesses):
    if guess in used_guesses:
        print("Sorry, you've already guessed that letter. Try again")
        return True
    else:
        print("Great! That letter hasn't been guessed yet!")
        return False


# TODO: function that adds stuff to hangman when a guess is wrong

# function that reveals correctly guessed letters - except that sometimes (not always!!!) it does something wrong
def reveal_correct_guess(locations, answer):
    updated_word = ""
    # This is the loop where it keeps going wrong! I want it to only add '_' for unsolved letters
    # sometimes it does
    # sometimes it does too many
    # e.g. for STERNUTATION, and input 't', printed out: _T____TT
    # never mind how to get this to work when some letters have been filled in
    # fix that later
    for index in locations:
        print(f"updated_word index: {index-len(updated_word)}")  # debugging line
        updated_word += ("_" * (index-len(updated_word)))
        updated_word += answer[index]
        #updated_word_length += len(index-updated_word_length)
        # for sublist in updated_word: this for loop is turning out wrong - replace it with something that
        #                              updates the length of updated_word
        #     print(f"sublist: {sublist}")
        #     updated_word_length += len(sublist)
    print(len(answer))  # debugging line
    print(len(updated_word))  # debugging line
    print(updated_word)
    if len(updated_word) < len(answer):  # fails this test if 1st letter is guessed, as 1st element '' is counted as 1
        print(f"Difference: {len(answer)-len(updated_word)}")
        updated_word += "_" * (len(answer)-len(updated_word))
    print(f"Final: {updated_word}")
    # string_version_updated_word = ""
    # for sublist in updated_word:
    #     for elem in sublist:
    #         string_version_updated_word += '_'.join(str(elem))
    # for sublist in updated_word:
    #     print(f"Sublist: {sublist}")
    #     string_version_updated_word = "".join(sublist)
    # print(f"Final: {string_version_updated_word}")

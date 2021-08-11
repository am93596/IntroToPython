from hangman_game import randomly_select_word, output_game, input_guesses, find_letter_in_word, already_used, reveal_correct_guess


# TODO: main function to run the game
def main():
    previous_guesses = []
    random_word = randomly_select_word()
    print(random_word)
    output_game(random_word)
    guess = input_guesses()
    if not already_used(guess, previous_guesses):
        previous_guesses.append(guess)
        correct_guess_locations = find_letter_in_word(guess, random_word)
        print(correct_guess_locations)
        reveal_correct_guess(correct_guess_locations, random_word)
    # else prompt again


main()

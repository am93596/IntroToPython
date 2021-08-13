from new_scrabble import ScrabbleHand


class ScrabbleGame:
    def __init__(self):
        self.total_score = 0

    def single_round(self):
        self.hand = ScrabbleHand()
        print(self.hand.get_tiles())
        self.guess = self.get_word_guess()
        score = self.hand.get_score(self.guess)
        self.total_score += score

    def get_word_guess(self):
        # Ask the user to input a guess
        # Use self.hand.is_valid_word to check it's valid
        # Loop until valid
        # Return the guess
        pass

    def ask_to_play_again(self):
        pass

    def exit_message(self):
        pass

    def main(self):
        while True:
            self.single_round()
            new_round = self.ask_to_play_again()
            if not new_round:
                break
            print(self.exit_message())

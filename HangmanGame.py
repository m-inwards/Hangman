from random import shuffle
from nltk.corpus import words


class HangmanGame:
    def __init__(self):
        # Define all required variables
        self.dictionary = []
        self.selected_word = ""
        self.guessed_letters = []
        self.num_of_guesses_left = 13
        self.correct_answer_guessed = False
        self.guess = ""

        # Call necessary functions to prep variables for the game
        self.populate_dictionary()
        self.select_word()

        # Start the game
        self.play_game()

    def restart_game(self):
        self.selected_word = ""
        self.guessed_letters = []
        self.num_of_guesses_left = 13
        self.correct_answer_guessed = False
        self.guess = ""

        self.select_word()
        self.play_game()

    def populate_dictionary(self):
        self.dictionary = words.words()

    def select_word(self):
        self.shuffle_dictionary()
        self.selected_word = self.dictionary[0]

    def shuffle_dictionary(self):
        shuffle(self.dictionary)
        shuffle(self.dictionary)
        shuffle(self.dictionary)

    def get_letter_from_player(self):
        self.guess = ""

        while len(self.guess) != 1:
            self.guess = input("Please enter a letter to guess:\n")

    def display_hangman_characters(self):
        hangman_characters = ""

        for letter in self.selected_word:
            if letter in self.guessed_letters:
                hangman_characters += letter
            else:
                hangman_characters += "_"

        print(hangman_characters)

    def check_answer(self):
        answer_correct = True

        for letter in self.selected_word:
            if letter not in self.guessed_letters:
                answer_correct = False
                break

        self.correct_answer_guessed = answer_correct

    def play_game(self):
        while self.num_of_guesses_left > 0 and self.correct_answer_guessed is False:
            print("==============================================")
            print(f"You have {self.num_of_guesses_left} {'guesses' if self.num_of_guesses_left != 1 else 'guess'} remaining:")
            print(f"So far you have guessed {', '.join(self.guessed_letters)}") if len(self.guessed_letters) > 0 else ""
            self.display_hangman_characters()

            self.get_letter_from_player()
            self.guessed_letters.append(self.guess) if self.guess not in self.guessed_letters else ""

            # Removes a guess if they got it wrong
            self.num_of_guesses_left -= 1 if self.guess not in self.selected_word else 0

            # Checks if they have got the word
            self.check_answer()

        # Responds whether they got it or not and the appropriate message
        if self.correct_answer_guessed:
            self.display_hangman_characters()
            print("Congratulations, you got it right!")
        else:
            print(f"Commiserations, you didnt quite get it. The word was: {self.selected_word}")

        # Checks if the player wants to play again
        play_again = ""

        while play_again.lower() not in ["yes", "y", "no", "n"]:
            play_again = input("Would you like to play again? (Y/N):\n")

        if play_again.lower() in ["yes", "y"]:
            self.restart_game()
        else:
            print("Thanks for playing, I hope you had fun :)")


if __name__ == "__main__":
    HangmanGame()

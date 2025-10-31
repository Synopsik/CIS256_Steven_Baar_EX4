import random
import os, subprocess

class GuessGame:
    def __init__(self):
        self.is_over = False
        self._words_list = ["cipher","epoch","glyph","kernel","matrix","nexus","pixel","vector","daemon","lambda"]
        self._random_word = ""
        self._guess_word = ""
        self.default_guesses = 10
        self._guesses = self.default_guesses


    def get_words_list(self) -> list[str]:
        return self._words_list


    def get_current_random_word(self) -> str:
        return self._random_word

    def get_guess_word(self) -> str:
        return self._guess_word

    def set_random_word(self) -> None:
        if not self._words_list:
            raise Exception("No elements in words list")
        self._random_word = random.choice(self._words_list)


    def can_guess(self) -> bool:
        return self._guesses > 0


    def startup(self) -> None:
        self._clear()
        self.set_random_word()
        self._guess_word = ""
        self._guesses = self.default_guesses
        self.is_over = False


    def register_guess(self, letter) -> None:
        self._guesses -= 1
        if letter == self._random_word[len(self._guess_word)]:
            self._guess_word += letter
            if len(self._guess_word) == len(self._random_word):
                self._clear()
                print("You win!")
                print(f"Correct Word: {self._random_word}")
                input("Press Enter to continue...")
                self.is_over = True
                return
            # self._guesses = self.default_guesses # Uncomment to reset user guesses after a correct guess
            self._clear()
        else:
            if not self.can_guess():
                self._clear()
                print("You lose!")
                input("Press Enter to continue...")
                self.is_over = True
                return
            print("\nIncorrect, try again!")
            input("Press Enter to continue...")
            self._clear()



    def take_guess(self) -> str:
        while True:
            print("Welcome to the word-guessing game!")
            print(f"Remaining Guesses: {self._guesses}")
            # print(f"Random Word: {self._random_word}") # Uncomment to include the random word in the output

            if len(self._guess_word) > 0:
                print(f"\nCurrent Guess: {self._guess_word}")

            guess = input("\nEnter a single letter: ")
            if (isinstance(guess, str)
                    and guess.isalpha()
                    and len(guess) == 1):
                return guess

            print("\nError! Type only a single alphabetic letter to continue.")
            input("Press Enter to continue")
            self._clear()


    @staticmethod # If you don't need to use `self` anywhere in your method
    def _clear() -> None:
        """
        Using the subprocess and os modules, determine the os type and clear the console screen.

        :return: None
        """
        if os.name == 'nt':
            # This is safer than os.system('cls')
            subprocess.run(['cls'], shell=True, check=False)
        else:
            subprocess.run(['clear'], check=False)


def main() -> None:
    game = GuessGame()

    while True:
        game.startup()
        while not game.is_over:
            guess = game.take_guess()
            game.register_guess(guess)


if __name__ == "__main__":
    main()

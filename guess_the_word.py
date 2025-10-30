import random
import os, subprocess


class GuessGame:
    def __init__(self):
        self._words = [
            "apple","anchor","azure","brick","bridge","bubble","candle","canvas","cipher","clutch",
            "clock","cloud","cobalt","comet","crisp","delta","dune","ember","epoch","echo",
            "flint","forge","frame","glimmer","glyph","harbor","hatch","haze","hybrid","iris",
            "ivory","jade","jolt","kernel","lumen","lark","matrix","meadow","mint","mosaic",
            "nexus","nova","nimbus","oak","onyx","orbit","orchid","pivot","pixel","plume",
            "quartz","quill","raven","ripple","rook","sable","saturn","scarlet","shift","silk",
            "spire","sprite","summit","tango","tide","timber","token","tuple","umbra","urban",
            "valve","vapor","vector","verdant","vex","vital","wisp","willow","wrath","xenon",
            "yarn","yarrow","yield","zephyr","zinc","zen","spark","scale","byte","cache",
            "agent","bytecode","cluster","daemon","engine","flask","grid","heap","index","lambda"
        ]
        self._random_word = ""
        self.get_random_word()
        self.start_guessing()


    def get_random_word(self) -> None:
        if not self._words:
            raise Exception("No elements in words list")
        self._random_word = random.choice(self._words)


    def start_guessing(self) -> bool:
        self._clear()
        guess_word = ""
        tries = 0
        while True:
            print(self._random_word)
            print(f'Word = "{guess_word}"\n')
            letter = input("Guess each letter: ")
            if letter == self._random_word[len(guess_word)]:
                guess_word += letter
                self._clear()
                if len(guess_word) == len(self._random_word):
                    print("You win!")
                    return True
            else:
                tries += 1
                if tries > 10:
                    print("You lose!")
                    return False
                print("\nIncorrect, try again!")
                input("Press Enter to continue...")
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


if __name__ == "__main__":
    main()
import string
import random

SAMPLE_WORDS = ["cat", "stegosaurus", "alphabet"]
alphabet = string.ascii_lowercase


class Game():

    def __init__(self, word_list=SAMPLE_WORDS, debug=False):
        self.alphabet = alphabet
        self.word_list = word_list
        self.chosen_word = None
        self.represented_word = ""
        self.remaning_letters = []
        self.guessed_letters = []
        self.errors = 0
        self.DEBUG = debug
        self.finish = False
        self.MAX_ERRORS = 6

        # Initialize
        self._choose_word()
        self._set_remaning_letters()
        self._set_represented_word()

        self.hangman = {
            0: """
                    --------------
                    |                 |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                -----------
                 """,
            1: """
                    --------------
                    |                 |
                    |                 O
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                -----------
                 """,
            2: """
                    --------------
                    |                 |
                    |                 O
                    |                 |
                    |
                    |
                    |
                    |
                    |
                    |
                -----------
                 """,
            3: """
                    --------------
                    |                 |
                    |                 O
                    |                 |
                    |                 \\
                    |
                    |
                    |
                    |
                    |
                -----------
                 """,
            4: """
                    --------------
                    |                 |
                    |                 O
                    |                 |
                    |                /\\
                    |
                    |
                    |
                    |
                    |
                -----------
                 """,
            5: """
                    --------------
                    |                 |
                    |                 O
                    |                 |\\
                    |                /\\
                    |
                    |
                    |
                    |
                    |
                -----------
                 """,
            6: """
                    --------------
                    |                 |
                    |                 O
                    |                /|\\
                    |                /\\
                    |
                    |
                    |
                    |
                    |
                -----------
                 """,
        }

    def _show_board(self):
        print(f"""
            -----------------------------------------------------------------------------------------------------
            | {self.hangman[self.errors]}
            |
            | GUESS WORD: {self.represented_word}



        
        """)

    def _choose_word(self):
        self.chosen_word = random.choice(self.word_list)

    def _set_remaning_letters(self):
        self.remaning_letters = [letter for letter in self.alphabet]

    def _set_represented_word(self):
        if len(self.guessed_letters) == 0:
            self.represented_word = "_ " * len(self.chosen_word)
        else:
            temp_representation = ""
            for letter in self.chosen_word:
                if letter in self.guessed_letters:
                    temp_representation += f"{letter} "
                else:
                    temp_representation += "_ "
            self.represented_word = temp_representation

    def _ask_for_letter(self):
        letter = input(f"""Choose a letter from the remaning ones: \n
                                    {" ".join(self.remaning_letters)}
            """)
        # TODO stop errors from happening
        return letter

    def _validate_letter(self, letter):
        return letter in self.chosen_word

    def _update_guessed_letters(self, letter):
        self.guessed_letters.append(letter)

    def _update_remaning_letters(self, letter):
        self.remaning_letters.remove(letter)

    def _check_all_letters_found(self):
        for letter in self.chosen_word:
            if letter not in self.guessed_letters:
                return False
        return True

    def _check_lost_by_errors(self):
        return self.errors >= self.MAX_ERRORS

    def _have_remaning_letters(self):
        return len(self.remaning_letters) > 0

    def _check_lost_condition(self):
        return self._check_lost_by_errors() or not self._have_remaning_letters()

    def _check_game_status(self):
        if self._check_lost_condition():
            self._lost()
        if self._check_all_letters_found():
            self._win()

    def _win(self):
        self.finish = True
        print("""
            YOU WON BABY!
        """)

    def _lost(self):
        self.finish = True
        print("""
            SORRY YOU LOST BABY!
        """)

    def _update_errors(self):
        self.errors += 1

    def _execute_game_turn(self):

        self._show_board()
        letter = self._ask_for_letter()
        if self._validate_letter(letter):
            self._update_guessed_letters(letter)
        else:
            self._update_errors()

        self._update_remaning_letters(letter)
        self._set_represented_word()
        self._check_game_status()

    def _print_debug(self):

        print(f"""
                +---------------------------------+
                | word                      |  {self.chosen_word} |
                | represented_word  | {self.represented_word}|
                | guessed letters       | {self.guessed_letters} |
                | errors                     | {self.errors}|
                | remaning letters     | {self.remaning_letters}|

        """)

    def run(self):

        while not self.finish:
            self._execute_game_turn()
            if self.DEBUG:
                self._print_debug()


if __name__ == "__main__":
    game = Game(debug=False)
    game.run()

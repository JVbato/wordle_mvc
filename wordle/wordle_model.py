from enum import Enum, auto

class Correctness(Enum):
    WRONG = auto()
    INWORD = auto()
    CORRECT = auto()



class WordleModel:
    def __init__(self, max_guess: int, word: str):
        self._max_guess = max_guess
        self._word: str = word.upper() 
        self._guessed_letters: dict[str, Correctness] = {}
        self._guessed_words: list[str] = []
        self.game_over: bool = False
    
    @property
    def guessed_words(self) -> list[str]:
        return self._guessed_words

    @property
    def guessed_letters(self) -> dict[str, Correctness]:
        return self._guessed_letters
    
    def guess_word(self, guess: str):
        checker: Correctness = Correctness.WRONG
        for idx, letter in enumerate(guess):
            letter = letter.upper()
            if letter == self._word[idx]:
                checker = Correctness.CORRECT
            elif letter in self._word:
                checker = Correctness.INWORD
            else:
                checker = Correctness.WRONG

            self._guessed_letters[letter] = checker
        
        temp: list[bool] = []

        for x in guess:
            if self._guessed_letters[x.upper()] == Correctness.CORRECT:
                temp.append(True)
            else:
                temp.append(False)
        self.game_over = all(temp)  

    def add_color(self, word: str):
        colored: str = ""
        for letter in word:
            if self.guessed_letters[letter] == Correctness.WRONG:
                colored += letter
            elif self.guessed_letters[letter] == Correctness.INWORD:
                colored += f"\033[93m{letter}\033[0m"
            elif self.guessed_letters[letter] == Correctness.CORRECT:
                colored += f"\033[92m{letter}\033[0m"
        self.guessed_words.append(colored)


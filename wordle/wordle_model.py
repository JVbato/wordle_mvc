from enum import Enum, auto

class WordState(Enum):
    UNGUESSED = auto()
    WRONG = auto()
    INWORD = auto()
    CORRECT = auto()

class WordleModel:
    def __init__(self, max_guess: int, word: str):
        self._max_guess = max_guess
        self._word: str = word.upper() 
        self._letter_status: dict[str, WordState] = {}
        self._guessed_words: list[str] = []
        self.game_over: bool = False

        self._word_str: str = "QWERTYUIOPASDFGHJKLZXCVBNM"

        for letter in self._word_str:
            self._letter_status[letter] = WordState.UNGUESSED
    
    @property
    def guessed_words(self) -> list[str]:
        return self._guessed_words

    @property
    def guessed_letters(self) -> dict[str, WordState]:
        return self._letter_status
    
    @property
    def alphabets(self) -> str:
        return self._word_str
    
    def guess_word(self, guess: str):
        checker: WordState = WordState.WRONG
        for idx, letter in enumerate(guess):
            letter = letter.upper()
            if letter == self._word[idx]:
                checker = WordState.CORRECT
            elif letter in self._word:
                checker = WordState.INWORD
            else:
                checker = WordState.WRONG

            self._letter_status[letter] = checker
        
        temp: list[bool] = []

        for x in guess:
            if self._letter_status[x.upper()] == WordState.CORRECT:
                temp.append(True)
            else:
                temp.append(False)
        self.game_over = all(temp)  

    def add_color(self, word: str):
        colored: str = ""
        for letter in word:
            if self.guessed_letters[letter] == WordState.WRONG:
                colored += f"\033[91m{letter}\033[0m"

            elif self.guessed_letters[letter] == WordState.INWORD:
                colored += f"\033[93m{letter}\033[0m"
            
            elif self.guessed_letters[letter] == WordState.CORRECT:
                colored += f"\033[92m{letter}\033[0m"
            
            else:
                colored += letter

        self.guessed_words.append(colored)
    
    def curr_color(self) -> list[tuple[str, WordState]]:
        # colored: list[str] = []
        # for letter in self._word_str:
        #     if self.guessed_letters[letter] == WordState.WRONG:
        #         colored.append(f"\033[91m{letter}\033[0m")

        #     elif self.guessed_letters[letter] == WordState.INWORD:
        #         colored.append(f"\033[93m{letter}\033[0m")
            
        #     elif self.guessed_letters[letter] == WordState.CORRECT:
        #         colored.append(f"\033[92m{letter}\033[0m")
            
        #     else:
        #         colored.append(letter)
        # return colored

        return [(x, self.guessed_letters[x]) for x in self._word_str]


        


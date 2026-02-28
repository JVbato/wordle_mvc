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
        self._max_char: str = max(set(self._word), key=self._word.count)
        self._max_letter_num = self._word.count(self._max_char)
        self._letter_status: list[dict[str, WordState]] = [{} for _ in range(self._max_letter_num)]
        self._guessed_words: list[str] = []
        self.game_over: bool = False

        self._word_str: str = "QWERTYUIOPASDFGHJKLZXCVBNM"

        for idx in range(self._max_letter_num):
            for letter in self._word_str:
                self._letter_status[idx][letter] = WordState.UNGUESSED

    

    @property
    def guessed_words(self) -> list[str]:
        return self._guessed_words

    @property
    def guessed_letters(self) -> list[dict[str, WordState]]:
        return self._letter_status
    
    @property
    def alphabets(self) -> str:
        return self._word_str
    
    def guess_word(self, guess: str):
        checker: WordState = WordState.WRONG

        counter: int = 0
        guessed: list[str] = []

        for idx, letter in enumerate(guess):
            letter = letter.upper()

            if guessed.count(letter) > counter:
                counter += 1
            guessed.append(letter)

            if letter == self._word[idx]:
                checker = WordState.CORRECT
            elif letter in self._word:
                checker = WordState.INWORD
            else:
                checker = WordState.WRONG

            self._letter_status[counter][letter] = checker
        
        temp: list[bool] = []
        counter: int = 0
        guessed: list[str] = []

        for x in guess:
            if guessed.count(x) > counter:
                counter += 1
            guessed.append(x)

            if self._letter_status[counter][x.upper()] == WordState.CORRECT:
                temp.append(True)
            else:
                temp.append(False)
        self.game_over = all(temp)  

    def add_color(self, word: str):
        colored: str = ""
        counter: int = 0
        guessed: list[str] = []

        for letter in word:
            if guessed.count(letter) > counter:
                counter += 1
            guessed.append(letter)
            
            if self.guessed_letters[counter][letter] == WordState.WRONG:
                colored += f"\033[91m{letter}\033[0m"

            elif self.guessed_letters[counter][letter] == WordState.INWORD:
                colored += f"\033[93m{letter}\033[0m"
            
            elif self.guessed_letters[counter][letter] == WordState.CORRECT:
                colored += f"\033[92m{letter}\033[0m"
            
            else:
                colored += letter

        self.guessed_words.append(colored)
    
    def curr_color(self) -> list[tuple[str, WordState]]:
<<<<<<< HEAD
        return [(x, self.guessed_letters[0][x]) for x in self._word_str]
=======
        counter: int = 0
        guessed: list[str] = []
        final: list[tuple[str, WordState]] = []
        
        for letter in self._word_str:
            if guessed.count(letter) > counter:
                counter += 1
            guessed.append(letter)
            final.append((letter, self.guessed_letters[counter][letter]))


        return final
>>>>>>> 34b4b5f07c0601b1c37c8732488c4f0538cafd4f


        


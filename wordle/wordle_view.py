from wordle_model import WordState

class WordleView:
    def __init__(self, word: str, word_bank: set[str]) -> None:
        self._word = word.upper()
        self._word_bank = word_bank
    
    def give_answer(self) -> str:
        guess: str = ""

        while len(guess) != len(self._word) or (not guess.isalpha()) or (guess.lower() not in self._word_bank):
            try:
                guess = input("what is the word? ").upper()
            except KeyboardInterrupt:
                exit()
            except:
                pass
        return guess

    def print_prev(self, past_guesses: list[str]):
        print("\033c", end="")
        for guess in past_guesses:
            print(guess.center(100))
        print()

    def print_current_state(self, alphabets: list[tuple[str, WordState]]):
        def color_checker(letter: str, state: WordState) -> str:
            if state == WordState.WRONG:
                return f"\033[91m{letter}\033[0m"

            elif state == WordState.INWORD:
                return f"\033[93m{letter}\033[0m"
            
            elif state == WordState.CORRECT:
                return f"\033[92m{letter}\033[0m"
            
            else:
                return letter

        for chunk in (alphabets[:10], alphabets[10:19], alphabets[19:]):
            spaced = "".join([f" {x[0]} " for x in chunk])
        
            colored = ""
            for letter, state in chunk:
                colored += f" {color_checker(letter, state)} "
            
            padding = (60 - len(spaced)) // 2
            print(" " * padding + colored) 
    
        print()


    
        
    
        
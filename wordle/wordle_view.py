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
            print(guess)


    
        
    
        
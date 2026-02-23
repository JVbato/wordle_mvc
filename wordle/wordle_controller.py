from wordle_model import WordleModel
from wordle_view import WordleView
from word_bank import word_bank
import random


class WordleController:
    def run(self) -> None:
        answer: str = random.choice(list(word_bank))
        print(answer)
        model = WordleModel(6, answer)
        view = WordleView(answer, word_bank)
        curr_guess: str = ""
        while not model.game_over:
            model.add_color(curr_guess)
            curr_state = model.curr_color()
            view.print_prev(model.guessed_words)
            view.print_current_state(curr_state)
            curr_guess = view.give_answer()
            model.guess_word(curr_guess)
        
        model.add_color(curr_guess)
        view.print_prev(model.guessed_words)
        print("you win")


if __name__ == "__main__":
    game = WordleController()
    game.run()



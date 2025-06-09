from textual.app import App 
from graphic import _start_screen, _typing_screen, _result_screen
from textual.binding import Binding
from word_handler import get_words
from typing_test import Typing_test

class termType(App):
    BINDINGS = [
    Binding("escape", "quit", "Quit"),
    Binding("ctrl+r", "reset_test", "Reset"),
    ]

    def on_mount(self):
        words = get_words()
        self.typing_test = Typing_test(words, 10)

        self.install_screen(_start_screen(), name="start")
        self.install_screen(_typing_screen(self.typing_test), name="typing")
        self.install_screen(_result_screen(self.typing_test), name="result")
        self.push_screen("start")


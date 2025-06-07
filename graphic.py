from textual.screen import Screen
from textual.binding import Binding
from textual.containers import Vertical
from textual.widgets import Input, Static

BINDINGS = [
    Binding("escape", "quit", "Quit"),
    Binding("ctrl+r", "reset_test", "Reset"),
]

class _start_screen(Screen): 
    def compose(self):
            yield Vertical(
            Static("🤖termType", id="title"),
            id="main_layout"
        )

class _typing_screen(Screen):
    def compose(self):
        yield Vertical(
        Static("Words will go here", id="word_display"),
        Input(placeholder="typed words will go here", id="input"),
        )

class _result_screen(Screen):
    def compose(self): 
        yield Vertical (
            Static("Stats: WPM: 0 | Accuracy: 100%", id="stats"),
        )


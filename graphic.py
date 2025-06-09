from textual.screen import Screen
from textual.containers import Vertical
from textual.widgets import Input, Static


class _start_screen(Screen): 
    def compose(self):
            yield Vertical(
            Static("🤖termType", id="title"),
            Static("press enter to start", id="instruction"),
            id="start_screen"
        )

    def on_key(self, event):
        if event.key == "enter":
            self.app.push_screen("typing")

class _typing_screen(Screen):
    def __init__(self, typing_test):
        super().__init__()
        self.typing_test = typing_test

    def compose(self):
        yield Vertical(
        Static("Words will go here", id="word_display"),
        Input(placeholder="typed words will go here", id="input"),
        )
    def on_mount(self):
        test_words = self.typing_test.start_test()
        if self.typing_test.test_words:
            words_text = "".join(test_words)
            self.query_one("#word_display").update(words_text)
            self.query_one("#input").focus()

    def on_input_submitted(self, event):
        typed_text = event.value.strip()
        result = self.typing_test.handle_keystroke(typed_text)

        if result == "test completed":
            self.app.push_screen("result")
        else: 
            self.query_one("#input").value = ""
            remaning_words = self.typing_test.test_words[self.typing_test.current_index]
            if remaning_words: 
                words_text = "".join(remaning_words)
                self.query_one("#word_display").update(words_text)



class _result_screen(Screen):
    def compose(self): 
        yield Vertical (
            Static("Stats: WPM: 0 | Accuracy: 100%", id="stats"),
        )


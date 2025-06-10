from textual.screen import Screen
from textual.containers import Vertical
from textual.widgets import Input, Static
from rich.text import Text


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
            words_text = " ".join(test_words)
            self.query_one("#word_display").update(words_text)
            self.query_one("#input").focus()

    def on_input_change(self, event):
        typed_text = input.value
        result = self.typing_test.handle_keystroke(typed_text)

        self.update_display()

        if result == "test completed":
            self.app.push_screen("result")


    def update_display(self):
        display_text = Text() 
        full_text =  " ".join(self.typing_test.test_words)

        typed_length = len(self.typing_test.typed_text)

        if typed_length > 0: 
            correct_part = full_text[:self.typing_test.correct_chars]
            display_text.append(correct_part, style="green")

            if self.typing_test.correct_chars > typed_length and typed_length <= self.typing_test.full_text:
                error_part = full_text[self.typing_test.correct_chars:typed_length]
                display_text.append(error_part, style="red")
            if typed_length < len(full_text): 
                cursor_char = full_text[typed_length]
                display_text.append(cursor_char, style="yellow")
        else: 
            if full_text:
                display_text.append(full_text[0], style="dim white")
                if len(full_text) >= 1:
                    display_text.append(full_text[1], style="white")
        self.query_one("#word_display").update(display_text)




class _result_screen(Screen):
    def compose(self): 
        yield Vertical (
            Static("Stats: WPM: 0 | Accuracy: 100%", id="stats"),
        )


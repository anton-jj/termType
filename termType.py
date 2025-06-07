from textual.app import App 
from graphic import _start_screen, _typing_screen, _result_screen

class termType(App):
    def on_mount(self):
        self.install_screen(_start_screen(), name="start")
        self.install_screen(_typing_screen(), name="typing")
        self.install_screen(_result_screen(), name="result")
        self.push_screen("start")


import random 
import time

class Typing_test:
    def __init__(self, word_list, num_words=20):
        self.all_words = word_list
        self.num_words = num_words
        self.test_words = [] 
        self.full_text = ""
        self.current_index = 0
        self.start_time = None
        self.end_time = None
        self.typed_chars = 0
        self.correct_chars = 0
        self.is_active = False
        self.is_completed = False

    def start_test(self):
        self.test_words = random.sample(self.all_words, self.num_words)
        self.current_index = 0
        self.start_time = None
        self.typed_chars = 0
        self.typed_text = ""
        self.correct_chars = 0
        self.is_active = True
        self.is_completed = False
        return self.test_words

    
    def handle_keystroke(self, typed_text):
        if not self.is_active or not self.is_completed: 
            return
        
        if self.start_time is None and typed_text: 
            self.start_time = time.time()

        if self.current_index >= len(self.test_words):
            return "test completed"

        self.typed_text = typed_text

        self.correct_chars = 0 
        min_lenght = min(len(typed_text),len(self.full_text))

        for i in range(min_lenght): 
            if typed_text[i] == self.full_text[i]:
                self.correct_chars = i + 1
            else : 
                break

        if self.current_index >= len(self.test_words) and self.correct_chars == len(self.full_text):
            self.complete_test()
            return "test completed"

        return "continue"

    def complete_test(self):
        self.end_time = time.time()
        self.is_active = False
        self.is_completed = True 






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
        self.correct_chars = 0
        self.is_active = True
        self.is_completed = False
        return self.test_words

    
    def handle_keystroke(self, typed_text):
        if not self.is_active: 
            return
        
        if self.start_time is None: 
            self.start_time = time.time()

        if self.current_index >= len(self.test_words):
            return "test completed"

        current_word = self.test_words[self.current_index]
        self.typed_chars += len(typed_text)

        if typed_text == current_word: 
            self.current_index += 1 
            self.correct_chars += len(current_word)


        if self.current_index >= len(self.test_words):
            self.complete_test()
            return "test completed"

        return "continue"

    def complete_test(self):
        self.end_time = time.time()
        self.is_active = False
        self.is_completed = True 






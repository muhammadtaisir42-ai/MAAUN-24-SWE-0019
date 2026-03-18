from datetime import datetime

class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer


    def is_correct(self, choice):
        return choice == self.answer
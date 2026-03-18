from datetime import datetime

class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer
def get_next_question(self):
    return self.questions.pop(0)

    def is_correct(self, choice):
        return choice == self.answer
    class CBT:
     def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        return self.questions.pop(0)  # FIFO
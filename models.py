from datetime import datetime

class Question:
    """
    A class to represent a multiple-choice question.

    Attributes:
        text (str): The text of the question.
        options (list): A list of possible answer options.
        answer (str): The correct answer to the question.

    Methods:
        is_correct(choice):
            Checks if the provided choice matches the correct answer.
            Args:
                choice (str): The user's selected answer.
            Returns:
                bool: True if the choice is correct, False otherwise.
    """
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

    def is_correct(self, choice):
        # Normalize case for comparison
        if choice is None:
            return False
        return choice.strip().lower() == self.answer.strip().lower()
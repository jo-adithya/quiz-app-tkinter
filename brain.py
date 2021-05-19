from question import Question
from data import question_data
import html

class Quiz:
    def __init__(self):
        self.questions = [Question(question["question"], question["correct_answer"]) for question in question_data]
        self.questions.insert(0, '')
        self.number = 1
        self.score = 0
        self.max_number = len(self.questions) - 1

    def check_answer(self, answer):
        if answer == self.questions[self.number].answer:
            self.number += 1
            self.score += 1
            return True
        self.number += 1

    def next_question(self):
        if self.number > self.max_number:
            return False, False
        return f"Q.{self.number}", f"{html.unescape(self.questions[self.number].question)}"

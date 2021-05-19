class Quiz:
    def __init__(self):
        self.questions = [Question(question["text"], question["answer"]) for question in question_data]
        # noinspection PyTypeChecker
        self.questions.insert(0, '')
        self.number = 1
        self.score = 0
        self.max_number = len(self.questions) - 1

    def check_answer(self, answer):
        if answer[0] == self.questions[self.number].answer[0]:
            print("You got it right!")
            self.score += 1
        else:
            print("You're wrong")
        self.check_info()

    def check_info(self):
        print(f"The correct answer was {self.questions[self.number].answer}")
        print(f"Your current score is: {self.score}/{self.max_number}\n")
        self.number += 1
        if self.number > self.max_number:
            print("You've completed the quiz!")
            print(f"Your final score was: {self.score}/{self.max_number}")
            return
        self.next_question()

    def next_question(self):
        user_ans = input(f"Q.{self.number}: {self.questions[self.number].question} (True/False)?: ").capitalize()
        self.check_answer(user_ans)

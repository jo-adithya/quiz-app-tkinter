from tkinter import *
from tkinter import messagebox
from brain import Quiz

THEME_COLOR = "#f4f4f4"
FONT_TITLE = ('Arial', 30, 'bold')
FONT_TEXT = ('Arial', 28, 'normal')
FONT_SCORE = ('Arial', 18, 'normal')
FONT_SUBTITLE = ('Arial', 22, 'bold italic')


class UserInterface:
    def __init__(self, quiz: Quiz):
        self.quiz = quiz

        self.window = Tk()
        self.window.title('Quiz App')
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)

        self.score = Label(text='Score: 0', bg=THEME_COLOR, font=FONT_SCORE)
        self.score.grid(row=0, column=1)

        self.card_img = PhotoImage(file='images/front_card.png')
        self.correct_img = PhotoImage(file='images/correct.png')
        self.wrong_img = PhotoImage(file='images/wrong.png')
        true_img = PhotoImage(file='images/like_btn.png')
        false_img = PhotoImage(file='images/unlike_btn.png')

        self.canvas = Canvas(width=700, height=500, highlightthickness=0)
        self.card = self.canvas.create_image(350, 250, image=self.card_img)
        self.card_num = self.canvas.create_text(345, 150, text='', font=FONT_TITLE)
        self.card_title = self.canvas.create_text(345, 200, text='Science: Computer', font=FONT_SUBTITLE)
        self.card_text = self.canvas.create_text(345, 300, text='', font=FONT_TEXT, width=500)
        self.canvas.grid(row=1, column=0, columnspan=2)

        self.true_btn = Button(image=true_img, highlightthickness=0, borderwidth=0, command=self.check_true)
        self.false_btn = Button(image=false_img, highlightthickness=0, borderwidth=0, command=self.check_false)
        self.true_btn.grid(row=2, column=1)
        self.false_btn.grid(row=2, column=0)

        self.next_question()
        self.window.mainloop()

    def next_question(self):
        q_num, q_text = self.quiz.next_question()
        if not q_num and not q_text:
            messagebox.showinfo(title='Completed',
                                message='Congratulations! You have completed the quiz.\n'
                                        f'You final score: {self.quiz.score}')
            self.window.destroy()
            return
        self.set_button('normal')
        self.change_color('black')
        self.canvas.itemconfig(self.card, image=self.card_img)
        self.canvas.itemconfig(self.card_num, text=q_num)
        self.canvas.itemconfig(self.card_text, text=q_text)

    def check_true(self):
        self.feedback(self.quiz.check_answer('True'))

    def check_false(self):
        self.feedback(self.quiz.check_answer('True'))

    def feedback(self, correct):
        if correct:
            self.canvas.itemconfig(self.card, image=self.correct_img)
            self.score.config(text=f'Score: {self.quiz.score}')
        else:
            self.canvas.itemconfig(self.card, image=self.wrong_img)
        self.change_color('white')
        self.set_button('disabled')
        self.window.after(1000, self.next_question)

    def change_color(self, color):
        self.canvas.itemconfig(self.card_num, fill=color)
        self.canvas.itemconfig(self.card_text, fill=color)
        self.canvas.itemconfig(self.card_title, fill=color)

    def set_button(self, state):
        self.true_btn.config(state=state)
        self.false_btn.config(state=state)

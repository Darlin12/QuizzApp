from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()

        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, pady=20, padx=20)

        self.score = Label(text=f"score: 0", background=THEME_COLOR)
        self.score.grid(row=1, column=2)

        self.canva = Canvas(width=300, height=250)
        self.canva.grid(row=2, column=1, columnspan=2, pady=50, padx=25)
        self.label_canva = self.canva.create_text(150, 125, width=270,
                                                  text=self.quiz.next_question(),
                                                  fill=THEME_COLOR,
                                                  font=("Arial", 20, "italic")
                                                  )
        self.true_img = PhotoImage(file='./images/true.png')
        self.true_btn = Button(image=self.true_img, padx=10, pady=5, command=self.right)
        self.true_btn.grid(row=3, column=1)

        self.false_img = PhotoImage(file='./images/false.png')
        self.false_btn = Button(image=self.false_img, padx=10, pady=5, command=self.false)
        self.false_btn.grid(row=3, column=2)

        self.window.mainloop()

    def get_next_question(self):
        self.canva.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=self.quiz.score)
            q_text = self.quiz.next_question()
            self.canva.itemconfig(self.label_canva, text=q_text)
        else:
            self.canva.itemconfig(self.label_canva, text="You reached the end of the quiz")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")



    def right(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canva.config(bg="green")
        else:
            self.canva.config(bg="red")
        self.window.after(1000, self.get_next_question)







from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface():

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Setting up the canvas
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, fill=THEME_COLOR, text="Question", font=FONT)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        # Buttons
        false_button = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button, bg=THEME_COLOR, highlightthickness= 0,
                                   command = self.guess_is_false)
        self.false_button.grid(row=2,column=1)
        right_button = PhotoImage(file="images/true.png")
        self.true_button = Button(image=right_button,bg=THEME_COLOR, highlightthickness= 0,
                                  command = self.guess_is_true)
        self.true_button.grid(row=2,column=0)
        self.score_label= Label(bg=THEME_COLOR, fg="white", font=(35))
        self.score_label.grid(row=0,column=1)


        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def guess_is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def guess_is_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


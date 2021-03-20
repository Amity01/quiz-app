from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class App_interface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(bg=THEME_COLOR)
        self.window.title("Quiz App")
        self.score = 0
        self.score_label = Label(text=f"Score: {self.score}", font=('Arial', 24), bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, pady=10)

        self.canvas = Canvas(width=400, height=400)
        self.question_text = self.canvas.create_text(200, 200, width=380, text="Question1", font=("Italic", 24), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=50, pady=30)

        right_image = PhotoImage(file="images/true.png")
        self.true_button = Button(width=80, height=80, image=right_image, bd=0,command=self.is_true)
        self.true_button.grid(row=2, column=0)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(width=80, height=80, image=wrong_image, bd=0, command=self.is_false)
        self.wrong_button.grid(row=2, column=1, pady=20)
        self.show_next_question()
        self.window.mainloop()

    def show_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.score}')
            self.canvas.itemconfig(self.question_text,text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
    def is_true(self):
        answer = self.quiz.question_list[self.quiz.question_number-1].answer
        if answer == 'True':
            self.score += 1
            self.canvas.config(bg ="green")
        else:
            self.canvas.config(bg="red")
        print(answer)
        self.window.after(1000,self.show_next_question)


    def is_false(self):
        answer = self.quiz.question_list[self.quiz.question_number-1].answer
        if answer =='False':
            self.score += 1
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.show_next_question)
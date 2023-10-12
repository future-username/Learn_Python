from tkinter import *
from tkinter.ttk import *


def check_answers():
    true_answers = []
    win_positions = 0
    lose_positions = 0
    for index_question, question_answers in enumerate(questions):
        for index_line, text_item in enumerate(question_answers):
            if '+' in text_item:
                true_answers.append(index_line)
    for index, user_answer in enumerate(value_answer):
        if user_answer.get() == true_answers[index]:
            win_positions += 1
        else:
            lose_positions += 1
    label.config(text=f'Correct:{win_positions}\tWrong:{lose_positions}'.expandtabs(38))


root = Tk()

button_check = Button(text='Check', command=check_answers)
button_check.pack(side=TOP)
label = Label()
label.pack(side=TOP)
questions = []
question = []
for text in open('questions.txt'):
    text = text.replace('-', '').strip()
    if text[:1].isdigit():
        question = []
        questions.append(question)
    if text:
        question.append(text)

value_answer = []
for number_question, lines in enumerate(questions):
    choose_value = IntVar()
    for number_line, line in enumerate(lines):
        line = line.replace('+', '').strip()
        if number_question != 0 and line[:1].isdigit():
            Label().pack(anchor=W)
        if line[:1].isdigit():
            Label(text=line).pack(anchor=W)
        else:
            user_answers = Radiobutton(text=line, variable=choose_value, value=number_line)
            user_answers.pack(side=TOP, fill=X)
    value_answer.append(choose_value)

root.mainloop()
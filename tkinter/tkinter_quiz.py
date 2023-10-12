# from tkinter import *
# from tkinter.ttk import *
#
#
# def ask_question(el):
#     for widget in el.winfo_children():
#         widget.destroy()
#     Label(el, text="Здесь могла быть Ваша реклама! \n Или вопрос с вариантами ответов.").pack()
#
#
# def first_screen(el):
#     Label(el, text='Welcome to my quiz!\n Press "Start" to continue...').pack()
#     Button(el, text="Start", command=lambda e=el: ask_question(e)).pack()
#
#
# root = Tk()
#
# frm = LabelFrame(text="Generate screen")
# frm.pack()
#
# first_screen(frm)
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
# answers = []
#
# quiz = ["Which widgets using to display text with the ability to edit it?",
#         "Canvas",
#         "Listbox",
#         "Entry",
#         "Text",
#         "Label",
#         "10110"]
#
#
# def result_text(el):
#     for widget in el.winfo_children():
#         widget.destroy()
#     points = check()
#     Label(el, text=f'Ваш результат: {points} балла').pack()
#     Button(el, text="Try again", command=lambda e=el: ask_question(e)).pack()
#
#
# def check():
#     points = 0
#     for t, a in zip(quiz[-1], answers):
#         if bool(int(t)) and bool(int(t)) == a.get():
#             points += 1
#         elif bool(int(t)) != a.get():
#             points -= 1
#     return points
#
#
# def ask_question(el):
#     for widget in el.winfo_children():
#         widget.destroy()
#     Label(el, text=quiz[0]).pack()
#     for index, element in enumerate(quiz[:-1]):
#         if index > 0:
#             answers.append(BooleanVar())
#             Checkbutton(el, text=element, variable=answers[index - 1], onvalue=1, offvalue=0).pack(anchor=W)
#     Button(el, text="Next >>", command=lambda e=el: result_text(e)).pack()
#
#
# def first_screen(el):
#     Label(el, text='Welcome to my quiz!\n Press "Start" to continue...').pack()
#     Button(el, text="Start", command=lambda e=el: ask_question(e)).pack()
#
#
# root = Tk()
#
# frm = LabelFrame(text="Generate screen")
# frm.pack()
#
# first_screen(frm)
#
# root.mainloop()


from tkinter import *
from tkinter.ttk import *
import random

answers = []

quiz = [
    {'question': 'What widgets using for positioning other widgets?',
     'answers': ['0Button', '0Radiobutton', '1Frame', '0Text', '1LabelFrame']},
    {'question': '2+2=',
     'answers': ['00', '01', '02', '14']},
    {'question': '1+2=',
     'answers': ['00', '01', '02', '13', '09', '07', '05']},
]


def result_text(el):
    for widget in el.winfo_children():
        widget.destroy()
    points = check()
    Label(el, text=f'Ваш результат: {points} балла').pack()
    Button(el, text="Try again", command=lambda e=el: first_screen(e)).pack()


def check():
    points = 0
    start = 0
    end = 0
    for element in quiz:
        if end != 0:
            start = end
        end += len(element['answers'])
        answer_get = any(i.get() for i in answers[start:end])
        for t, a in zip(element['answers'], answers[start:end]):
            if answer_get and bool(int(t[0])) == a.get():
                points += 1
            elif answer_get and bool(int(t[0])) != a.get():
                points -= 1
    return points


def ask_question(el, iter_quiz):
    for widget in el.winfo_children():
        widget.destroy()
    current_question = next(iter_quiz)
    Label(el, text=current_question['question']).pack()
    random.shuffle(current_question['answers'])
    for index, answer in enumerate(current_question['answers']):
        variable = BooleanVar()
        answers.append(variable)
        Checkbutton(el, text=answer[1:], variable=variable, onvalue=1, offvalue=0).pack(anchor=W)

    if current_question != quiz[-1]:
        print(next(iter_quiz))
        Button(el, text="Previous <<", command=lambda e=el: ask_question(e, iter_quiz)).pack(side=LEFT)
        Button(el, text="Next >>", command=lambda e=el: ask_question(e, iter_quiz)).pack(side=RIGHT)
    else:
        Button(el, text="Previous <<", command=lambda e=el: result_text(e)).pack(side=LEFT)
        Button(el, text="Next >>", command=lambda e=el: result_text(e)).pack(side=RIGHT)


def first_screen(el):
    for widget in el.winfo_children():
        widget.destroy()
    iter_quiz = iter(quiz)
    Label(el, text='Welcome to my quiz!\n Press "Start" to continue...').pack()
    Button(el, text="Start", command=lambda e=el: ask_question(e, iter_quiz)).pack()


root = Tk()

frm = LabelFrame(text="Generate screen")
frm.pack()

first_screen(frm)

root.mainloop()

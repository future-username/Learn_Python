from tkinter import *
from tkinter.ttk import *
import random
from typing import Union


answers = []

iter_temp = []

quiz = [
    {'question': 'What widgets using for positioning other widgets?',
     'answers': ['0Button', '0Radiobutton', '1Frame', '0Text', '1LabelFrame']},
    {'question': '2+2=',
     'answers': ['00', '01', '02', '14']},
    {'question': '1+2=',
     'answers': ['00', '01', '02', '13', '09', '07', '05']},
]


def result_text(index: int):
    clean_screen(iter_temp[index])
    points = check()
    frame_result = Frame()
    frame_result.pack()
    Label(frame_result, text=f'Ваш результат: {points} балла').pack()
    button_command = lambda: (clean_screen(frame_result), frame_generate_screen.pack())
    Button(frame_result, text="Try again", command=button_command).pack()


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


def ask_question(index: int) -> None:
    index_previous = len(quiz) - 1 if index == 0 else index - 1
    index_current = index
    index_next = index + 1 if index < len(quiz) - 1 else 0

    iter_temp[index_previous].pack_forget()
    iter_temp[index_next].pack_forget()
    iter_temp[index_current].pack()
    button_frame = iter_temp[index].children['!frame'].children
    button_previous = button_frame['!button']
    button_finish = button_frame['!button2']
    button_next = button_frame['!button3']

    button_previous.config(text="Previous <<", command=lambda: ask_question(index_previous))
    button_finish.config(text="Finish test", command=lambda: result_text(index_current))
    button_next.config(text="Next >>", command=lambda: ask_question(index_next))


def clean_screen(element: Union[LabelFrame, Frame]) -> None:
    element.pack_forget()


def first_screen() -> None:
    Label(frame_generate_screen, text='Welcome to my quiz!\n Press "Start" to continue...').pack()
    command_button = lambda: (clean_screen(frame_generate_screen), ask_question(0))
    Button(frame_generate_screen, text="Start", command=command_button).pack()


def generate_quiz() -> None:
    for current_question in quiz:
        frame = LabelFrame(text=current_question['question'])
        random.shuffle(current_question['answers'])
        for index, answer in enumerate(current_question['answers']):
            variable = BooleanVar()
            answers.append(variable)
            Checkbutton(frame, text=answer[1:], variable=variable, onvalue=1, offvalue=0).pack(anchor=W)

        frame_button = Frame(frame)
        frame_button.pack(side=BOTTOM)
        button_previous = Button(frame_button, text="Previous <<")
        button_previous.pack(side=LEFT)

        button_finish = Button(frame_button, text="Finish test")
        button_finish.pack(side=LEFT)

        button_next = Button(frame_button, text="Next >>")
        button_next.pack(side=LEFT)

        iter_temp.append(frame)


root = Tk()

frame_generate_screen = LabelFrame(text="Generate screen")
frame_generate_screen.pack()
generate_quiz()
first_screen()

root.mainloop()

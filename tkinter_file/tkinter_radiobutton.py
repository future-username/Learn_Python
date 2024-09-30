# from tkinter import *
# from tkinter.ttk import *
#
# root = Tk()
#
# Radiobutton(text='The first').pack(anchor=W)
# Radiobutton(text='The second').pack(anchor=W)
# Radiobutton(text='The third').pack(anchor=W)
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
# root = Tk()
#
# rb_var = BooleanVar()
# rb_var.set(0)
# Radiobutton(text='The first', variable=rb_var, value=0).pack(anchor=W)
# Radiobutton(text='The second', variable=rb_var, value=1).pack(anchor=W)
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def print_console():
#     print(rb_var.get())
#
#
# root = Tk()
# rb_var = StringVar()
# Radiobutton(text='The first', variable=rb_var, value='Clicked 1', command=print_console).pack(anchor=W)
# Radiobutton(text='The second', variable=rb_var, value='Clicked 2', command=print_console).pack(anchor=W)
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def print_console():
#     print(rb_var.get())
#
#
# root = Tk()
# rb_var = IntVar()
# Radiobutton(text='The first', variable=rb_var, value=1, command=print_console).pack(anchor=W)
# Radiobutton(text='The second', variable=rb_var, value=2, command=print_console).pack(anchor=W)
# Radiobutton(text='The Third', variable=rb_var, value=3, command=print_console).pack(anchor=W)
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def print_console():
#     print(rb_var.get())
#
#
# root = Tk()
# rb_var = StringVar()
# Label = Label(root, text="Is the capital of China?")
# Label.pack()
# Radiobutton(text='Beijing', variable=rb_var, value="Beijing", command=print_console).pack(anchor=W)
# Radiobutton(text='Hong Kong', variable=rb_var, value="Hong Kong", command=print_console).pack(anchor=W)
# Radiobutton(text='Tokyo', variable=rb_var, value="Tokyo", command=print_console).pack(anchor=W)
# Radiobutton(text='Taipei', variable=rb_var, value="Taipei", command=print_console).pack(anchor=W)
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def check_answer():
#     if rb_var.get() == 0:
#         label_value.set('You are wrong. :(')
#     elif rb_var.get() == 1:
#         label_value.set('True!!!')
#     elif rb_var.get() == 2:
#         label_value.set('You are kidding. ;)')
#
#
# root = Tk()
#
# Label(text='How to translate: "The current window?"').pack()
#
# rb_var = IntVar()
# rb_var.set(0)
# Radiobutton(text="Правильное окно", variable=rb_var, value=1).pack()
# Radiobutton(text="Текущее окно", variable=rb_var, value=2).pack()
# Radiobutton(text="Летящее окно", variable=rb_var, value=3).pack()
# button = Button(text="Check", command=check_answer).pack()
#
# label_value = StringVar()
# label_value.set("Choose an answer!")
# Label(textvariable=label_value).pack()
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def check_answer():
#     if rb_var.get() == 0:
#         label_value.set('You are wrong. :(')
#     elif rb_var.get() == 1:
#         label_value.set('Chosen 1 radiobutton')
#     elif rb_var.get() == 2:
#         label_value.set('Chosen 2 radiobutton')
#     elif rb_var.get() == 3:
#         label_value.set('Chosen 3 radiobutton')
#     elif rb_var.get() == 4:
#         label_value.set('Chosen 4 radiobutton)')
#
#
# root = Tk()
#
# Label(text='Look at the working program"').pack()
#
# rb_var = IntVar()
# rb_var.set(0)
# Radiobutton(text="the first", variable=rb_var, value=1, command=check_answer).pack()
# Radiobutton(text="the second", variable=rb_var, value=2, command=check_answer).pack()
# Radiobutton(text="the third", variable=rb_var, value=3, command=check_answer).pack()
# Radiobutton(text="the fourth", variable=rb_var, value=4, command=check_answer).pack()
#
# label_value = StringVar()
# label_value.set('radiobutton still not choose')
# Label(textvariable=label_value).pack()
#
# root.mainloop()
#
#
# from tkinter import *
# from tkinter.ttk import *
#
#
# def check_answer():
#     if rb_var.get() == 0:
#         label_value.set('You are wrong. :(')
#     elif rb_var.get() == 1:
#         label_value.set('+5(921)234-56-78')
#     elif rb_var.get() == 2:
#         label_value.set('+5(941)234-56-78')
#     elif rb_var.get() == 3:
#         label_value.set('+5(928)234-56-78')
#
#
# root = Tk()
#
# Label(text='Choose name for show the cellphone number.').grid(column=0, row=0, columnspan=2)
#
# rb_var = IntVar()
# rb_var.set(0)
# Radiobutton(text="Pit", variable=rb_var, value=1, command=check_answer).grid(column=0, row=1, sticky=NSEW)
# Radiobutton(text="Ann", variable=rb_var, value=2, command=check_answer).grid(column=0, row=2, sticky=NSEW)
# Radiobutton(text="Bob", variable=rb_var, value=3, command=check_answer).grid(column=0, row=3, sticky=NSEW)
#
# label_value = StringVar()
# label_value.set('')
# Label(textvariable=label_value).grid(column=1, row=2, sticky=NSEW)
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def check_answer():
#     label_value.set(rb_var.get())
#
#
# root = Tk()
#
# Label(text='Choose name for show the cellphone number.').grid(column=0, row=0, columnspan=2)
#
# rb_var = StringVar()
# Radiobutton(text="Pit", variable=rb_var, value="+5(921)234-56-78",
# command=check_answer).grid(column=0, row=1, sticky=NSEW)
# Radiobutton(text="Ann", variable=rb_var, value="+5(941)234-56-78",
# command=check_answer).grid(column=0, row=2, sticky=NSEW)
# Radiobutton(text="Bob", variable=rb_var, value="+5(928)234-56-78",
# command=check_answer).grid(column=0, row=3, sticky=NSEW)
#
# label_value = StringVar()
# Label(textvariable=label_value).grid(column=1, row=2, sticky=NSEW)
#
# root.mainloop()


from tkinter import *
from tkinter.ttk import *


def check_answer():
    check_entry = entry.get()
    if choose_value.get() == 3 and check_entry.lower().strip() == "правильно":
        label_value.set('Правильно!')
    else:
        label_value.set('Ошибка;(')


root = Tk()

Label(text='Выберите верный вариант написания слов в русском языке').pack()
choose_value = IntVar()
Radiobutton(text="пастолку, пастольку", variable=choose_value, value=1).pack(side=TOP, fill=X)
Radiobutton(text="вилька, тарелька", variable=choose_value, value=2).pack(side=TOP, fill=X)
frame = Frame()
frame.pack(fill=X)
Radiobutton(frame, text="ваша версия:", variable=choose_value, value=3).pack(side=LEFT, fill=X)
entry = Entry(frame)
entry.pack(side=LEFT, fill=X)
Button(text="Проверить", command=check_answer).pack()
label_value = StringVar()
Label(textvariable=label_value).pack()

root.mainloop()

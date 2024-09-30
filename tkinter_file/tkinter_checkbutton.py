# from tkinter import *
# from tkinter.ttk import *
#
# root = Tk()
#
# ch_var1 = BooleanVar()
# ch_var1.set(0)
# Checkbutton(text="First", variable=ch_var1, onvalue=1, offvalue=0).pack(anchor=W)
#
# ch_var2 = BooleanVar()
# ch_var2.set(0)
# Checkbutton(text="Second", variable=ch_var2, onvalue=1, offvalue=0).pack(anchor=W)
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def print_value():
#     print("First: {}".format(ch_var1.get()))
#     print("Second: {}".format(ch_var2.get()))
#
#
# root = Tk()
#
# ch_var1 = BooleanVar()
# ch_var1.set(0)
# Checkbutton(text="First", variable=ch_var1, onvalue=1, offvalue=0, command=print_value).pack(anchor=W)
#
# ch_var2 = BooleanVar()
# ch_var2.set(0)
# Checkbutton(text="Second", variable=ch_var2, onvalue=1, offvalue=0, command=print_value).pack(anchor=W)
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def print_value():
#     print("First: {}".format(ch_var1.get()))
#     print("Second: {}".format(ch_var2.get()))
#     print("Third: {}".format(ch_var3.get()))
#
#
# root = Tk()
#
# ch_var1 = BooleanVar()
# ch_var1.set(0)
# Checkbutton(text="First", variable=ch_var1, onvalue=1, offvalue=0, command=print_value).pack(anchor=W)
#
# ch_var2 = IntVar()
# ch_var2.set(0)
# Checkbutton(text="Second", variable=ch_var2, onvalue=5, offvalue=-5, command=print_value).pack(anchor=W)
#
# ch_var3 = StringVar()
# ch_var3.set("")
# Checkbutton(text="Third", variable=ch_var3, onvalue="выбран", offvalue="не выбран", command=print_value).pack(anchor=W)
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def check_answer():
#     first = choose_value_1.get()
#     second = choose_value_2.get()
#     third = choose_value_3.get()
#     fourth = choose_value_4.get()
#     if second:
#         label.config(text="ошибка")
#     elif first and third and fourth:
#         label.config(text="Верно")
#     else:
#         label.config(text="ответ не полный")
#
#
# root = Tk()
#
# Label(text='Сколько будет 1 + 1 =').pack()
# choose_value_1 = IntVar()
# Checkbutton(text="11, для строчного типа данных",
#             variable=choose_value_1, onvalue=1, offvalue=0).pack(side=TOP, fill=X)
# choose_value_2 = IntVar()
# Checkbutton(text="5, цена с надбавкой для рыночной экономики",
#             variable=choose_value_2, onvalue=1, offvalue=0).pack(side=TOP, fill=X)
# choose_value_3 = IntVar()
# Checkbutton(text="10, для чисел двоичной системы счисления",
#             variable=choose_value_3, onvalue=1, offvalue=0).pack(side=TOP, fill=X)
# choose_value_4 = IntVar()
# Checkbutton(text="2, для чисел троичной системы счисления и выше",
#             variable=choose_value_4, onvalue=1, offvalue=0).pack(side=TOP, fill=X)
# Button(text="Проверить", command=check_answer).pack(side=TOP)
# label = Label(text="Выберите ответы, которые считаете верными")
# label.pack(side=TOP)
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def print_colours():
#     text.delete(1.0, END)
#     text.insert(END, black_value.get())
#     if black_value.get() and green_value.get():
#         text.insert(END, ", ")
#     text.insert(END, green_value.get())
#     # if green_value.get() and blue_value.get() or black_value.get() and blue_value.get():
#     if blue_value.get() and (black_value.get() or green_value.get()):
#         text.insert(END, ", ")
#     text.insert(END, blue_value.get())
#     if red_value.get() and (black_value.get() or green_value.get() or blue_value.get()):
#         text.insert(END, ", ")
#     text.insert(END, red_value.get())
#     if white_value.get() and (black_value.get() or green_value.get() or blue_value.get() or red_value.get()):
#         text.insert(END, ", ")
#     # if not white_value.get() and not black_value.get() and not green_value.get() and not blue_value.get()\
#     #         and not red_value.get():
#     if not (white_value.get() or black_value.get() or green_value.get() or blue_value.get() or red_value.get()):
#         text.insert(END, "Please choose the color")
#     text.insert(END, white_value.get())
#     text.insert(END, ".")
#
#
# root = Tk()
#
# left_frame = Frame()
# left_frame.pack(side=LEFT)
# black_value = StringVar()
# Checkbutton(left_frame, text="black", variable=black_value, onvalue="black", offvalue="").pack(fill=X)
# green_value = StringVar()
# Checkbutton(left_frame, text="green", variable=green_value, onvalue="green", offvalue="").pack(fill=X)
# blue_value = StringVar()
# Checkbutton(left_frame, text="blue", variable=blue_value, onvalue="blue", offvalue="").pack(fill=X)
# red_value = StringVar()
# Checkbutton(left_frame, text="red", variable=red_value, onvalue="red", offvalue="").pack(fill=X)
# white_value = StringVar()
# Checkbutton(left_frame, text="white", variable=white_value, onvalue="white", offvalue="").pack(fill=X)
# Button(left_frame, text="Print", command=print_colours).pack(side=TOP)
# text = Text(width=40, height=20)
# text.pack(side=RIGHT, fill=BOTH, expand=1)
#
# root.mainloop()


from tkinter import *
from tkinter.ttk import *


def check_answer():
    check_entry = entry.get()
    # if third_value.get() and check_entry.lower().strip() == "7" or third_value.get()\
    #         and check_entry.lower().strip() == "8":
    #
    if third_value.get() and (check_entry.lower().strip() == "7" or check_entry.lower().strip() == "8"):
        label.config(text='Правильно!')
    else:
        label.config(text='Ошибка;(')


root = Tk()

Label(text="Идет урок в грузинской школе.\n Учитель спрашивает: 'сколко будэт: 2+2 ?'").pack()
first_value = IntVar()
Checkbutton(text="3", variable=first_value, onvalue=1, offvalue=0).pack(side=TOP, fill=X)
second_value = IntVar()
Checkbutton(text="5", variable=second_value, onvalue=1, offvalue=0).pack(side=TOP, fill=X)
fourth_value = IntVar()
Checkbutton(text="4", variable=fourth_value, onvalue=1, offvalue=0).pack(side=TOP, fill=X)
frame = Frame()
frame.pack(fill=X)
third_value = IntVar()
Checkbutton(frame, text="ваша версия:", variable=third_value, onvalue=1, offvalue=0).pack(side=LEFT, fill=X)
entry = Entry(frame)
entry.pack(side=LEFT, fill=X)
Button(text="Проверить", command=check_answer).pack()
label = Label(text="Выберите ответы, которые считаете верными")
label.pack()

root.mainloop()

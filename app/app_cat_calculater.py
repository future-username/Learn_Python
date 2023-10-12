from tkinter import *
from tkinter.ttk import *


def set_first():
    # print("Called the first function!")
    # print(num12.get())
    entry_15.delete(0, END)
    field_1 = len(num12.get().split(".")) == 2 and num12.get().split(".")[0].isdigit()\
              and num12.get().split(".")[1].isdigit() or num12.get().isdigit()

    field_2 = len(entry_13.get().split(".")) == 2 and entry_13.get().split(".")[0].isdigit() and\
              entry_13.get().split(".")[1].isdigit() or entry_13.get().isdigit()

    field_3 = len(entry_14.get().split(".")) == 2 and entry_14.get().split(".")[0].isdigit()\
              and entry_14.get().split(".")[1].isdigit() or entry_14.get().isdigit()

    if field_1 and field_2 and field_3:
        entry_15.insert(0, float(num12.get()) * float(entry_13.get()) / float(entry_14.get()))
    else:
        entry_15.insert(END, 0)


def set_second():
    entry_25.delete(0, END)
    field_1 = len(entry_22.get().split(".")) == 2 and entry_22.get().split(".")[0].isdigit() \
              and entry_22.get().split(".")[1].isdigit() or entry_22.get().isdigit()

    field_2 = len(entry_23.get().split(".")) == 2 and entry_23.get().split(".")[0].isdigit() and \
              entry_23.get().split(".")[1].isdigit() or entry_23.get().isdigit()

    field_3 = len(entry_24.get().split(".")) == 2 and entry_24.get().split(".")[0].isdigit() \
              and entry_24.get().split(".")[1].isdigit() or entry_24.get().isdigit()

    if field_1 and field_2 and field_3:
        entry_25.insert(0, float(entry_22.get()) * float(entry_23.get()) / float(entry_24.get()))
    else:
        entry_25.insert(END, 0)


def set_third():
    entry_35.delete(0, END)
    field_1 = len(entry_32.get().split(".")) == 2 and entry_32.get().split(".")[0].isdigit() \
              and entry_32.get().split(".")[1].isdigit() or entry_32.get().isdigit()

    field_2 = len(entry_33.get().split(".")) == 2 and entry_33.get().split(".")[0].isdigit() and \
              entry_33.get().split(".")[1].isdigit() or entry_33.get().isdigit()

    field_3 = len(entry_34.get().split(".")) == 2 and entry_34.get().split(".")[0].isdigit() \
              and entry_34.get().split(".")[1].isdigit() or entry_34.get().isdigit()

    if field_1 and field_2 and field_3:
        entry_35.insert(0, float(entry_32.get()) * float(entry_33.get()) / float(entry_34.get()))
    else:
        entry_35.insert(END, 0)


def set_forth():
    set_first()
    set_second()
    set_third()
    entry_for_year.delete(0, END)
    field_1 = len(entry_15.get().split(".")) == 2 and entry_15.get().split(".")[0].isdigit() \
              and entry_15.get().split(".")[1].isdigit() or entry_15.get().isdigit()

    field_2 = len(entry_25.get().split(".")) == 2 and entry_25.get().split(".")[0].isdigit() and \
              entry_25.get().split(".")[1].isdigit() or entry_25.get().isdigit()

    field_3 = len(entry_35.get().split(".")) == 2 and entry_35.get().split(".")[0].isdigit() \
              and entry_35.get().split(".")[1].isdigit() or entry_35.get().isdigit()

    if field_1 and field_2 and field_3:
        entry_for_year.insert(0, float(entry_15.get()) + float(entry_25.get()) + float(entry_35.get()) * 365)
    else:
        entry_for_year.insert(END, 0)


def set_fifth():
    set_forth()
    entry_all_years.delete(0, END)

    field_1 = len(entry_for_year.get().split(".")) == 2 and entry_for_year.get().split(".")[0].isdigit() \
              and entry_for_year.get().split(".")[1].isdigit() or entry_for_year.get().isdigit()

    field_2 = len(entry_years.get().split(".")) == 2 and entry_years.get().split(".")[0].isdigit() \
              and entry_years.get().split(".")[1].isdigit() or entry_years.get().isdigit()

    if field_1 and field_2:
        entry_all_years.insert(0, float(entry_for_year.get()) * float(entry_years.get()))
    else:
        entry_all_years.insert(END, 0)


root = Tk()

root.title('Calculator for cat')

Label(text="Товар").grid(column=0, row=0)
Label(text="Кол-во ед.").grid(column=1, row=0)
Label(text="Цены за ед.").grid(column=2, row=0)
Label(text="Кол-во дней").grid(column=3, row=0)
Label(text="Общая цена").grid(column=5, row=0)

entry_11 = Entry()
entry_11.grid(column=0, row=1)
num12 = StringVar()
num12.set(5)
entry_12 = Entry(textvariable=num12)
entry_12.grid(column=1, row=1)
entry_13 = Entry()
entry_13.insert(0, 3)
entry_13.grid(column=2, row=1)
entry_14 = Entry()
entry_14.insert(0, 4)
entry_14.grid(column=3, row=1)
Button(text="=", command=set_first).grid(column=4, row=1)
entry_15 = Entry()
entry_15.insert(0, 0)
entry_15.grid(column=5, row=1)

entry_21 = Entry()
entry_21.grid(column=0, row=2)
entry_22 = Entry()
entry_22.insert(0, 5)
entry_22.grid(column=1, row=2)
entry_23 = Entry()
entry_23.insert(0, 3)
entry_23.grid(column=2, row=2)
entry_24 = Entry()
entry_24.insert(0, 4)
entry_24.grid(column=3, row=2)
Button(text="=", command=set_second).grid(column=4, row=2)
entry_25 = Entry()
entry_25.insert(0, 0)
entry_25.grid(column=5, row=2)

entry_31 = Entry()
entry_31.grid(column=0, row=3)
entry_32 = Entry()
entry_32.insert(0, 5)
entry_32.grid(column=1, row=3)
entry_33 = Entry()
entry_33.insert(0, 3)
entry_33.grid(column=2, row=3)
entry_34 = Entry()
entry_34.insert(0, 4)
entry_34.grid(column=3, row=3)
Button(text="=", command=set_third).grid(column=4, row=3)
entry_35 = Entry()
entry_35.insert(0, 0)
entry_35.grid(column=5, row=3)

Label(text="Всего затраты за год", justify=RIGHT).grid(column=0, row=4, columnspan=4)
button_6 = Button(text="=", command=set_forth)
button_6.grid(column=4, row=4)
entry_for_year = Entry()
entry_for_year.grid(column=5, row=4)

Label(text="Количество лет", justify=RIGHT).grid(column=0, row=5, columnspan=4)
entry_years = Entry()
entry_years.insert(0, 10)
entry_years.grid(column=5, row=5)

Label(text="Общее содержание за все годы", justify=RIGHT).grid(column=0, row=6, columnspan=4)
button_6 = Button(text="Итого", command=set_fifth)
button_6.grid(column=4, row=6)
entry_all_years = Entry()
entry_all_years.grid(column=5, row=6)


root.mainloop()


# from tkinter import *
#
#
# interface_config = [
#     ['Label, Товар, 1', 'Label, Кол-во ед., 1', 'Label, Цены за ед., 1', 'Label, Кол-во дней, 1', '',
#      'Label, Общая цена, 1'],
#     ['Entry', 'Entry', 'Entry', 'Entry', 'Button, =', 'Entry'],
#     ['Entry', 'Entry', 'Entry', 'Entry', 'Button, =', 'Entry'],
#     ['Entry', 'Entry', 'Entry', 'Entry', 'Button, =', 'Entry'],
#     ['Label, Всего затраты за год, 4', '', '', '', 'Button, =', 'Entry'],
#     ['Label, Количество лет, 4', '', '', '', '', 'Entry'],
#     ['Label, Общее содержание за все годы, 4', '', '', '', 'Button, Итого', 'Entry']
# ]
# root = Tk()
# root.title('Calculator for cat')
#
# for y in range(len(interface_config)):
#     for x in range(len(interface_config[y])):
#         if interface_config[y][x] and interface_config[y][x].split(sep=",")[0] == 'Label':
#             Label(text=interface_config[y][x].split(sep=",")[1],
#                   fg="black").grid(column=x, row=y, columnspan=interface_config[y][x].split(sep=",")[2], sticky=NSEW)
#         if interface_config[y][x] and interface_config[y][x].split(sep=",")[0] == 'Button':
#             Button(text=interface_config[y][x].split(sep=",")[1], fg="black").grid(column=x, row=y, sticky=NSEW)
#         if interface_config[y][x] and interface_config[y][x].split(sep=",")[0] == 'Entry':
#             Entry(bg="white").grid(column=x, row=y, sticky=NSEW)
#
# root.mainloop()


from tkinter import *


interface_config = [
    ['Label, Товар, 1', 'Label, Кол-во ед., 1', 'Label, Цены за ед., 1', 'Label, Кол-во дней, 1', '',
     'Label, Общая цена, 1'],
    ['Entry', 'Entry', 'Entry', 'Entry', 'Button, =', 'Entry'],
    ['Entry', 'Entry', 'Entry', 'Entry', 'Button, =', 'Entry'],
    ['Entry', 'Entry', 'Entry', 'Entry', 'Button, =', 'Entry'],
    ['Label, Всего затраты за год, 4', '', '', '', 'Button, =', 'Entry'],
    ['Label, Количество лет, 4', '', '', '', '', 'Entry'],
    ['Label, Общее содержание за все годы, 4', '', '', '', 'Button, Итого', 'Entry']
]
root = Tk()
root.title('Calculator for cat')

for y, buttons in enumerate(interface_config):
    for x, text in enumerate(buttons):
        if text and text.split(sep=",")[0] == 'Label':
            Label(text=text.split(sep=",")[1],
                  fg="black").grid(column=x, row=y, columnspan=text.split(sep=",")[2], sticky=NSEW)
        if text and text.split(sep=",")[0] == 'Button':
            Button(text=text.split(sep=",")[1], fg="black").grid(column=x, row=y, sticky=NSEW)
        if text and text.split(sep=",")[0] == 'Entry':
            Entry(bg="white").grid(column=x, row=y, sticky=NSEW)

root.mainloop()



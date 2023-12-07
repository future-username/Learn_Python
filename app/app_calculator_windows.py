# from tkinter import *
#
# button_texts = ["MC", "MR", "MS", "M+", "M-", "<-", "CE", "C", '±', '√', 7, 8, 9, "/", "%", 4, 5, 6, "*", "1/x", 1, 2,
#                 3, "-", '=', 0, "", '.', "+"]
# root = Tk()
#
# root.title("Calculator")
# label_entry = Entry(justify=RIGHT)
# label_entry.grid(column=0, row=0, columnspan=5, sticky=NSEW)
# label_entry.insert(END, 0)
#
# for i in range(len(button_texts)):
#     if button_texts[i] == "=":
#         Button(text="=", fg="black").grid(column=i % 5, row=i // 5 + 1, rowspan=2, sticky=NSEW)
#     elif button_texts[i] == 0:
#         Button(text=0, fg="black").grid(column=i % 5, row=i // 5 + 1, columnspan=2, sticky=NSEW)
#     elif button_texts[i]:
#         Button(text=button_texts[i], fg="black").grid(column=i % 5, row=i // 5 + 1, sticky=NSEW)
#
# root.mainloop()


# from tkinter import *
#
# button_texts = [
#     ["MC", "MR", "MS", "M+", "M-"],
#     ["<-", "CE", "C", '±', '√'],
#     [7, 8, 9, "/", "%"],
#     [4, 5, 6, "*", "1/x"],
#     [1, 2, 3, "-", '='],
#     [0, "", '.', "+"]
# ]
# root = Tk()
#
# root.title("Calculator")
# label_entry = Entry(justify=RIGHT)
# label_entry.grid(column=0, row=0, columnspan=5, sticky=NSEW)
# label_entry.insert(END, 0)
#
# for y in range(len(button_texts)):
#     # print(y)
#     # print(button_texts[y])
#     for x in range(len(button_texts[y])):
#         if button_texts[y][x] == "=":
#             Button(text="=", fg="black").grid(column=x, row=y+1, rowspan=2, sticky=NSEW)
#         elif button_texts[y][x] == 0:
#             Button(text=0, fg="black").grid(column=x, row=y + 1, columnspan=2, sticky=NSEW)
#         elif button_texts[y][x]:
#             Button(text=button_texts[y][x], fg="black").grid(column=x, row=y + 1, sticky=NSEW)
#
# root.mainloop()


# from tkinter import *
#
# button_texts = [
#     ["MC 1 1", "MR 1 1", "MS 1 1", "M+ 1 1", "M- 1 1"],
#     ["<- 1 1", "CE 1 1", "C 1 1", '± 1 1', '√ 1 1'],
#     ["7 1 1", "8 1 1", "9 1 1", "/ 1 1", "% 1 1"],
#     ['4 1 1', '5 1 1', '6 1 1', "* 1 1", "1/x 1 1"],
#     ['1 1 1', '2 1 1', '3 1 1', "- 1 1", '= 1 2'],
#     ['0 2 1', "", '. 1 1', "+ 1 1"]
# ]
# root = Tk()
#
# root.title("Calculator")
# label_entry = Entry(justify=RIGHT)
# label_entry.grid(column=0, row=0, columnspan=5, sticky=NSEW)
# label_entry.insert(END, 0)
#
# for y in range(len(button_texts)):
#     # print(y)
#     # print(button_texts[y])
#     for x in range(len(button_texts[y])):
#         if button_texts[y][x]:
#             Button(text=button_texts[y][x].split()[0],
#                    fg="black").grid(column=x, row=y + 1, rowspan=button_texts[y][x].split()[2],
#                                     columnspan=button_texts[y][x].split()[1], sticky=NSEW)
#
# root.mainloop()


# from tkinter import *
#
# button_texts = [
#     ["MC 1 1", "MR 1 1", "MS 1 1", "M+ 1 1", "M- 1 1"],
#     ["<- 1 1", "CE 1 1", "C 1 1", '± 1 1', '√ 1 1'],
#     ["7 1 1", "8 1 1", "9 1 1", "/ 1 1", "% 1 1"],
#     ['4 1 1', '5 1 1', '6 1 1', "* 1 1", "1/x 1 1"],
#     ['1 1 1', '2 1 1', '3 1 1', "- 1 1", '= 1 2'],
#     ['0 2 1', "", '. 1 1', "+ 1 1"]
# ]
# root = Tk()
#
# root.title("Calculator")
# label_entry = Entry(justify=RIGHT)
# label_entry.grid(column=0, row=0, columnspan=5, sticky=NSEW)
# label_entry.insert(END, '0')
#
# for y, buttons in enumerate(button_texts):
#     for x, text in enumerate(buttons):
#         if text:
#             _ = Button(text=text.split()[0], fg='black')
#             _.grid(column=x, row=y+1, columnspan=text.split()[1], rowspan=text.split()[2], sticky=NSEW)
#
# root.mainloop()


from tkinter import *

button_texts = [
    # ["MC 1 1", "MR 1 1", "MS 1 1", "M+ 1 1", "M- 1 1"],
    # ["<- 1 1", "CE 1 1", "C 1 1", '± 1 1', '√ 1 1'],
    # ["7 1 1", "8 1 1", "9 1 1"],  # "/ 1 1"],  # "% 1 1"],
    # ['4 1 1', '5 1 1', '6 1 1'],  # "* 1 1"],  # "1/x 1 1"],
    # ['1 1 1', '2 1 1', '3 1 1', "- 1 1", '= 1 2'],
    # ['0 2 1', "", '. 1 1', "+ 1 1"]
    ['0 1 1', "1 1 1", "c 1 1", "+ 1 1"]
]


def clear():
    display_expression.delete(0, END)
    display_number.delete(0, END)
    display_expression.insert(END, '0')
    display_number.insert(END, '0')


def add_number_to_entry(value: str):
    if display_expression.get().strip() == '0':
        display_expression.delete(0, END)
        display_number.delete(0, END)
        display_expression.insert(END, value)
        display_number.insert(END, value)
    elif display_expression.get()[-1] == '0' and display_expression.get()[-2] in ('+', '-') and value != '0':
        number = f'{display_expression.get()[:-1]}{value}'
        display_expression.delete(0, END)
        display_expression.insert(END, number)
        display_number.delete(0, END)
        display_number.insert(END, value)

    elif display_expression.get()[-1] != '0':
        display_expression.insert(END, value)
        display_number.insert(END, value)


def add_sign_to_entry(value: str):
    if display_expression.get()[-1] not in ('+', '-', '='):
        display_expression.insert(END, value)
        display_number.delete(0, END)


def calculate():
    example = list(display_expression.get().strip())
    print(example)


def main(value: str):
    if value in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        add_number_to_entry(value)
    elif value in ('+', '-'):
        add_sign_to_entry(value)
    elif value in '=':
        calculate()
    elif value in 'c':
        clear()


root = Tk()

root.title("Calculator")
display_expression = Entry(justify=RIGHT)
display_expression.grid(column=0, row=0, columnspan=5, sticky=NSEW)
display_expression.insert(END, '0')

display_number = Entry(justify=RIGHT)
display_number.grid(column=0, row=1, columnspan=5, sticky=NSEW)
display_number.insert(END, '0')

for y, buttons in enumerate(button_texts):
    for x, text in enumerate(buttons):
        if text:
            _ = Button(text=text.split()[0], fg='black', command=lambda t=text.split()[0]: main(t))
            _.grid(column=x, row=y + 2, columnspan=text.split()[1], rowspan=text.split()[2], sticky=NSEW)

root.mainloop()

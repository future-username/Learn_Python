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
from operator import add, sub, mul, truediv, pow
import re

button_texts = [
    ["MC 1 1", "MR 1 1", "MS 1 1", "M+ 1 1", "M- 1 1"],
    ["<- 1 1", "CE 1 1", "C 1 1", '± 1 1', '√ 1 1'],
    ["7 1 1", "8 1 1", "9 1 1", "/ 1 1", "% 1 1"],
    ['4 1 1', '5 1 1', '6 1 1', "* 1 1", "1/x 1 1"],
    ['1 1 1', '2 1 1', '3 1 1', "- 1 1", '= 1 2'],
    ['0 2 1', "", '. 1 1', "+ 1 1"],
]

last_value = None
operators = {"+": add, "-": sub, "*": mul, "/": truediv, "^": pow}
precedence = {"+": 0, "-": 0, "*": 1, "/": 1, '^': 2}


def clear():
    display_expression.delete(0, END)
    display_number.delete(0, END)
    display_expression.insert(END, '0')
    display_number.insert(END, '0')


def add_number_to_entry(value: str):
    if display_expression.get().strip()[-1] in '=':
        display_expression.delete(0, END)
        display_number.delete(0, END)
    elif display_expression.get().strip()[-2:] in ('+0', '-0', '0'):
        display_expression.delete(len(display_expression.get()) - 1)
        display_number.delete(len(display_number.get()) - 1)
    display_expression.insert(END, value)
    display_number.insert(END, value)


def add_sign_to_entry(value: str):
    display_expression.insert(END, value)
    if display_expression.get().strip()[-2:] in ('+=', '-=', '/=', '*=', '=+', '=-', '=*', '=/', '=^'):
        display_expression.delete(len(display_expression.get()) - 2)
    elif display_expression.get().strip()[-2] in operators.keys():
        display_expression.delete(len(display_expression.get()) - 2)
    elif display_expression.get().strip()[-1] in '=':
        display_number.delete(len(display_number.get()) - 1)
    calculate()


def apply_op(op_stack, num_stack):
    op = op_stack.pop()
    num2, num1 = num_stack.pop(), num_stack.pop()
    num_stack.append(operators[op](num1, num2))


def calculate():
    example = display_expression.get().strip()
    if example[-1] in operators.keys():
        example = display_expression.get().strip()[:-1]
    num_stack, op_stack = [], []

    for token in re.findall(r"[+/*-]|\d+", example):
        if token in operators:
            while op_stack and op_stack[-1] in operators and precedence[token] <= precedence[op_stack[-1]]:
                apply_op(op_stack, num_stack)
            op_stack.append(token)
        else:
            num_stack.append(float(token))

    while op_stack:
        apply_op(op_stack, num_stack)

    display_number.delete(0, END)
    display_number.insert(0, str(num_stack[0]))


def get_example_as_list(example: str) -> list:
    result = []
    element = ''
    for char in example:
        if char in operators.keys():
            result.append(element)
            element = ''
            result.append(char)
        elif char != ' ':
            element += char
    result.append(element) if element else None
    return result


def create_interface(value: str):
    global last_value
    if value in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        display_number.delete(0, END) if last_value in operators.keys() else None
        last_value = value
        add_number_to_entry(value)
    elif value in operators.keys():
        last_value = value
        add_sign_to_entry(value)
    elif value in '=':
        last_value = value
        add_sign_to_entry(value)
    elif value in '<-' and display_expression.get().strip() != '0':
        last_value = value
        display_expression.delete(len(display_expression.get()) - 1)
        display_expression.insert(END, '0') if not display_expression.get().strip() else None
        display_number.delete(0, END)
        example = get_example_as_list(display_expression.get())[-1]
        display_number.insert(0, example) if example not in operators.keys() else None
    elif value in 'C':
        last_value = value
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
            _ = Button(text=text.split()[0], fg='black', command=lambda t=text.split()[0]: create_interface(t))
            _.grid(column=x, row=y + 2, columnspan=int(text.split()[1]), rowspan=int(text.split()[2]), sticky=NSEW)

root.mainloop()

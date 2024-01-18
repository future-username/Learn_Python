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
from operator import add, sub, mul, truediv

button_texts = [
    # ["MC 1 1", "MR 1 1", "MS 1 1", "M+ 1 1", "M- 1 1"],
    ["<- 1 1", "CE 1 1", "C 1 1", '± 1 1', '√ 1 1'],
    ["7 1 1", "8 1 1", "9 1 1", "/ 1 1", "% 1 1"],
    ['4 1 1', '5 1 1', '6 1 1', "* 1 1", "1/x 1 1"],
    ['1 1 1', '2 1 1', '3 1 1', "- 1 1", '= 1 2'],
    ['0 2 1', "", '. 1 1', "+ 1 1"],
]

last_value = None
operators = {"+": add, "-": sub, "*": mul, "/": truediv}


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

    display_number.delete(0, END)
    display_number.insert(0, str(calculate(display_expression.get().strip()[:-1])))


def set_plus_minus():
    number = float(display_number.get().strip()) * -1
    example = display_expression.get().strip()
    number_index = len(example) - len(get_example_as_list(example)[-1])
    display_expression.delete(number_index, END)
    display_number.delete(0, END)
    display_expression.insert(END, str(number))
    display_number.insert(END, str(number))


def get_example_as_list(example: str) -> list:
    previous = ''
    numbers = []
    element = ''
    for char in example:
        element += char
        if char in '+*/-' and previous.isdigit():
            numbers.extend([element[:-1], char])
            element = ''
        previous = char

    numbers.append(element)
    return numbers


def calculate(example: list | str, signs: str = '*/') -> float:
    list_example = get_example_as_list(example) if isinstance(example, str) else example
    result_example = []
    previous, char = None, None
    for index, element in enumerate(list_example):
        if str(element) not in '*/+-' and not char:
            previous = float(element)
        elif str(element) in signs:
            char = element
        elif char:
            previous = operators[char](float(previous), float(element))
            char = None
        elif str(element) in '+-' and '+-' not in signs:
            result_example.extend([previous, element])
            char = None
    result_example.append(previous)
    return calculate(result_example, '+-') if '+' in result_example or '-' in result_example else result_example[0]


def create_interface(value: str):
    global last_value
    if last_value == '<-' and display_expression.get().strip()[-1] in operators.keys() and value != '<-':
        display_number.delete(0, END)

    if value in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
        display_number.delete(0, END) if last_value in operators.keys() else None
        add_number_to_entry(value)
    elif value == '±':
        set_plus_minus()
    elif value in operators.keys():
        add_sign_to_entry(value)
    elif value in '=':
        add_sign_to_entry(value)
    elif value in 'C' or (value in '<-' and '=' in display_expression.get().strip()):
        clear()
    elif (value in '<-' and display_expression.get().strip() != '0'
          and display_expression.get().strip()[-1] not in operators.keys()):
        display_expression.delete(len(display_expression.get()) - 1)
        display_expression.insert(END, '0') if not display_expression.get().strip() else None
        display_number.delete(0, END)
        example = get_example_as_list(display_expression.get())[-1]
        display_number.insert(0, example) if example not in operators.keys()\
            else display_number.insert(0, '0')
    last_value = value


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

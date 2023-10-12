# def sum_numbers(a, b):
#     print(a+b)
#     # return a+b
#
#
# print(sum_numbers(8, 9))
# sum_numbers(5, 8)
# sum_numbers(7, 8)


# def replace_char(line, old, new):
#     print(line.replace(old, new))
#
#
# replace_char('name', 'm', '0')
# word = 'name'
# char_1 = 'n'
# char_2 = 'N'
# replace_char(word, char_1, char_2)


"""is_number"""

# def is_int_positive(value):
#     return value.isdigit()
#
#
# def is_int_negative(value):
#     return value.count('-') == 1 and value.removeprefix('-').isdigit()
#
#
# def is_int(value):
#     return is_int_positive(value) or is_int_negative(value)
#
#
# def is_float_positive(value):
#     return value.count('.') == 1 and value.replace('.', '').isdigit()
#
#
# def is_float_negative(value):
#     return value.count('.') == 1 and value.count('-') == 1 and value.replace('.', '').replace('-', '').isdigit()
#
#
# def is_float(value):
#     return is_float_positive(value) or is_float_negative(value)
#
#
# def is_number_positive(value):
#     return is_int_positive(value) or is_float_positive(value)
#
#
# def is_number_negative(value):
#     return is_int_negative(value) or is_float_negative(value)
#
#
# def is_number(value):
#     return is_int(value) or is_float(value)
#
#
# def is_zero(value: str) -> bool:
#     check_minus = (value.count('-') == 1 and value[0] == '-') or value.count('-') == 0
#     check_dot = value.count('.') == 1 or value.count('.') == 0
#     # check_zero =
#     return check_minus and check_dot
#
#
# correct_numbers = ['342', '-2', '23.3', '-23.3', '3.', '.3', '-.4']
# incorrect_numbers = [' 34 2', '--2', '23 .3', '-2 3.3', '3..', '.,3', '-,4', '', ' ', '34f', '.', '-']
# zero_numbers = ['0', '-0', '00000000', '.0', '-0.', '-.0', '0.', '0.00']
# zero_numbers_incorrect = ['--0', '00.0000.00', '.0.', '-0-.', '-.-0', '0-.', '0.0-.0', '.', '-', '10', '-0.1']
# for number in zero_numbers:
#     print(is_zero(number), number)


# def print_value(value: int)->str:
#     result = value * 2
#     print(result)
#     print(value.upper())
#     return result
#
#
# print_value('egegeg')
# print_value(3).split()
# [].insert()
# todo: is_zero, calculator_fields, cat_calculator


# from tkinter import *
#
#
# def change_time(value: str, label: Label):
#     label.config(text=value)


# def change_time_2(value: str):
#     label_2.config(text=value)
#
#
# def change_time_3(value: str):
#     label_3.config(text=value)


# def change_time():
#     label_1.config(text='monday')
#
#
# def change_time_2():
#     label_2.config(text='tuesday')
#
#
# def change_time_3():
#     label_3.config(text='wednesday')


# root = Tk()
#
# label_1 = Label(text='1')
# label_1.pack()
# label_2 = Label(text='2')
# label_2.pack()
# label_3 = Label(text='3')
# label_3.pack()
#
# change_time('monday', label_1)
# change_time('tuesday', label_2)
# change_time('wednesday', label_3)
#
#
# root.mainloop()


# def get_input() -> str:
#     return input('Enter the number:\t')
#
#
# def test_input(value: str) -> bool:
#     return value.isnumeric() and value != '0'
#
#
# def str_to_int(value: str) -> int:
#     return int(value)
#
#
# def print_int(value: int) -> None:
#     print(value)
#
#
# def main() -> None:
#     text = get_input()
#     number = str_to_int(value=text) if test_input(value=text) else print('Error type')
#     print_int(number)
#
#
# if __name__ == '__main__':
#     main()


# numbers = {
#     'I': 1,
#     'II': 2,
#     'III': 3,
#     'V': 5,
#     'IV': 4,
#     'VI': 6,
#     'VII': 7,
#     'VIII': 8,
#     'IX': 9,
#     'X': 10,
#     'XX': 20,
#     'XXX': 30,
#     'XL': 40,
#     'L': 50
# }
#
#
# def is_number(value: str, roman_numbers: list) -> bool:
#     return any(value == number for number in roman_numbers)
#
#
# def start_or_end_number(value: str, roman_numbers: list) -> bool:
#     is_dozen = 'L' in roman_numbers
#     is_unit = 'V' in roman_numbers
#     flag = False
#     for number in roman_numbers:
#         if value.startswith(number) and is_dozen:
#             flag = True
#         elif value.endswith(number) and is_unit:
#             flag = True
#     return flag
#
#
# def is_rim_number(value: str) -> bool:
#     dozens = list(numbers.keys())[9:]
#     units = list(numbers.keys())[:9]
#     is_dozen_after_unit = start_or_end_number(value, dozens) and start_or_end_number(value, units)
#     return is_dozen_after_unit or is_number(value, dozens) or is_number(value, units)
#
#
# def rim_unit_to_int(num: str) -> str:
#     result = ''
#     for char in list(numbers.keys())[:9]:
#         if num.endswith(char):
#             result = char
#     return result
#
#
# def rim_dozen_to_int(num: str) -> str:
#     result = ''
#     for char in list(numbers.keys())[9:]:
#         if num.startswith(char):
#             result = char
#     return result
#
#
# def rim_to_int(num: str) -> int:
#     dozen = rim_dozen_to_int(num)
#     unit = rim_unit_to_int(num)
#     result = int()
#     if dozen and unit:
#         result = numbers[dozen] + numbers[unit]
#     elif dozen:
#         result = numbers[dozen]
#     elif unit:
#         result = numbers[unit]
#
#     return result
#
#
# def main() -> None:
#     text = input('Enter the number:\t').upper().strip()
#     print(rim_to_int(text)) if is_rim_number(text) else print('Это не римское число')
#
#
# if __name__ == '__main__':
#     main()


from tkinter import *

numbers = [
    ['I', 1],
    ['II', 2],
    ['III', 3],
    ['IV', 4],
    ['V', 5],
    ['VI', 6],
    ['VII', 7],
    ['VIII', 8],
    ['IX', 9],
    ['X', 10],
    ['XX', 20],
    ['XXX', 30],
    ['XL', 40],
    ['L', 50],
    ['LX', 60],
    ['LXX', 70],
    ['LXXX', 80],
    ['XC', 90],
    ['C', 100],
    ['CC', 200],
    ['CCC', 300],
    ['CD', 400],
    ['D', 500],
    ['DC', 600],
    ['DCC', 700],
    ['DCCC', 800],
    ['CM', 900],
]

units = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
dozens = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
hundreds = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
check = ''


# def is_rim_number(value: str) -> bool:
#     dozen, unit = [], []
#     for roman_number, int_number in numbers:
#         dozen = list(roman_number)[9:]
#         unit = list(roman_number)[:9]
#
#     is_dozen_after_unit = start_or_end_number(value, dozen) and start_or_end_number(value, unit)
#     return is_dozen_after_unit or is_number(value, dozen) or is_number(value, unit)


def is_number(value: str, roman_numbers: list) -> bool:
    return any(value == number for number in roman_numbers)


def start_or_end_number(value: str, roman_numbers: list) -> bool:
    global check
    is_dozen = 'L' in roman_numbers
    is_unit = 'V' in roman_numbers
    is_hundred = 'C' in roman_numbers
    flag = False
    for number in roman_numbers:
        if value.startswith(number) and is_hundred:
            check = check.replace(number, '')
            flag = True
        elif value.startswith(number) and is_dozen:
            check = check.replace(number, '')
            flag = True
        elif value.endswith(number) and is_unit:
            flag = True

    return flag


# def is_rim_number(value: str) -> bool:
#     is_hundred_after_dozen = start_or_end_number(value, hundreds) and start_or_end_number(value, dozens)
#     is_hundred_after_unit = start_or_end_number(value, hundreds) and start_or_end_number(value, units)
#     is_dozen_after_unit = start_or_end_number(value, dozens) and start_or_end_number(value, units)
#     return is_dozen_after_unit or is_number(value, dozens) or is_number(value, units) or is_hundred_after_dozen or is_number(value, hundreds) or is_hundred_after_unit

def is_rim_number(value: str) -> bool:
    global check
    check = value
    is_hundred_after_dozen = start_or_end_number(value, hundreds) and start_or_end_number(value, dozens)
    is_hundred_after_unit = start_or_end_number(value, hundreds) and start_or_end_number(value, units)
    is_dozen_after_unit = start_or_end_number(value, dozens) and start_or_end_number(value, units)
    return is_dozen_after_unit or is_number(value, dozens) or is_number(value, units) or is_hundred_after_dozen or is_number(value, hundreds) or is_hundred_after_unit


def rim_to_int(value: str) -> int:
    units, dozens, hundreds = numbers[:9], numbers[9:18], numbers[18:]
    result_hundred, result_dozen, result_unit = 0, 0, 0

    for roman_number, int_number in hundreds:
        if value.startswith(roman_number):
            result_hundred = int_number
            value = value.replace(roman_number, '')
    for roman_number, int_number in dozens:
        if value.startswith(roman_number):
            result_dozen = int_number
            value = value.replace(roman_number, '')
    for roman_number, int_number in units:
        if value.endswith(roman_number):
            result_unit = int_number
    return result_hundred + result_dozen + result_unit


def int_to_rim(value: str) -> str:
    if len(value) == 2:
        int_dozen = int(' '.join(value).split()[0]) * 10
        int_unit = int(' '.join(value).split()[1])
        value = f'{int_dozen} {int_unit}'
    elif len(value) == 3:
        int_hundred = int(' '.join(value).split()[0]) * 100
        int_dozen = int(' '.join(value).split()[1]) * 10
        int_unit = int(' '.join(value).split()[2])
        value = f'{int_hundred} {int_dozen} {int_unit}'

    result = ''
    for roman_number, int_number in numbers:
        for i in value.split():
            if int(i) == int_number:
                result = f'{roman_number}{result}'
    return result


def is_number_int(num: str) -> bool:
    return num.isdigit()


def main(widget_in: Entry, widget_out: Label) -> None:
    # result = int_to_rim(widget_in.get()) if is_number_int(widget_in.get()) else 'Это не число'
    # result = ''
    # print(rim_to_int(widget_in.get()))
    # print(is_rim_number(widget_in.get()))
    # if is_number_int(widget_in.get()):
    #     result = int_to_rim(widget_in.get())
    # elif is_rim_number(widget_in.get()):
    #     result = rim_to_int(widget_in.get().upper())
    # widget_out.config(text=result)
    # is_rim_number('1')
    for i in ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XVI',
              'XVII', 'XVIII', 'XIX', 'XX', 'VV', 'VX', '   V', 'XCM', 'CM', 'XC', 'CX', 'IC', 'CX', 'CI', 'CXXIIX', 'CXXKI', 'XgyreudhjsvcbmnIX']:
        print(i, is_rim_number(i.strip()))


root = Tk()
root.title('Convert Roman')
entry = Entry()
entry.pack(side=LEFT)
button = Button(text='Convert', command=lambda: main(entry, label))
button.pack(side=LEFT)
label = Label()
label.pack(side=LEFT)

root.mainloop()

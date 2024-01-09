# # class Square:
# #     def __init__(self, side):
# #         self.side = side
# #
# #     def calculate_area(self):
# #         return self.side * self.side
# #
# #
# # class Rectangle:
# #     def __init__(self, width, height):
# #         self.width = width
# #         self.height = height
# #
# #     def get_area(self):
# #         return self.width * self.height
# #
# #
# # class RectangleAdapter:
# #     def __init__(self, rectangle):
# #         self.rectangle = rectangle
# #
# #     def calculate_area(self):
# #         return self.rectangle.get_area()
# #
# #
# # # Пример использования
# # square = Square(5)
# # rectangle = Rectangle(4, 6)
# #
# # adapter = RectangleAdapter(rectangle)
# # area = adapter.calculate_area()
# #
# # print("Area:", area)
#
#
# # class SingletonClass(object):
# #     instance = None
# #
# #     def __new__(cls):
# #         if not cls.instance:
# #             cls.instance = super(SingletonClass, cls).__new__(cls)
# #         return cls.instance
# #
# #
# # # Usage:
# # s1 = SingletonClass()
# # s2 = SingletonClass()
# #
# # print(s1 is s2)  # Output: True
#
#
# # class Button:
# #     def __init__(self, text):
# #         self.text = text
# #
# #     def click(self):
# #         print(f"Button '{self.text}' was clicked")
# #
# #
# # class UIFactory:
# #     def create_button(self, button_type, text):
# #         if button_type == "Windows":
# #             return WindowsButton(text)
# #         elif button_type == "Linux":
# #             return LinuxButton(text)
# #         else:
# #             raise ValueError("Invalid button type")
# #
# #
# # class WindowsButton(Button):
# #     def __init__(self, text):
# #         super().__init__(text)
# #         # Дополнительная инициализация для кнопки Windows
# #
# #
# # class LinuxButton(Button):
# #     def __init__(self, text):
# #         super().__init__(text)
# #         # Дополнительная инициализация для кнопки Linux
# #
# #
# # factory = UIFactory()
# #
# # windows_button = factory.create_button("Windows", "Click me")
# # windows_button.click()  # Выведется: Button 'Click me' was clicked
# #
# # linux_button = factory.create_button("Linux", "Press here")
# # linux_button.click()  # Выведется: Button 'Press here' was clicked
#
# # from operator import add, sub, mul, truediv
# #
# # line = '2+2/2'
# #
# # sign_labels = {
# #     "+": add,
# #     "-": sub,
# #     "*": mul,
# #     "/": truediv,
# # }
# #
# #
# # def split_example(example: str) -> list:
# #     result = []
# #     example_number = ''
# #     for value in example:
# #         if value in sign_labels.items().mapping:
# #             result.extend([example_number, value])
# #             example_number = ''
# #         else:
# #             example_number += value
# #     result.append(example_number)
# #     return result
# #
# #
# # def calculate(example):
# #     result = None
# #     sign = ''
# #     for element in split_example(example):
# #         if element not in sign_labels.items().mapping and not sign:
# #             result = int(element)
# #         elif element in sign_labels:
# #             sign = element
# #         elif sign:
# #             result = sign_labels[sign](result, int(element))
# #
# #     return result
# #
# #
# # print(calculate(line))
#
#
# import operator
# import re
#
# line = '2+3/2*7'
# operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "^": operator.pow}
# precedence = {"+": 0, "-": 0, "*": 1, "/": 1, '^': 2}
#
#
# def apply_op(op_stack, num_stack):
#     op = op_stack.pop()
#     num2, num1 = num_stack.pop(), num_stack.pop()
#     num_stack.append(operators[op](num1, num2))
#
#
# def calculate(line):
#     num_stack, op_stack = [], []
#
#     for token in re.findall("[+/*-]|[\d]+", line):
#         if token in operators:
#             while op_stack and op_stack[-1] in operators and precedence[token] <= precedence[op_stack[-1]]:
#                 apply_op(op_stack, num_stack)
#             op_stack.append(token)
#         else:
#             num_stack.append(float(token))
#
#     while op_stack:
#         apply_op(op_stack, num_stack)
#
#     return num_stack[0]
#
#
# print(calculate(line))
from operator import add, sub, mul, truediv
import re

operators = {"+": add, "-": sub, "*": mul, "/": truediv, '+-': sub, '--': add, '++': add, '-+': sub}
precedence = {"+": 0, "-": 0, "*": 1, "/": 1, '+-': 0, '--': 0, '++': 0, '-+': 0}


def apply_op(op_stack, num_stack):
    # print(op_stack, num_stack)
    op = op_stack.pop()
    num2, num1 = num_stack.pop(), num_stack.pop()
    num_stack.append(operators[op](num1, num2))


def calculate(example):
    if example[-1] in operators.keys():
        example = example[:-1]
    num_stack, op_stack = [], []
    example = example.replace('+-', '-')
    example = example.replace('--', '+')

    for token in re.findall(r"[+/*-]|\d+", example):
        if example.startswith('-') and not num_stack and len(op_stack) == 1:
            num_stack.append(float(f'{op_stack[0]}{token}'))
            op_stack.clear()
        elif token in operators:
            while op_stack and op_stack[-1] in operators and precedence[token] <= precedence[op_stack[-1]]:
                apply_op(op_stack, num_stack)
            op_stack.append(token)
        else:
            num_stack.append(float(token))

    while op_stack:
        apply_op(op_stack, num_stack)
    return str(num_stack[0])
    # display_number.delete(0, END)
    # display_number.insert(0, str(num_stack[0]))


print('result', calculate('-5+6'))
print('result', calculate('-5+-6'))
print('result', calculate('-5--6'))
print('result', calculate('5-6'))
print('result', calculate('5+6'))

"""
2+2/-2*10-5*-8
2+-10--40
32
"""

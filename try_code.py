# # from tkinter import *
# # from random import randrange
# #
# # flag = True
# #
# #
# # class SingletonFrame(type):
# #     _instances: dict[str, LabelFrame] = {}
# #
# #     def __call__(cls, *args, **kwargs):
# #         if cls not in cls._instances:
# #             instance = super().__call__(*args, **kwargs)
# #             cls._instances[cls] = instance
# #         return cls._instances[cls]
# #
# #
# # class MyStringVar(metaclass=SingletonFrame):
# #     def __init__(self, field, *args, **kwargs):
# #         self.field = field
# #         super().__init__(*args, **kwargs)
# #         self.data = randrange(100)
# #         # root.bind('<Key>', self.set_data)
# #
# #     def set_data(self, _):
# #         print(self.field['background'])
# #         self.data = self.field.get()
# #
# #
# # def change_entry():
# #     global flag, entry1, entry
# #     if flag:
# #         # entry1.pack_forget()
# #         entry1.destroy()
# #         # entry.pack()
# #         entry = Entry()
# #         entry.pack()
# #         entry.insert(0, string_var.data)
# #     else:
# #         # entry1.pack()
# #         entry1 = Entry()
# #         entry1.pack()
# #         # entry.pack_forget()
# #         entry.destroy()
# #         entry1.insert(0, string_var.data)
# #     flag = not flag
# #     print(MyStringVar().data)
# #
# #
# # root = Tk()
# # entry = Entry(background='yellow')
# # string_var = MyStringVar(entry)
# # entry.insert(0, string_var.data)
# # # entry.pack()
# # entry1 = Entry()
# # string_var = MyStringVar(entry)
# # entry1.insert(0, string_var.data)
# # root.bind('<Key>', string_var.set_data)
# # # entry1.pack()
# # Button(text='1', command=change_entry).pack()
# #
# # root.mainloop()
#
#
# from tkinter import *
# from tkinter import filedialog
# import json
#
#
# class Errors:
#     @staticmethod
#     def type_error(value, type_value):
#         raise TypeError(f'{value} this is not {type_value}')
#
#
# class SingletonForm(type):
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             instance = super().__call__(*args, **kwargs)
#             cls._instances[cls] = instance
#         return cls._instances[cls]
#
#
# class Data(metaclass=SingletonForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.__languages_data: dict = {}
#         self.language_name = ''
#
#     def get_language(self, language: str) -> list:
#         for item in self.__languages_data:
#             if item["language"] == language:
#                 return item['data']
#
#     def set_language(self, language: str, data: list[dict]):
#         for index, data in enumerate(self.__languages_data):
#             if data["language"] == language:
#                 self.languages_data[index]['data'] = data
#
#     @property
#     def languages_data(self):
#         return self.__languages_data
#
#     @languages_data.setter
#     def languages_data(self, data: dict) -> None:
#         self.__languages_data = data
#
#
# class LabelEntry(Frame):
#     def __init__(self, parent, label_text: str, entry_text: str, *args, **kwargs):
#         """
#         :param parent:
#         :param label_text: str
#         :param entry_text: str
#         """
#         super().__init__(parent, *args, **kwargs)
#
#         self.__entry = Entry(master=self, bg="white")
#         self.__entry.insert(0, entry_text)
#         self.__entry.pack(side=RIGHT)
#
#         Label(master=self, text=label_text, fg="black").pack(side=LEFT)
#
#     def get_data(self) -> str:
#         return self.__entry.get()
#
#
# class Form(LabelFrame):
#     def __init__(self, language: str, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         self.__language = language
#         self['text'] = self.__language
#         self.__data_list: list[dict] = []
#         self.__data_dict = {}
#         self.pack()
#
#     def change(self):
#         for widget in self.winfo_children():
#             self.__save_data(widget, Data().language_name)
#         for label in Data().get_language(self.__language):
#             LabelEntry(self, label['label'], label['entry']).pack(fill=X)
#         Data().language_name = self.__language
#
#     def __save_data(self, data: Widget, language) -> None:
#         temp = {}
#         for element in data.winfo_children():
#             if isinstance(element, Label):
#                 temp['label'] = element['text']
#                 self.__data_list.append(temp)
#                 temp = {}
#             if isinstance(element, Entry):
#                 temp['entry'] = element.get()
#
#         name = language if not Data().language_name else Data().language_name
#         Data().set_language(name, self.__data_list)
#
#
# class ButtonTranslate:
#     __previous_form_1 = None
#
#     def __init__(self, parent: LabelFrame, language_name: str):
#         self.parent = parent if isinstance(parent, LabelFrame) else Errors.type_error(parent, LabelFrame)
#         self.language_name = language_name
#         self.data_list: list[dict] = []
#
#         self.button = Button(parent, text=language_name, fg="black", command=self.translate_label)
#
#     def translate_label(self):
#         self.__class__.__previous_form_1.destroy() if self.__class__.__previous_form_1 else None
#         f = Form(self.language_name)
#         f.change()
#         self.__class__.__previous_form_1 = f
#         # Form(self.frame, self.language_name).change()
#
#         # for label in Data().get_language(self.language_name):
#         #     LabelEntry(self.frame, label['label'], label['entry']).pack(fill=X)
#
#     def pack(self, *args, **kwargs):
#         """
#         Pack button
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         self.button.pack(*args, **kwargs)
#
#     def grid(self, *args, **kwargs):
#         """
#         Grid button
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         self.button.grid(*args, **kwargs)
#
#
# class App:
#     def __init__(
#             self,
#             title: str,
#             frame_buttons_title: str = '',
#             frame_form_title: str = ''
#     ):
#         self.frame_buttons_title = frame_buttons_title if isinstance(frame_buttons_title, str) \
#             else Errors.type_error(frame_buttons_title, str)
#         self.frame_form_title = frame_form_title if isinstance(frame_form_title, str) \
#             else Errors.type_error(frame_form_title, str)
#         # None if isinstance(languages, json) else Errors.type_error(languages, dict)
#         # for key in languages.keys():
#         #     None if isinstance(key, str) else Errors.type_error(key, str)
#         #
#         # for value in languages.values():
#         #     None if isinstance(value, list) else Errors.type_error(value, list)
#         #     for value_in_list in value:
#         #         None if isinstance(value_in_list, str) else Errors.type_error(value_in_list, str)
#
#         self.root = Tk()
#         None if isinstance(title, str) else Errors.type_error(title, str)
#         self.root.title(title)
#         frame_menu = Frame()
#         frame_menu.pack()
#         Button(frame_menu, text='Open', fg="black", command=self.__open_file).pack(side=LEFT)
#         Button(frame_menu, text='Save', fg="black").pack(side=RIGHT)
#
#     def __create_interface(self, languages: json):
#         frame_buttons = LabelFrame(text=self.frame_buttons_title)
#         frame_buttons.pack()
#
#         # frame_form = LabelFrame(text=self.frame_form_title)
#         # frame_form.pack()
#         Data().languages_data = languages
#         for index, language in enumerate(languages):
#             _ = ButtonTranslate(frame_buttons, language["language"])
#             _.grid(column=index, row=len(language["data"]))
#             _.translate_label() if index == 0 else None
#
#     def __open_file(self):
#         """
#         Open file and add data to Labels
#         :return: None
#         """
#         file_name = filedialog.askopenfilename(filetypes=[("json files", '*.json')])
#         if file_name:
#             with open(file_name, 'r', encoding='UTF-8') as file:
#                 file_data = json.load(file)
#             self.__create_interface(file_data) if file_data else None
#
#     # def __save_file(self):
#     #     data = {
#     #
#     #     }
#     #     file_name = filedialog.asksaveasfilename(
#     #         defaultextension='.json', filetypes=[("json files", '*.json')],
#     #         title="Choose filename")
#     #     if file_name:
#     #         with open(file_name, 'w', encoding='UTF-8') as file:
#     #             file.write(json.dumps(data))
#
#     def draw(self):
#         self.root.mainloop()
#
#
# if __name__ == '__main__':
#     App(title="Form", frame_buttons_title='Translate').draw()
# from tkinter_file.tkinter_grid import result_plus


# import tkinter as tk
#
#
# class Command:
#     def __init__(self, calculator):
#         self.calculator = calculator
#
#     def execute(self):
#         return self.calculator.calculate()
#
#
#
#
#
# class Calculator:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.entry1 = tk.Entry(self.root)
#         self.entry2 = tk.Entry(self.root)
#         self.button = tk.Button(self.root, text="Calculate", command=self.calculate)
#         self.result = tk.StringVar()
#         self.label = tk.Label(self.root, textvariable=self.result)
#
#         self.entry1.pack()
#         self.entry2.pack()
#         self.button.pack()
#         self.label.pack()
#
#         self.root.mainloop()
#
#     def calculate(self):
#         op1 = int(self.entry1.get())
#         op2 = int(self.entry2.get())
#         command = Command(self)
#         result = command.execute(op1, op2)
#         self.result.set(result)
#
#
# if __name__ == "__main__":
#     import warnings
#
#     warnings.filterwarnings("ignore", category=UserWarning,
#                             message="Secure coding is not enabled for restorable state!")
#     Calculator()


# import re
#
# def is_russian_phone_number(phone_number):
#     pattern = re.compile(r'(\+7|7)([ -]*)?(\(?\d{3}\)?)[ -]*(\d{3})[ -]*(\d{2})[ -]*(\d{2})')
#     return bool(pattern.match(phone_number))
#
# # Test the function
# print(is_russian_phone_number('+7 (999) 123-45-67'))  # True
# print(is_russian_phone_number('79991234567'))  # True
# print(is_russian_phone_number('+7 999 123 45 67'))  # True
# print(is_russian_phone_number('7999123456'))  # False (missing extension digits)
# print(is_russian_phone_number('+999 123 45 67'))  # False (wrong country code)


# import operator
# from typing import Callable
#
#
# def some_func(a: int, b: int, name: str, func: Callable):
#     print(name, func(a, b))
#
#
# print(operator.add(1, 1))
# print(operator.sub(1, 1))
#
# some_func(5, 8, 'summ', operator.add)
# some_func(5, 8, 'sub', operator.sub)


# from abc import ABC, abstractmethod
#
#
# class AssureClient(ABC):
#
#     # noinspection PyUnusedLocal
#     @abstractmethod
#     def __init__(
#             self,
#             host: str,
#             port: int = 30001,
#             access_token = None,
#             ssl_cert = None):
#         raise NotImplementedError()
#
#
# class LabelEntry(ABC):
#     @abstractmethod
#     def __init__(self, parent, label_text: str, entry_text: str, *args, **kwargs):
#         """
#         LabelEntry
#         :param parent:
#         :param label_text: text to Label
#         :param entry_text: text to Entry
#         """
#         super().__init__(*args, **kwargs)
#         raise NotImplementedError()
#
#     @abstractmethod
#     def get_data(self) -> dict[str: str]:
#         """
#         Get data from LabelEntry
#         :return: label and entry in dict
#         """
#         raise NotImplementedError()


# class StringCheck:
#     def __init__(self, text: str):
#         self.__text = text
#
#     def is_lower(self):
#         return self.__text.islower()
#
#     def is_upper(self):
#         return self.__text.isupper()
#
#     def is_title(self):
#         return self.__text.istitle()
#
#
# class StringSwitchCase:
#     def __init__(self, text: str):
#         self.__text = text
#
#     def lower(self):
#         return self.__text.lower()
#
#     def upper(self):
#         return self.__text.upper()
#
#     def title(self):
#         return self.__text.title()
#
#
# class StringJustify:
#     def __init__(self, text: str):
#         self.__text = text
#
#     def center(self, width: int, fill_char: str = " ") -> str:
#         return self.__text.center(width, fill_char)
#     def left_just(self, width: int, fill_char: str = " ") -> str:
#         return self.__text.ljust(width, fill_char)
#     def right_just(self, width: int, fill_char: str = " ") -> str:
#         return self.__text.rjust(width, fill_char)
#
# class MyString:
#     def __init__(self, text: str):
#         self.__text = text
#         self.check = StringCheck(self.__text)
#         self.switch_case = StringSwitchCase(self.__text)
#         self.justify = StringJustify(self.__text)
#
#
# line = MyString('AnY tExT.')
# print(line.switch_case.lower())
# print(line.check.is_lower())


# from threading import Thread
# from tkinter import Tk, Button, Label
# from random import randint
# import time
#
# amount = 1
# place = 1
#
# def go_thread(widget, text):
#     global place
#     text += '#'
#     widget.config(text=text)
#     if len(text) < 30:
#         time.sleep(randint(0, 3))
#         go_thread(widget, text)
#     else:
#         text += f'  {place} place'
#         widget.config(text=text, bg="lightgreen")
#         place += 1
#
# def run_thread():
#     global amount
#     label = Label()
#     label.pack(anchor="w", padx=5, pady=3)
#     Thread(target=go_thread, args=(label, f'Thread {amount}: ')).start()
#     amount += 1
#
# root = Tk()
# root.title('Monogenes')
# root.minsize(250,50)
# Button(text="Run a new thread", command=run_thread).pack()
# root.mainloop()


#  напишите стек, который поддерживает методы push, pop, top, get_min
# (получение минимального элемента) за постоянное время:

# это будет твой класс Stack и надо его реализовать !
# class Stack:
#     def __init__(self):
#         self.stack = []   # основной стек для хранения элементов
#         self.min_num = None # стек для хранения минимальных значений
#
#     def push(self, value):
#         if not self.min_num:
#             self.min_num = value
#         elif value < self.min_num:
#             self.min_num = value
#
#         self.stack.append(value)
#
#     def pop(self):
#         return self.stack.pop(len(self.stack))
#
#     def top(self):
#         return self.stack[-1]
#
#     def get_min(self):
#         return self.min_num
#
#
# # Пример использования
# stack = Stack()
# stack.push(3)
# stack.push(5)
# print(stack.get_min())  # Вывод: 3


# import functools
#
#
# def my_decorator(func):
#     # @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Вызов функции до выполнения.")
#         result = func(*args, **kwargs)
#         print("Вызов функции после выполнения.")
#         return result
#
#     return wrapper
#
#
# @my_decorator
# def say_hello(name):
#     """Приветствует пользователя по имени."""
#     return f"Привет, {name}!"
#
#
# print(say_hello.__name__)  # Выводит "say_hello"
# print(say_hello.__doc__)  # Выводит "Приветствует пользователя по имени."
# # print(say_hello('xcghjk').)

# from functools import wraps
#
# class StringCheck:
#     def __init__(self, text: str):
#         self.__text = text
#
#     @wraps(str.islower)
#     def is_lower(self):
#         return self.__text.islower()
#
#     def is_upper(self):
#         return self.__text.isupper()
#
#     def is_title(self):
#         return self.__text.istitle()
#
#
# print(f'{StringCheck('sd').is_lower.__doc__ =}')
# print(f'{StringCheck('sd').is_upper.__doc__ =}')   # 'aNy TeXt.'


# from functools import wraps
# """
# Парттерн Фасад: реализация кода в результате которой,
# происходи группировка методов основного класса String на подгруппы методов.
# """
#
# class StringCheck:
#     def __init__(self, text: str):
#         self.__text = text
#
#     @wraps(str.islower)
#     def is_lower(self):
#         return self.__text.islower()
#
#     @wraps(str.isupper)
#     def is_upper(self):
#         """
#         My doc
#         :return:
#         """
#         return self.__text.isupper()
#
#     def is_title(self):
#         return self.__text.istitle()
#
#
# print(f'{StringCheck('sd').is_lower.__doc__ =}')
# print(f'{StringCheck('sd').is_upper.__doc__ =}')
# print(f'{StringCheck('sd').is_title.__doc__ =}')


# class StringSwitchCase:
#     def __init__(self, text: str):
#         self.__text = text
#
#     def lower(self):
#         return self.__text.lower()
#
#     def upper(self):
#         return self.__text.upper()
#
#     def title(self):
#         return self.__text.title()
def write_doc(param: str) -> str:
    doc_info = str().__getattribute__(param.strip().split('.')[-1].removesuffix('()')).__doc__

    n = '"""'

    return f"\t\t{n}\t\t\n{doc_info}\n{n}".replace('\n', '\n\t\t')


for line in open('another_try_code.py'):
    # if line.startswith('def'):
    #     print(line)

    if line.strip().startswith('return'):
        print(write_doc(line))
    print(line, end='')


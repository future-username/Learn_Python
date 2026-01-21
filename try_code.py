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
# def write_doc(param: str) -> str:
#     doc_info = str().__getattribute__(param.strip().split('.')[-1].removesuffix('()')).__doc__
#
#     n = '"""'
#
#     return f"\t\t{n}\t\t\n{doc_info}\n{n}".replace('\n', '\n\t\t')
#
#
# for line in open('another_try_code.py'):
#     # if line.startswith('def'):
#     #     print(line)
#
#     if line.strip().startswith('return'):
#         print(write_doc(line))
#     print(line, end='')

# mermaid2py.py
# from __future__ import annotations
# from dataclasses import dataclass, field
# from typing import List, Optional, Dict, Union
# import re
# import asyncio
# from contextlib import contextmanager

# # ---------- IR ----------
# @dataclass
# class Participant:
#     name: str
#     label: Optional[str] = None

# @dataclass
# class Message:
#     src: str
#     dst: str
#     text: str
#     kind: str  # "call" or "return"

# @dataclass
# class AltBranch:
#     label: str
#     body: List["Node"] = field(default_factory=list)

# @dataclass
# class AltBlock:
#     branches: List[AltBranch] = field(default_factory=list)

# @dataclass
# class OptBlock:
#     label: str
#     body: List["Node"] = field(default_factory=list)

# @dataclass
# class LoopBlock:
#     label: str
#     body: List["Node"] = field(default_factory=list)

# @dataclass
# class ParBlock:
#     branches: List[List["Node"]] = field(default_factory=list)

# @dataclass
# class CriticalBlock:
#     label: str
#     body: List["Node"] = field(default_factory=list)
#     option_label: Optional[str] = None
#     option_body: List["Node"] = field(default_factory=list)

# @dataclass
# class Note:
#     label: str

# Node = Union[Message, AltBlock, OptBlock, LoopBlock, ParBlock, CriticalBlock, Note]

# @dataclass
# class Diagram:
#     participants: Dict[str, Participant]
#     body: List[Node]

# # ---------- Parser ----------
# ARROW_RE = re.compile(r"^\s*([A-Za-z_][\w]*)\s*(-{2}|-)?(>>|>)\s*([A-Za-z_][\w]*)\s*:\s*(.+)$")
# PARTICIPANT_RE = re.compile(r"^\s*participant\s+([A-Za-z_][\w]*)(?:\s+as\s+(.+))?\s*$")
# ALT_RE = re.compile(r"^\s*alt\s*(.*)$")
# ELSE_RE = re.compile(r"^\s*else\s*(.*)$")
# END_RE = re.compile(r"^\s*end\s*$")
# OPT_RE = re.compile(r"^\s*opt\s*(.*)$")
# LOOP_RE = re.compile(r"^\s*loop\s*(.*)$")
# PAR_RE = re.compile(r"^\s*par\s*(.*)$")
# AND_RE = re.compile(r"^\s*and\s*(.*)$")
# CRIT_RE = re.compile(r"^\s*critical\s*(.*)$")
# OPTION_RE = re.compile(r"^\s*option\s*(.*)$")
# NOTE_RE = re.compile(r"^\s*Note\s+(?:over|left of|right of)\s+.+:\s*(.*)$")
# IGNORE_RE = re.compile(r"^\s*(sequenceDiagram|autonumber|activate|deactivate|create|destroy|box|rect|end\s+box|%%).*")

# def parse_mermaid(text: str) -> Diagram:
#     participants: Dict[str, Participant] = {}
#     body: List[Node] = []
#     stack: List[List[Node]] = [body]
#     alt_stack: List[AltBlock] = []
#     par_stack: List[ParBlock] = []
#     crit_stack: List[CriticalBlock] = []

#     def current_body() -> List[Node]:
#         return stack[-1]

#     for raw in text.splitlines():
#         line = raw.strip("\n")
#         if not line.strip():
#             continue

#         # participants
#         m = PARTICIPANT_RE.match(line)
#         if m:
#             name, label = m.group(1), (m.group(2).strip() if m.group(2) else None)
#             participants[name] = Participant(name=name, label=label)
#             continue

#         # ignore visuals/comments
#         if IGNORE_RE.match(line):
#             continue

#         # notes
#         m = NOTE_RE.match(line)
#         if m:
#             current_body().append(Note(label=m.group(1).strip()))
#             continue

#         # alt
#         m = ALT_RE.match(line)
#         if m:
#             blk = AltBlock(branches=[AltBranch(label=(m.group(1) or "condition").strip())])
#             current_body().append(blk)
#             alt_stack.append(blk)
#             stack.append(blk.branches[0].body)
#             continue

#         m = ELSE_RE.match(line)
#         if m and alt_stack:
#             stack.pop()  # end previous branch body
#             blk = alt_stack[-1]
#             blk.branches.append(AltBranch(label=(m.group(1) or "else").strip()))
#             stack.append(blk.branches[-1].body)
#             continue

#         # opt
#         m = OPT_RE.match(line)
#         if m:
#             blk = OptBlock(label=(m.group(1) or "optional").strip())
#             current_body().append(blk)
#             stack.append(blk.body)
#             continue

#         # loop
#         m = LOOP_RE.match(line)
#         if m:
#             blk = LoopBlock(label=(m.group(1) or "loop").strip())
#             current_body().append(blk)
#             stack.append(blk.body)
#             continue

#         # par
#         m = PAR_RE.match(line)
#         if m:
#             blk = ParBlock(branches=[[]])
#             current_body().append(blk)
#             par_stack.append(blk)
#             stack.append(blk.branches[0])
#             continue

#         m = AND_RE.match(line)
#         if m and par_stack:
#             stack.pop()
#             blk = par_stack[-1]
#             blk.branches.append([])
#             stack.append(blk.branches[-1])
#             continue

#         # critical
#         m = CRIT_RE.match(line)
#         if m:
#             blk = CriticalBlock(label=(m.group(1) or "critical").strip())
#             current_body().append(blk)
#             crit_stack.append(blk)
#             stack.append(blk.body)
#             continue

#         m = OPTION_RE.match(line)
#         if m and crit_stack:
#             stack.pop()
#             blk = crit_stack[-1]
#             blk.option_label = (m.group(1) or "option").strip()
#             stack.append(blk.option_body)
#             continue

#         # end
#         if END_RE.match(line):
#             # close whichever block is active
#             if alt_stack:
#                 stack.pop()
#                 alt_stack.pop()
#             elif par_stack:
#                 stack.pop()
#                 par_stack.pop()
#             elif crit_stack:
#                 stack.pop()
#                 crit_stack.pop()
#             else:
#                 if len(stack) > 1:
#                     stack.pop()
#             continue

#         # message
#         m = ARROW_RE.match(line)
#         if m:
#             src, _, arrow, dst, text = m.group(1), m.group(2), m.group(3), m.group(4), m.group(5).strip()
#             kind = "return" if arrow == ">" else "call"
#             current_body().append(Message(src=src, dst=dst, text=text, kind=kind))
#             continue

#         # fallback: ignore unknown lines
#         # print(f"IGNORED: {line}")

#     return Diagram(participants=participants, body=body)

# # ---------- Codegen ----------
# def snake(s: str) -> str:
#     s = re.sub(r"[^\w]+", "_", s.strip())
#     s = re.sub(r"_+", "_", s)
#     return s.strip("_").lower() or "step"

# def indent(s: str, n: int = 1) -> str:
#     pad = "    " * n
#     return "\n".join(pad + line if line else "" for line in s.splitlines())

# @contextmanager
# def transaction():
#     # TODO: plug your real transaction here
#     try:
#         yield
#     except Exception:
#         # rollback logic
#         raise

# def collect_participants(di: Diagram) -> List[str]:
#     names = set(di.participants.keys())
#     # also from messages
#     def walk(nodes: List[Node]):
#         for n in nodes:
#             if isinstance(n, Message):
#                 names.add(n.src); names.add(n.dst)
#             elif isinstance(n, AltBlock):
#                 for b in n.branches: walk(b.body)
#             elif isinstance(n, OptBlock): walk(n.body)
#             elif isinstance(n, LoopBlock): walk(n.body)
#             elif isinstance(n, ParBlock):
#                 for br in n.branches: walk(br)
#             elif isinstance(n, CriticalBlock):
#                 walk(n.body); walk(n.option_body)
#             else:
#                 pass
#     walk(di.body)
#     return sorted(names)

# def gen_classes(di: Diagram) -> str:
#     out = []
#     for name in collect_participants(di):
#         label = di.participants.get(name, Participant(name)).label
#         title = label or name
#         out.append(f"class {name}:")
#         doc = f'"""Participant: {title}"""'
#         out.append(indent(doc, 1))
#         out.append(indent("def __init__(self):\n        pass", 1))
#         out.append("")  # blank
#     return "\n".join(out)

# def gen_steps(nodes: List[Node], ctx_vars: List[str], step_counter: List[int], depth: int=0, async_mode: bool=False) -> str:
#     lines: List[str] = []
#     def new_step():
#         step_counter[0] += 1
#         return step_counter[0]

#     for n in nodes:
#         if isinstance(n, Note):
#             lines.append(f"# NOTE: {n.label}")
#         elif isinstance(n, Message):
#             if n.kind == "call":
#                 s = new_step()
#                 fname = f"step_{s}_{snake(n.src)}_to_{snake(n.dst)}_{snake(n.text)}"
#                 args = ", ".join(ctx_vars)
#                 lines.append(f"await {fname}({args})" if async_mode else f"{fname}({args})")
#             else:
#                 lines.append(f"# return: {n.src} -> {n.dst}: {n.text}")
#         elif isinstance(n, OptBlock):
#             cond = snake(n.label or "optional") or "cond"
#             lines.append(f"if {cond}:")
#             lines.append(indent(gen_steps(n.body, ctx_vars, step_counter, depth+1, async_mode), 1))
#         elif isinstance(n, AltBlock):
#             for i, br in enumerate(n.branches):
#                 kw = "if" if i == 0 else "else"
#                 lbl = snake(br.label or ( "branch" if i==0 else "else"))
#                 head = f"{kw} {lbl}:" if kw == "if" else "else:"
#                 lines.append(head)
#                 lines.append(indent(gen_steps(br.body, ctx_vars, step_counter, depth+1, async_mode), 1))
#         elif isinstance(n, LoopBlock):
#             it = snake(n.label or "loop") or "n"
#             lines.append(f"for i in range({it}):")
#             lines.append(indent(gen_steps(n.body, ctx_vars, step_counter, depth+1, async_mode), 1))
#         elif isinstance(n, ParBlock):
#             # turn each branch into an async task
#             async_mode = True
#             branch_calls = []
#             inner_defs = []
#             for bi, br in enumerate(n.branches, start=1):
#                 s = new_step()
#                 fn = f"branch_{s}_{bi}"
#                 body = gen_steps(br, ctx_vars, step_counter, depth+1, async_mode=True)
#                 inner_defs.append(f"async def {fn}({', '.join(ctx_vars)}):\n{indent(body,1) or indent('pass',1)}")
#                 branch_calls.append(f"{fn}({', '.join(ctx_vars)})")
#             lines.extend(inner_defs)
#             lines.append(f"await asyncio.gather(\n{indent(',\n'.join(branch_calls),1)}\n)")
#         elif isinstance(n, CriticalBlock):
#             lines.append("try:")
#             lines.append(indent("with transaction():", 1))
#             inner = gen_steps(n.body, ctx_vars, step_counter, depth+1, async_mode)
#             lines.append(indent(inner or "pass", 2))
#             if n.option_body:
#                 lines.append("except Exception:")
#                 alt = gen_steps(n.option_body, ctx_vars, step_counter, depth+1, async_mode)
#                 lines.append(indent(alt or "raise", 1))
#             else:
#                 lines.append("except Exception:\n    raise")
#     return "\n".join(lines)

# def gen_functions(di: Diagram) -> str:
#     steps: List[str] = []
#     seen: set[str] = set()
#     def walk(nodes: List[Node]):
#         for n in nodes:
#             if isinstance(n, Message) and n.kind == "call":
#                 name = f"{snake(n.src)}_to_{snake(n.dst)}_{snake(n.text)}"
#                 if name not in seen:
#                     seen.add(name)
#                     fn = f"def step_{len(seen)}_{name}({', '.join(collect_participants(di))}):\n    # TODO: implement `{n.text}` from {n.src} -> {n.dst}\n    pass"
#                     steps.append(fn)
#             elif isinstance(n, AltBlock):
#                 for b in n.branches: walk(b.body)
#             elif isinstance(n, OptBlock): walk(n.body)
#             elif isinstance(n, LoopBlock): walk(n.body)
#             elif isinstance(n, ParBlock):
#                 for br in n.branches: walk(br)
#             elif isinstance(n, CriticalBlock):
#                 walk(n.body); walk(n.option_body)
#     walk(di.body)
#     return "\n\n".join(steps)

# def generate_python(di: Diagram) -> str:
#     parts = collect_participants(di)
#     classes = gen_classes(di)
#     functions = gen_functions(di)
#     # orchestrator
#     step_counter = [0]
#     body = gen_steps(di.body, parts, step_counter, async_mode=False)
#     # wrap in async if needed
#     needs_async = "asyncio.gather" in body or "await " in body
#     orchestrator = []
#     if needs_async:
#         orchestrator.append("async def main():")
#         orchestrator.append(indent("\n".join([f"{p} = {p}()" for p in parts]), 1))
#         orchestrator.append(indent(body or "pass", 1))
#         orchestrator.append("\nif __name__ == '__main__':\n    asyncio.run(main())")
#     else:
#         orchestrator.append("def main():")
#         orchestrator.append(indent("\n".join([f"{p} = {p}()" for p in parts]), 1))
#         orchestrator.append(indent(body or "pass", 1))
#         orchestrator.append("\nif __name__ == '__main__':\n    main()")
#     prelude = "import asyncio\nfrom contextlib import contextmanager\n\n" + transaction.__code__.co_consts[0] if False else ""
#     return "\n\n".join([
#         "# Generated from Mermaid sequence diagram",
#         "import asyncio",
#         "from contextlib import contextmanager",
#         "",
#         "@" + "contextmanager",
#         "def transaction():\n    try:\n        yield\n    except Exception:\n        raise",
#         "",
#         classes,
#         functions,
#         "\n".join(orchestrator),
#     ])

# # ---------- CLI-like usage ----------
# def translate(mermaid_text: str) -> str:
#     di = parse_mermaid(mermaid_text)
#     return generate_python(di)

# if __name__ == "__main__":
#     demo = ''sequenceDiagram
#     participant User
#     participant Main as Main (if __name__ == "__main__")
#     participant App
#     participant Model
#     participant View
#     participant Controller
#     participant Canvas
#     participant ButtonColor
#     participant ButtonFigures
    
#     User->>Main: Запуск приложения
#     Main->>App: создание App(root)
    
#     Note over App: Приватные поля: __master, __model, __view, __controller
#     App->>Model: создание Model(colors, figures)
#     Note over Model: Приватные поля: __colors, __figures
    
#     App->>View: создание View(master, title)
#     Note over View: Приватные поля: __master, __controller, __color_frame, __figure_frame,<br>__color_label, __color_entry, __figure_label, __buttons_frame,<br>__color_buttons_panel, __figure_buttons_panel, __canvas
    
#     App->>Controller: создание Controller(model, view)
#     Note over Controller: Приватные поля: __model, __view
    
#     View->>Controller: set_controller(controller)
    
#     App->>App: __initialize_view_components()
#     App->>Model: get_colors()
#     App->>View: create_color_buttons(colors)
#     View->>ButtonColor: создание кнопок цветов
#     Note over ButtonColor: Приватные поля: __color_hex, __color_name
    
#     App->>Model: get_figures()
#     App->>View: create_figure_buttons(figures)
#     View->>ButtonFigures: создание кнопок фигур
#     Note over ButtonFigures: Приватные поля: __figure_name, __figure_params
    
#     App->>Model: get_color_name(initial_color_hex)
#     App->>Controller: handle_color_button_click(initial_color_hex, initial_color_name)
#     Controller->>View: set_drawing_color(color_hex)
#     View->>Canvas: set_drawing_color(color_hex)
#     Note over Canvas: Приватные поля: __drawing_color, __current_shape, __start_x,<br>__start_y, __current_shape_id, __shapes
    
#     Controller->>View: update_color_display(color_hex, color_name)
    
#     App->>Controller: handle_figure_button_click(initial_figure)
#     Controller->>View: set_active_figure(figure_name)
#     View->>Canvas: set_shape(figure_name)
#     Controller->>View: update_figure_display(figure_name)
    
#     App->>View: mainloop()
    
#     Note over User, Canvas: Взаимодействие пользователя с приложением
    
#     User->>ButtonColor: Клик на кнопку цвета
#     ButtonColor->>Controller: handle_color_button_click(color_hex, color_name)
#     Controller->>View: set_drawing_color(color_hex)
#     View->>Canvas: set_drawing_color(color_hex)
#     Controller->>View: update_color_display(color_hex, color_name)
    
#     User->>ButtonFigures: Клик на кнопку фигуры
#     ButtonFigures->>Controller: handle_figure_button_click(figure_name)
#     Controller->>View: set_active_figure(figure_name)
#     View->>Canvas: set_shape(figure_name)
#     Controller->>View: update_figure_display(figure_name)
    
#     User->>Canvas: Нажатие кнопки мыши (ButtonPress-1)
#     Canvas->>Canvas: __on_press(event)
#     User->>Canvas: Перетаскивание мыши (B1-Motion)
#     Canvas->>Canvas: __on_drag(event)
#     Note over Canvas: Приватные методы: __on_press(), __on_drag()
#     Canvas->>Canvas: Расчет координат фигуры
#     Canvas->>Canvas: create_line(shape_points)
#     User->>Canvas: Отпускание кнопки мыши (ButtonRelease-1)
#     Canvas->>Canvas: __on_drag(event, is_filled: bool)
#     '''
#     print(translate(demo))



# import os
# import sys
# import google.generativeai as genai

# # Получаем API-ключ

# genai.configure(api_key="AIzaSyA9OhSaCjx4xpR9Ul8gPUTfX52q8ZY1W9Y")

# # Получаем запрос из аргументов
# prompt = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Привет!"

# # Выбираем модель
# model = genai.GenerativeModel("gemini-2.5-pro")

# # Отправляем запрос
# response = model.generate_content(prompt)

# # Выводим результат
# print("\n🧠 Ответ от Gemini:\n")
# print(response.text)

# def f():
#     try:
#         return 1
#     except Exception:
#         return 2
#     finally: print(3)
#
# print(f())


import tkinter as tk
from tkinter import messagebox
from enum import Enum


class CalculatorState(Enum):
    """Перечисление состояний калькулятора"""
    IDLE = "idle"
    PROCESSING = "processing"
    NORMALIZING = "normalizing"
    VALIDATING = "validating"
    CALCULATING = "calculating"
    ERROR = "error"
    RESULT = "result"


class NumberNormalizer:
    """Класс для нормализации числовых строк"""

    @staticmethod
    def normalize_number(value: str) -> str:
        """
        Нормализует строку с числом

        Args:
            value: Входная строка

        Returns:
            Нормализованная строка
        """
        if not value:
            return "0"

        result = value.strip().replace(',', '.')

        if not result:
            return "0"

        return result


class NumberValidator:
    """Класс для валидации числовых значений"""

    @staticmethod
    def is_number(value: str) -> bool:
        """
        Проверяет, является ли строка корректным числом

        Args:
            value: Строка для проверки

        Returns:
            True если строка является числом, False в противном случае
        """
        try:
            float(value)
            return True
        except ValueError:
            return False


class EntryNormalizer:
    """Класс для нормализации данных из полей ввода"""

    @staticmethod
    def normalize_entries(entry: tk.Entry) -> str:
        """
        Получает и нормализует значение из поля ввода

        Args:
            entry: Поле ввода tkinter

        Returns:
            Нормализованное значение
        """
        value = entry.get()
        return NumberNormalizer.normalize_number(value)


class CalculatorApp:
    """Главный класс приложения калькулятора"""

    def __init__(self, master: tk.Tk, amount: int = 10):
        """
        Инициализация калькулятора

        Args:
            master: Главное окно tkinter
            amount: Количество полей ввода
        """
        self.master = master
        self.amount = amount
        self.state = CalculatorState.IDLE
        self.entry_fields = []

        # Настройка окна
        self.master.title("Калькулятор")
        self.master.resizable(False, False)

        # Создание интерфейса
        self._create_widgets()

    def _create_widgets(self):
        """Создание виджетов интерфейса"""
        # Создание полей ввода и знаков плюс
        for i in range(self.amount):
            entry = tk.Entry(self.master, width=10, font=("Arial", 12))
            entry.grid(row=0, column=i * 2, padx=5, pady=10)
            self.entry_fields.append(entry)

            # Добавление знака "+" между полями (кроме последнего)
            if i < self.amount - 1:
                label_plus = tk.Label(self.master, text="+", font=("Arial", 14))
                label_plus.grid(row=0, column=i * 2 + 1)

        # Знак равно
        label_equals = tk.Label(self.master, text="=", font=("Arial", 14))
        label_equals.grid(row=0, column=self.amount * 2 - 1)

        # Поле результата
        self.result_field = tk.Entry(
            self.master,
            width=15,
            font=("Arial", 12, "bold"),
            state="readonly",
            justify="center"
        )
        self.result_field.grid(row=0, column=self.amount * 2, padx=5)

        # Кнопка вычисления
        calculate_button = tk.Button(
            self.master,
            text="Вычислить",
            command=self.calculate_plus,
            font=("Arial", 12),
            bg="#4CAF50",
            fg="white",
            padx=20,
            pady=5
        )
        calculate_button.grid(row=1, column=0, columnspan=self.amount * 2 + 1, pady=10)

        # Метка состояния (для отладки)
        self.state_label = tk.Label(
            self.master,
            text=f"Состояние: {self.state.value}",
            font=("Arial", 9),
            fg="gray"
        )
        self.state_label.grid(row=2, column=0, columnspan=self.amount * 2 + 1)

    def _set_state(self, new_state: CalculatorState):
        """
        Установка нового состояния калькулятора

        Args:
            new_state: Новое состояние
        """
        self.state = new_state
        self.state_label.config(text=f"Состояние: {self.state.value}")
        self.master.update_idletasks()

    def calculate_plus(self):
        """Основной метод вычисления суммы"""
        # Переход в состояние обработки
        self._set_state(CalculatorState.PROCESSING)

        # Нормализация ввода
        self._set_state(CalculatorState.NORMALIZING)
        normalized_values = []

        for entry in self.entry_fields:
            normalized_value = EntryNormalizer.normalize_entries(entry)
            normalized_values.append(normalized_value)

        # Валидация значений
        self._set_state(CalculatorState.VALIDATING)
        values = []

        for normalized_value in normalized_values:
            if not NumberValidator.is_number(normalized_value):
                # Переход в состояние ошибки
                self._set_state(CalculatorState.ERROR)
                messagebox.showerror(
                    "Ошибка",
                    f"Некорректное значение: '{normalized_value}'\n"
                    "Пожалуйста, введите корректные числа."
                )
                self._display_result("Ошибка")
                self._set_state(CalculatorState.IDLE)
                return

            values.append(float(normalized_value))

        # Вычисление результата
        self._set_state(CalculatorState.CALCULATING)
        result = sum(values)

        # Форматирование результата (целое число без дробной части)
        if result == int(result):
            result = int(result)

        # Отображение результата
        self._set_state(CalculatorState.RESULT)
        self._display_result(str(result))

        # Возврат в состояние ожидания
        self._set_state(CalculatorState.IDLE)

    def _display_result(self, result: str):
        """
        Отображение результата в поле результата

        Args:
            result: Строка результата для отображения
        """
        self.result_field.config(state="normal")
        self.result_field.delete(0, tk.END)
        self.result_field.insert(0, result)
        self.result_field.config(state="readonly")


def main():
    """Главная функция приложения"""
    root = tk.Tk()
    app = CalculatorApp(root, amount=11)
    root.mainloop()

#todo исправить диаграмму и код с числом во 2 ячейке
if __name__ == "__main__":
    main()
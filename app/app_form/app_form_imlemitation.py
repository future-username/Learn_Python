from app_form_interfaces import SingletonForm as _SingletonForm, Data as _Data, App as _App
from app_form_interfaces import TypeException as _TypeException
from app_form_interfaces import LabelEntry as _LabelEntry, Form as _Form, ButtonTranslate as _ButtonTranslate

from tkinter import Frame, LabelFrame, Label, Entry
import json


class TypeException(_TypeException):
    @staticmethod
    def type_error(value, type_value: type):
        raise f'{value} type not {type_value}'


class SingletonForm(_SingletonForm, type):
    def __call__(cls, *args, **kwargs):
        super().__call__(*args, **kwargs)
        pass


class LabelEntry(_LabelEntry, Frame):
    def __init__(self, parent, label_text, entry_text, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__parent = parent
        self.__label_text = label_text if isinstance(label_text, str) else TypeException.type_error(label_text, str)
        self.__entry_text = entry_text if isinstance(entry_text, str) else TypeException.type_error(entry_text, str)
        self.pack()
        self.__label = Label(self, text=self.__label_text)
        self.__label.pack()
        self.__entry = Entry(self)
        self.__entry.insert(0, entry_text)
        self.__entry.pack()

    def get_data(self):
        return {"label": self.__label_text, "entry": self.__entry.get()}




class Form(_Form, LabelFrame):
    def __init__(self, language: str, *args, **kwargs):
        self.__language = language if isinstance(language, str) else TypeException.type_error(language, str)
        super().__init__(self.__language, *args, **kwargs)
        self.pack()


    def change(self):
        pass

    def get_list_data(self) -> list:
        pass

class Data(_Data):
    def __init__(self, *args, **kwargs):
       pass

    @property
    def get_language(self, language: str) -> list:
        pass

    @get_language.setter
    def set_language(self, language: str, new_data: list[dict]):
        pass

    @property
    def languages_data(self):
        pass

    @languages_data.setter
    def languages_data(self, data: dict):
        pass

    def clean_data(self):
        pass


class ButtonTranslate(_ButtonTranslate):
    def __init__(self, parent: LabelFrame, language_name: str):
        pass

    def change_form(self):
        pass

    def pack(self, *args, **kwargs):
        pass

    def grid(self, *args, **kwargs):
        pass

    @classmethod
    def destroy(cls):
        pass

class App(_App):
    def __init__(
            self,
            title: str,
            frame_buttons_title: str = '',
            frame_form_title: str = ''
    ):
        pass

    def create_interface(self, languages: json):
        pass

    def open_file(self):
        pass

    @staticmethod
    def __save_file():
        pass

    def draw(self):
        pass

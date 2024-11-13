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
        super().__init__(language, *args, **kwargs)
        self.__language = language if isinstance(language, str) else TypeException.type_error(language, str)
        self['text'] = self.__language
        self.pack()

    def change(self):
        pass

    def get_list_data(self) -> list:
        return self.children.get()
        pass

class Data(_Data, metaclass=SingletonForm):
    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        self.__language_data = {}

    def get_language(self, language_name) -> list:
        for item in self.__language_data:
            if item['language'] == language_name:
                return item['data']

    def set_language(self, language_name: str, new_data: list[dict]):
        for index, data in enumerate(self.__language_data):
            if data['language'] == language_name:
                self.__language_data[index]['data'] = new_data

    @property
    def languages_data(self):
        return self.__language_data

    @languages_data.setter
    def languages_data(self, data: dict):
        self.__language_data = data

    def clean_data(self):
        self.__language_data.clear()


class ButtonTranslate(_ButtonTranslate):
    def __init__(self, parent: LabelFrame, language_name: str):
        self.__parent = parent
        self.__language_name = language_name


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

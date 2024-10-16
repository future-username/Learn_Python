from abc import ABC, abstractmethod
from tkinter import Frame, LabelFrame
import json


class TypeException(ABC, Exception):
    """
    Typical processing print Errors
    """

    @staticmethod
    @abstractmethod
    def type_error(value, type_value: type):
        """
        Check type of value and raise error description
        :param value: Object for check type
        :param type_value: type for check object
        """
        raise NotImplementedError()


class SingletonForm(ABC, type):
    """
    class Singleton
    """

    @abstractmethod
    def __call__(cls, *args, **kwargs):
        """
        Call Singleton
        :return: cls
        """
        raise NotImplementedError()


class Data(ABC):
    """
    class Data(metaclass=SingletonForm):
    """
    @abstractmethod
    def __init__(self, *args, **kwargs):
        """
        Language Data
        """
        raise NotImplementedError()

    @abstractmethod
    def get_language(self, language: str) -> list:
        """
        Get language from data
        :param language: language name to get data from current
        :return: language data
        """
        raise NotImplementedError()

    @abstractmethod
    def set_language(self, language: str, new_data: list[dict]):
        """
        Load new language data to data class
        :param language: language name
        :param new_data: language data
        """
        raise NotImplementedError()

    @property
    @abstractmethod
    def languages_data(self):
        """
        Get all languages data
        :return: languages_data
        """
        raise NotImplementedError()

    @languages_data.setter
    @abstractmethod
    def languages_data(self, data: dict):
        """
        Set new languages_data
        :param data: set languages_data
        """
        raise NotImplementedError()

    @abstractmethod
    def clean_data(self):
        """
        Clean data
        """
        raise NotImplementedError()


class LabelEntry(ABC, Frame):
    """
    LabelEntry is one widget line form
    """
    # noinspection PyUnusedLocal
    @abstractmethod
    def __init__(self, parent, label_text: str, entry_text: str, *args, **kwargs):
        """
        LabelEntry building
        :param parent:
        :param label_text: text to Label
        :param entry_text: text to Entry
        """
        super().__init__(*args, **kwargs)
        raise NotImplementedError()

    @abstractmethod
    def get_data(self) -> dict[str: str]:
        """
        Get data from LabelEntry
        :return: label and entry in dict
        """
        raise NotImplementedError()


class Form(ABC, LabelFrame):
    # noinspection PyUnusedLocal
    @abstractmethod
    def __init__(self, language: str, *args, **kwargs):
        """
        Form data
        :param language: current language form
        """
        super().__init__(*args, **kwargs)
        raise NotImplementedError()

    @abstractmethod
    def change(self):
        """
        Change language name
        """
        raise NotImplementedError()

    @abstractmethod
    def get_list_data(self) -> list:
        """
        Get data from label entries
        """
        raise NotImplementedError()


class ButtonTranslate(ABC):
    # noinspection PyUnusedLocal
    @abstractmethod
    def __init__(self, parent: LabelFrame, language_name: str):
        """
        Buttons make translate form
        :param parent: LabelFrame in which they are stored buttons
        :param language_name: language to translate form
        """
        raise NotImplementedError()

    @abstractmethod
    def change_form(self):
        """
        Change form to another language
        """
        raise NotImplementedError()

    @abstractmethod
    def pack(self, *args, **kwargs):
        """
        Pack button
        """
        raise NotImplementedError()

    @abstractmethod
    def grid(self, *args, **kwargs):
        """
        Grid button
        """
        raise NotImplementedError()

    @classmethod
    @abstractmethod
    def destroy(cls):
        """
        Destroy form
        """
        raise NotImplementedError()


class App(ABC):
    # noinspection PyUnusedLocal
    @abstractmethod
    def __init__(
            self,
            title: str,
            frame_buttons_title: str = '',
            frame_form_title: str = ''
    ):
        """
        App
        :param title: form title
        :param frame_buttons_title: the title from frame in buttons which translate
        :param frame_form_title: the title language form
        """
        raise NotImplementedError()

    @abstractmethod
    def create_interface(self, languages: json):
        """
        Create interface form
        :param languages: json from form data with label and entries
        """
        raise NotImplementedError()

    @abstractmethod
    def open_file(self):
        """
        Open file and add data to Labels
        """
        raise NotImplementedError()

    @staticmethod
    @abstractmethod
    def __save_file():
        """
        Save file or update current
        """
        raise NotImplementedError()

    @abstractmethod
    def draw(self):
        """
        Draw form
        """
        raise NotImplementedError()

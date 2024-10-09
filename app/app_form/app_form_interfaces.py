from abc import ABC, abstractmethod
from tkinter import Frame, LabelFrame


class Errors(ABC):
    """
    Typical processing print Errors
    """

    @staticmethod
    @abstractmethod
    def type_error(value, type_value: type):
        """
        Check type of value and print error description
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


class Data(ABC, metaclass=SingletonForm):
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

    @abstractmethod
    @property
    def languages_data(self):
        """
        Get all languages data
        :return: languages_data
        """
        raise NotImplementedError()

    @abstractmethod
    @languages_data.setter
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
    @abstractmethod
    def __init__(self, parent, label_text: str, entry_text: str, *args, **kwargs):
        """
        LabelEntry
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
    def __init__(self, language: str, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__language = language
        self['text'] = self.__language
        self.pack()

        self.__label_entries: LabelEntry | list = []

    def change(self):
        for label in Data().get_language(self.__language):
            label = LabelEntry(self, label['label'], label['entry'])
            label.pack(fill=X)
            self.__label_entries.append(label)

        Data().language_name = self.__language

    def get_list_data(self) -> list:
        result = []
        for label in self.__label_entries:
            result.append(label.get_data())
        return result


class ButtonTranslate:
    __previous_form: Form | None = None

    def __init__(self, parent: LabelFrame, language_name: str):
        self.parent = parent if isinstance(parent, LabelFrame) else Errors.type_error(parent, LabelFrame)
        self.language_name = language_name

        self.button = Button(parent, text=language_name, fg="black", command=self.change_form)

        self.__data_list: list[dict] = []
        self.__data_dict = {}

    def change_form(self):
        if self.__class__.__previous_form:
            Data().set_language(Data().language_name, self.__class__.__previous_form.get_list_data())
            self.__class__.__previous_form.destroy()

        form = Form(self.language_name)
        form.change()
        self.__class__.__previous_form = form

    def pack(self, *args, **kwargs):
        """
        Pack button
        :param args:
        :param kwargs:
        :return:
        """
        self.button.pack(*args, **kwargs)

    def grid(self, *args, **kwargs):
        """
        Grid button
        :param args:
        :param kwargs:
        :return:
        """
        self.button.grid(*args, **kwargs)

    @classmethod
    def destroy(cls):
        if cls.__previous_form:
            cls.__previous_form.destroy()
            cls.__previous_form = None


class App:
    def __init__(
            self,
            title: str,
            frame_buttons_title: str = '',
            frame_form_title: str = ''
    ):
        self.frame_buttons_title = frame_buttons_title if isinstance(frame_buttons_title, str) \
            else Errors.type_error(frame_buttons_title, str)
        self.frame_form_title = frame_form_title if isinstance(frame_form_title, str) \
            else Errors.type_error(frame_form_title, str)

        self.__frame_buttons = None

        self.root = Tk()
        None if isinstance(title, str) else Errors.type_error(title, str)
        self.root.title(title)
        frame_menu = Frame()
        frame_menu.pack()
        Button(frame_menu, text='Open', fg="black", command=self.__open_file).pack(side=LEFT)
        Button(frame_menu, text='Save', fg="black", command=self.__save_file).pack(side=RIGHT)

    def __create_interface(self, languages: json):
        self.__frame_buttons = LabelFrame(text=self.frame_buttons_title)
        self.__frame_buttons.pack()

        Data().languages_data = languages
        for index, language in enumerate(languages):
            _ = ButtonTranslate(self.__frame_buttons, language["language"])
            _.pack(side=LEFT)
            _.change_form() if index == 0 else None

    def __open_file(self):
        """
        Open file and add data to Labels
        :return: None
        """
        ButtonTranslate.destroy()
        self.__frame_buttons.destroy() if self.__frame_buttons else None
        Data().clean_data()

        file_name = filedialog.askopenfilename(filetypes=[("json files", '*.json')])
        if file_name:
            with open(file_name, 'r', encoding='UTF-8') as file:
                file_data = json.load(file)
            try:
                self.__create_interface(file_data) if file_data else None
            except TypeError:
                messagebox.showerror(message='Open file with form')

    @staticmethod
    def __save_file():
        data = Data().get_languages_data()
        file_name = filedialog.asksaveasfilename(
            defaultextension='.json', filetypes=[("json files", '*.json')],
            title="Choose filename")
        if file_name:
            with open(file_name, 'w', encoding='UTF-8') as file:
                file.write(json.dumps(list(data), indent=4))

    def draw(self):
        self.root.mainloop()

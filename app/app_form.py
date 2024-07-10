# from tkinter import *
#
#
# def translate_label():
#     label_name.config(text="Имя:")
#     label_surname.config(text="Фамилия:")
#     label_year.config(text="Год рождения:")
#
#
# root = Tk()
# root.title("GUI на Python")
# root.geometry("235x130")
#
# label_name = Label(root, text="Name:", fg="black")
# label_name.place(x=10, y=10)
#
# entry_name = Entry(root, bg="white")
# entry_name.place(x=100, y=10)
#
# label_surname = Label(root, text="Surname:", fg="black")
# label_surname.place(x=10, y=40)
#
# entry_surname = Entry(root, bg="white")
# entry_surname.place(x=100, y=40)
#
# label_year = Label(root, text="Year:", fg="black")
# label_year.place(x=10, y=70)
#
# entry_year = Entry(root, bg="white")
# entry_year.place(x=100, y=70)
#
# button_translate = Button(root, text="Russia", fg="black", command=translate_label)
# button_translate.place(x=100, y=100)
#
# root.mainloop()


# from tkinter import *
#
#
# label_ru = ['Имя:', 'Фамилия:', 'Год рождения:', 'Город:', 'Телефон:', 'Почта:']
# label_en = ["Name:", "Surname:", "Year:", 'City:', "Phone:", "Mail:"]
# widget_labels = []
#
#
# def translate_label():
#     i = 0
#     if button_translate['text'] == 'Russia':
#         for n in range(len(label_en)):
#             widget_labels[i].config(text=label_ru[i])
#             i += 1
#         button_translate.config(text="English")
#     else:
#         for n in range(len(label_en)):
#             widget_labels[i].config(text=label_en[i])
#             i += 1
#         button_translate.config(text="Russia")
#
#
# root = Tk()
# root.title("GUI на Python")
# root.geometry(f"300x{len(label_en)*25+60}")
#
# for i in range(len(label_en)):
#     label_name = Label(root, text=label_en[i], fg="black")
#     label_name.place(x=10, y=25*i+15)
#     widget_labels.append(label_name)
#     entry_name = Entry(root, bg="white")
#     entry_name.place(x=100, y=25*i+15)
# button_translate = Button(root, text="Russia", fg="black", command=translate_label)
# button_translate.place(x=100, y=len(label_en)*25+25)
#
# root.mainloop()


# from tkinter import *
#
# languages = {
#     "Русский": ['Имя:', 'Фамилия:', 'Отчество:', 'Год рождения:', 'Город:', 'Телефон:', 'Почта:'],
#     "English": ["Name:", "Surname:", "Year:", 'City:', "Phone:", "Mail:"],
#     "Türkçe": ['Ad:', 'Soyadı:', 'Doğum Yılı:', 'Şehir:', 'Telefon:', 'E-posta:']
# }
#
#
# def translate_label(language: str):
#     root.winfo_children()[1].destroy() if len(root.winfo_children()) > 1 else None
#
#     frame_form = LabelFrame()
#     frame_form.pack()
#
#     for index, text in enumerate(languages[language]):
#         label_name = Label(frame_form, text=text, fg="black")
#         label_name.grid(column=0, row=1 + index)
#         entry_name = Entry(frame_form, bg="white")
#         entry_name.grid(column=1, row=1 + index)
#
#
# root = Tk()
# root.title("GUI на Python")
#
# frame_buttons = LabelFrame(text='Translate')
# frame_buttons.pack()
#
#
# for index, language in enumerate(languages.keys()):
#     button_translate = Button(frame_buttons, text=language, fg="black", command=lambda l=language: translate_label(l))
#     button_translate.grid(column=index, row=len(languages['Русский']))
#
# translate_label('Русский')
#
# root.mainloop()


# from tkinter import *
# from typing import Dict, List
#
# LANGUAGES = {
#     "Русский": [{'Имя:': "", 'Фамилия:': "", 'Отчество:': "", 'Год рождения:': "", 'Город:': "", 'Телефон:': "", 'Почта:': ""}],
#     "English": [{"Name:": "", "Surname:": "", "Year:": "", 'City:': "", "Phone:": "", "Mail:": ""}],
#     "Türkçe": [{'Ad:': "", 'Soyadı:': "", 'Doğum Yılı:': "", 'Şehir:': "", 'Telefon:': "", 'E-posta:': ""}]
# }
#
#
# class Errors:
#     @staticmethod
#     def type_error(value, type_value):
#         raise TypeError(f'{value} this is not {type_value}')
#
#
# class LabelEntry:
#     def __init__(self, parent, text):
#         """
#
#         :param parent:
#         :param text:
#         """
#         self.frame = Frame(parent)
#         self.label = Label(master=self.frame, text=text, fg="black")
#         self.entry = Entry(master=self.frame, bg="white")
#
#     def pack(self, *args, **kwargs):
#         """
#         Pack frame
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         self.frame.pack(*args, **kwargs)
#         self.label.pack(side=LEFT)
#         self.entry.pack(side=RIGHT)
#
#     def grid(self, *args, **kwargs):
#         """
#         Grid frame
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         self.frame.grid(*args, **kwargs)
#         self.label.pack(side=LEFT)
#         self.entry.pack(side=RIGHT)
#
#
# class ButtonTranslate:
#     def __init__(self, parent: LabelFrame, language: str, labels: list, frame: LabelFrame):
#         parent = parent if isinstance(parent, LabelFrame) else Errors.type_error(parent, LabelFrame)
#         language = language if isinstance(language, str) else Errors.type_error(language, str)
#         self.labels = labels if isinstance(labels, list) else Errors.type_error(labels, list)
#         self.frame = frame if isinstance(frame, LabelFrame) else Errors.type_error(frame, LabelFrame)
#
#         self.button = Button(parent, text=language, fg="black", command=self.translate_label)
#
#     def translate_label(self):
#         for widget in self.frame.winfo_children():
#             widget.destroy()
#
#         for text in self.labels:
#             LabelEntry(self.frame, text).pack(fill=X)
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
#             languages: Dict[str, List[str]],
#             frame_buttons_title: str = '',
#             frame_form_title: str = ''
#     ):
#         None if isinstance(languages, dict) else Errors.type_error(languages, dict)
#         for key in languages.keys():
#             None if isinstance(key, str) else Errors.type_error(key, str)
#
#         for value in languages.values():
#             None if isinstance(value, list) else Errors.type_error(value, list)
#             for value_in_list in value:
#                 None if isinstance(value_in_list, str) else Errors.type_error(value_in_list, str)
#
#         self.root = Tk()
#         None if isinstance(title, str) else Errors.type_error(title, str)
#         self.root.title(title)
#
#         None if isinstance(frame_buttons_title, str) else Errors.type_error(frame_buttons_title, str)
#         frame_buttons = LabelFrame(text=frame_buttons_title)
#         frame_buttons.pack()
#
#         None if isinstance(frame_form_title, str) else Errors.type_error(frame_form_title, str)
#         frame_form = LabelFrame(text=frame_form_title)
#         frame_form.pack()
#
#         for index, language in enumerate(languages.keys()):
#             _ = ButtonTranslate(frame_buttons, language, languages[language], frame_form)
#             _.grid(column=index, row=len(languages['Русский']))
#             _.translate_label() if index == 0 else None
#
#     def draw(self):
#         self.root.mainloop()
#
#
# if __name__ == '__main__':
#     App(title="Form", languages=LANGUAGES, frame_buttons_title='Translate').draw()


from tkinter import *
from tkinter import filedialog
import json


class Errors:
    @staticmethod
    def type_error(value, type_value):
        raise TypeError(f'{value} this is not {type_value}')


class SingletonForm(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Data(metaclass=SingletonForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__languages_data: dict = {}
        self.language_name = ''

    def get_language(self, language: str) -> list:
        for item in self.__languages_data:
            if item["language"] == language:
                return item['data']

    def set_language(self, language: str, new_data: list[dict]):
        for index, data in enumerate(self.__languages_data):
            if data["language"] == language:
                self.languages_data[index]['data'] = new_data

    def get_languages_data(self) -> dict:
        return self.__languages_data

    @property
    def languages_data(self):
        return self.__languages_data

    @languages_data.setter
    def languages_data(self, data: dict) -> None:
        self.__languages_data = data

    def clean_data(self):
        self.__languages_data.clear()


class LabelEntry(Frame):
    def __init__(self, parent, label_text: str, entry_text: str, *args, **kwargs):
        """
        :param parent:
        :param label_text: str
        :param entry_text: str
        """
        super().__init__(parent, *args, **kwargs)

        self.__entry = Entry(master=self, bg="white")
        self.__entry.insert(0, entry_text)
        self.__entry.pack(side=RIGHT)

        self.__label = Label(master=self, text=label_text, fg="black")
        self.__label.pack(side=LEFT)

    def get_data(self) -> dict[str: str]:
        return {'label': self.__label['text'], 'entry': self.__entry.get()}


class Form(LabelFrame):
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
        print(self.__class__.__previous_form)
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
            _.grid(column=index, row=len(language["data"]))
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
            self.__create_interface(file_data) if file_data else None

    @staticmethod
    def __save_file():
        data = Data().get_languages_data()
        file_name = filedialog.asksaveasfilename(
            defaultextension='.json', filetypes=[("json files", '*.json')],
            title="Choose filename")
        if file_name:
            with open(file_name, 'w', encoding='UTF-8') as file:
                file.write(json.dumps(list(data)))

    def draw(self):
        self.root.mainloop()


if __name__ == '__main__':
    App(title="Form", frame_buttons_title='Translate').draw()

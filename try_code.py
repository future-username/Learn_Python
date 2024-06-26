# from tkinter import *
# from random import randrange
#
# flag = True
#
#
# class SingletonFrame(type):
#     _instances: dict[str, LabelFrame] = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             instance = super().__call__(*args, **kwargs)
#             cls._instances[cls] = instance
#         return cls._instances[cls]
#
#
# class MyStringVar(metaclass=SingletonFrame):
#     def __init__(self, field, *args, **kwargs):
#         self.field = field
#         super().__init__(*args, **kwargs)
#         self.data = randrange(100)
#         # root.bind('<Key>', self.set_data)
#
#     def set_data(self, _):
#         print(self.field['background'])
#         self.data = self.field.get()
#
#
# def change_entry():
#     global flag, entry1, entry
#     if flag:
#         # entry1.pack_forget()
#         entry1.destroy()
#         # entry.pack()
#         entry = Entry()
#         entry.pack()
#         entry.insert(0, string_var.data)
#     else:
#         # entry1.pack()
#         entry1 = Entry()
#         entry1.pack()
#         # entry.pack_forget()
#         entry.destroy()
#         entry1.insert(0, string_var.data)
#     flag = not flag
#     print(MyStringVar().data)
#
#
# root = Tk()
# entry = Entry(background='yellow')
# string_var = MyStringVar(entry)
# entry.insert(0, string_var.data)
# # entry.pack()
# entry1 = Entry()
# string_var = MyStringVar(entry)
# entry1.insert(0, string_var.data)
# root.bind('<Key>', string_var.set_data)
# # entry1.pack()
# Button(text='1', command=change_entry).pack()
#
# root.mainloop()


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

    def set_language(self, language: str, data: list[dict]):
        for index, data in enumerate(self.__languages_data):
            if data["language"] == language:
                self.languages_data[index]['data'] = data

    @property
    def languages_data(self):
        return self.__languages_data

    @languages_data.setter
    def languages_data(self, data: dict) -> None:
        self.__languages_data = data


class LabelEntry(Frame):
    def __init__(self, parent, label_text: str, entry_text: str, *args, **kwargs):
        """
        :param parent:
        :param label_text: str
        :param entry_text: str
        """
        super().__init__(*args, **kwargs)
        self.__frame = Frame(parent)

        self.__entry = Entry(master=self.__frame, bg="white")
        self.__entry.insert(0, entry_text)
        self.__entry.pack(side=RIGHT)

        Label(master=self.__frame, text=label_text, fg="black").pack(side=LEFT)
        self.__frame.pack(fill=X)

    def get_data(self) -> str:
        return self.__entry.get()


class Form(LabelFrame):
    def __init__(self, language: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.__language_name = language_name if isinstance(language_name, str) \
        #     else Errors.type_error(language_name, str)
        # self.__frame = frame

        self.__language = language
        self['text'] = self.__language
        self.__data_list: list[dict] = []
        self.__data_dict = {}
        self.pack()

    def change(self):
        for widget in self.winfo_children():
            self.__save_data(widget, Data().language_name)
        for label in Data().get_language(self.__language):
            LabelEntry(self, label['label'], label['entry'])
        Data().language_name = self.__language

    def __save_data(self, data: Widget, language) -> None:
        temp = {}
        for element in data.winfo_children():
            if isinstance(element, Label):
                temp['label'] = element['text']
                self.__data_list.append(temp)
                temp = {}
            if isinstance(element, Entry):
                temp['entry'] = element.get()

        name = language if not Data().language_name else Data().language_name
        Data().set_language(name, self.__data_list)


win = None


class ButtonTranslate:
    __previous_form_1 = None

    def __init__(self, parent: LabelFrame, language_name: str):
        self.parent = parent if isinstance(parent, LabelFrame) else Errors.type_error(parent, LabelFrame)
        self.language_name = language_name
        # self.frame = frame if isinstance(frame, LabelFrame) else Errors.type_error(frame, LabelFrame)
        self.data_list: list[dict] = []

        self.button = Button(parent, text=language_name, fg="black", command=self.translate_label)
        print(self.__previous_form_1)

    def translate_label(self):
        self.__class__.__previous_form_1.destroy() if self.__class__.__previous_form_1 else None
        f = Form(self.language_name)
        f.change()
        self.__class__.__previous_form_1 = f
        # Form(self.frame, self.language_name).change()
        print(win.winfo_children(), '\n')

        # for label in Data().get_language(self.language_name):
        #     LabelEntry(self.frame, label['label'], label['entry']).pack(fill=X)

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


class App:
    def __init__(
            self,
            title: str,
            frame_buttons_title: str = '',
            frame_form_title: str = ''
    ):
        global win
        self.frame_buttons_title = frame_buttons_title if isinstance(frame_buttons_title, str) \
            else Errors.type_error(frame_buttons_title, str)
        self.frame_form_title = frame_form_title if isinstance(frame_form_title, str) \
            else Errors.type_error(frame_form_title, str)
        # None if isinstance(languages, json) else Errors.type_error(languages, dict)
        # for key in languages.keys():
        #     None if isinstance(key, str) else Errors.type_error(key, str)
        #
        # for value in languages.values():
        #     None if isinstance(value, list) else Errors.type_error(value, list)
        #     for value_in_list in value:
        #         None if isinstance(value_in_list, str) else Errors.type_error(value_in_list, str)

        self.root = Tk()
        win = self.root
        None if isinstance(title, str) else Errors.type_error(title, str)
        self.root.title(title)
        frame_menu = Frame()
        frame_menu.pack()
        Button(frame_menu, text='Open', fg="black", command=self.__open_file).pack(side=LEFT)
        Button(frame_menu, text='Save', fg="black").pack(side=RIGHT)

    def __create_interface(self, languages: json):
        frame_buttons = LabelFrame(text=self.frame_buttons_title)
        frame_buttons.pack()

        # frame_form = LabelFrame(text=self.frame_form_title)
        # frame_form.pack()
        Data().languages_data = languages
        for index, language in enumerate(languages):
            _ = ButtonTranslate(frame_buttons, language["language"])
            _.grid(column=index, row=len(language["data"]))
            _.translate_label() if index == 0 else None

    def __open_file(self):
        """
        Open file and add data to Labels
        :return: None
        """
        file_name = filedialog.askopenfilename(filetypes=[("json files", '*.json')])
        if file_name:
            with open(file_name, 'r', encoding='UTF-8') as file:
                file_data = json.load(file)
            self.__create_interface(file_data) if file_data else None

    # def __save_file(self):
    #     data = {
    #
    #     }
    #     file_name = filedialog.asksaveasfilename(
    #         defaultextension='.json', filetypes=[("json files", '*.json')],
    #         title="Choose filename")
    #     if file_name:
    #         with open(file_name, 'w', encoding='UTF-8') as file:
    #             file.write(json.dumps(data))

    def draw(self):
        self.root.mainloop()


if __name__ == '__main__':
    App(title="Form", frame_buttons_title='Translate').draw()

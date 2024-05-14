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
        for language_data in self.language_data:
            if language_data["language"] == language:
                return language_data['data']

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


class LabelEntry:
    def __init__(self, parent, label_text: str, entry_text: str):
        """

        :param parent:
        :param label_text: str
        :param entry_text: str
        """
        self.frame = Frame(parent)
        self.label = Label(master=self.frame, text=label_text, fg="black")
        self.entry = Entry(master=self.frame, bg="white")
        self.entry.insert(0, entry_text)

    def pack(self, *args, **kwargs):
        """
        Pack frame
        :param args:
        :param kwargs:
        :return:
        """
        self.frame.pack(*args, **kwargs)
        self.label.pack(side=LEFT)
        self.entry.pack(side=RIGHT)

    def grid(self, *args, **kwargs):
        """
        Grid frame
        :param args:
        :param kwargs:
        :return:
        """
        self.frame.grid(*args, **kwargs)
        self.label.pack(side=LEFT)
        self.entry.pack(side=RIGHT)


class ButtonTranslate:
    # def __init__(self, parent: LabelFrame, language: str, labels: list, frame: LabelFrame):
    def __init__(self, parent: LabelFrame, language_name: str, languages_data: list, frame: LabelFrame):
        parent = parent if isinstance(parent, LabelFrame) else Errors.type_error(parent, LabelFrame)
        # self.language = language if isinstance(language, str) else Errors.type_error(language, str)
        # self.labels = labels if isinstance(labels, list) else Errors.type_error(labels, list)
        # self.languages_data = languages_data if isinstance(languages_data, list) else Errors.type_error(languages_data,
        #                                                                                                 list)
        self.language_name = language_name
        Data().language_name = self.language_name
        self.frame = frame if isinstance(frame, LabelFrame) else Errors.type_error(frame, LabelFrame)
        self.data_list: list[dict] = []

        self.button = Button(parent, text=language_name, fg="black", command=self.translate_label)

    # def generate_lines(self):
    #     for widget in self.dict_frames.items().winfo_children():
    #         widget.pack_forget()
    #     for label in self.labels:
    #         LabelEntry(self.frame, label['label'], label['entry']).pack(fill=X)
    #     self.dict_frames[self.language] = self.frame
    #     self.frame.pack_forget()

    # def save_data(self, data: Widget) -> None:
    #     data_dict = {}
    #     if not self.data_list:
    #         self.data_list.update({'language': Data().language})
    #         self.data_list.update({"data": []})
    #     for language_data in Data().language_data:
    #         if language_data["language"] == Data().language:
    #             for element, language in zip(data.winfo_children(), language_data["data"]):
    #                 if isinstance(element, Entry):
    #                     data_dict['entry'] = element.get()
    #                 else:
    #                     data_dict['label'] = element['text']
    #
    #             if len(data_dict.keys()) > 1:
    #                 self.data_list['data'].append(data_dict)
    #                 # print(self.data_list)
    #                 break
    #                 # data_dict = {}

    def save_data(self, data: Widget) -> None:
        data_dict = {}

        for element in data.winfo_children():
            if 'label' in data_dict.keys():
                self.data_list.append(data_dict)
                data_dict.clear()
            if isinstance(element, Entry):
                data_dict['entry'] = element.get()
            else:
                data_dict['label'] = element['text']

        Data().set_language(Data().language_name, self.data_list)

    # def update_data(self) -> None:
    #     index_dict = 0
    #     for index, language_data in enumerate(Data().language_data):
    #         if language_data["language"] == Data().language:
    #             index_dict = index
    #     # print(self.data_list)
    #     # print("\n" * 2)
    #     # print(Data().language_data[index_dict])
    #     print(Data().language_data[index_dict]['data'])
    #     Data().language_data[index_dict]['data'].clear()
    #     Data().language_data[index_dict]['data'].append(self.data_list)
    #     # print(Data().language, Data().language_data[index_dict])

    def delete_current_widget(self):
        for _ in self.frame.winfo_children():
            self.data_list.clear()
        for widget in self.frame.winfo_children():
            self.save_data(widget)
        for widget in self.frame.winfo_children():
            widget.destroy()

    def translate_label(self):
        self.delete_current_widget()

        for data in Data().languages_data:
            if data["language"] == self.language_name:
                for label in data["data"]:
                    LabelEntry(self.frame, label['label'], label['entry']).pack(fill=X)
        Data().language_name = self.language_name


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
        None if isinstance(title, str) else Errors.type_error(title, str)
        self.root.title(title)
        frame_menu = Frame()
        frame_menu.pack()
        Button(frame_menu, text='Open', fg="black", command=self.__open_file).pack(side=LEFT)
        Button(frame_menu, text='Save', fg="black").pack(side=RIGHT)

    def __create_interface(self, languages: json):
        frame_buttons = LabelFrame(text=self.frame_buttons_title)
        frame_buttons.pack()

        frame_form = LabelFrame(text=self.frame_form_title)
        frame_form.pack()
        Data().languages_data = languages
        for index, language in enumerate(languages):
            _ = ButtonTranslate(frame_buttons, language["language"], language["data"], frame_form)
            _ = ButtonTranslate(frame_buttons, language["language"], languages, frame_form)
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

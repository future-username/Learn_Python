from tkinter import *
from random import randrange

flag = True


class SingletonFrame(type):
    _instances: dict[str, LabelFrame] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class MyStringVar(metaclass=SingletonFrame):
    def __init__(self, field, *args, **kwargs):
        self.field = field
        super().__init__(*args, **kwargs)
        self.data = randrange(100)
        # root.bind('<Key>', self.set_data)

    def set_data(self, _):
        print(self.field['background'])
        self.data = self.field.get()


def change_entry():
    global flag, entry1, entry
    if flag:
        # entry1.pack_forget()
        entry1.destroy()
        # entry.pack()
        entry = Entry()
        entry.pack()
        entry.insert(0, string_var.data)
    else:
        # entry1.pack()
        entry1 = Entry()
        entry1.pack()
        # entry.pack_forget()
        entry.destroy()
        entry1.insert(0, string_var.data)
    flag = not flag
    print(MyStringVar().data)


root = Tk()
entry = Entry(background='yellow')
string_var = MyStringVar(entry)
entry.insert(0, string_var.data)
# entry.pack()
entry1 = Entry()
string_var = MyStringVar(entry)
entry1.insert(0, string_var.data)
root.bind('<Key>', string_var.set_data)
# entry1.pack()
Button(text='1', command=change_entry).pack()

root.mainloop()

# from tkinter import *
# from tkinter import filedialog
# import json
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
# class LabelEntry:
#     def __init__(self, parent, label_text: str, entry_text: str, _=None):
#         """
#
#         :param parent:
#         :param label_text: str
#         :param entry_text: str
#         """
#         self.__frame = Frame(parent)
#         self.__label = Label(master=self.__frame, text=label_text, fg="black")
#         self.__entry = Entry(master=self.__frame, bg="white")
#         self.__entry.insert(0, entry_text)
#
#     def pack(self, *args, **kwargs):
#         """
#         Pack frame
#         :param args:
#         :param kwargs:
#         :return:
#         """
#         self.__frame.pack(*args, **kwargs)
#         self.__label.pack(side=LEFT)
#         self.__entry.pack(side=RIGHT)
#
#     # def grid(self, *args, **kwargs):
#     #     """
#     #     Grid frame
#     #     :param args:
#     #     :param kwargs:
#     #     :return:
#     #     """
#     #     # self.frame.grid(*args, **kwargs)
#     #     self.label.pack(side=LEFT)
#     #     self.entry.pack(side=RIGHT)
#
#
# class Form:
#     def __init__(self, parent: LabelFrame, language: str, labels: list, frame: LabelFrame):
#         parent = parent if isinstance(parent, LabelFrame) else Errors.type_error(parent, LabelFrame)
#         self.__language = language if isinstance(language, str) else Errors.type_error(language, str)
#         self.__labels = labels if isinstance(labels, list) else Errors.type_error(labels, list)
#         self.__frame = frame if isinstance(frame, LabelFrame) else Errors.type_error(frame, LabelFrame)
#         # self.__dict_frames: dict[str, LabelFrame] = {}
#
#         self.button = Button(parent, text=language, fg="black", command=self.generate_lines)
#
#     def generate_lines(self):
#         for widget in self.dict_frames.items().winfo_children():
#             widget.pack_forget()
#         for label in self.__labels:
#             LabelEntry(self.__frame, label['label'], label['entry']).pack(fill=X)
#         self.__dict_frames[self.__language] = self.__frame
#         self.__frame.pack_forget()
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
# class Data(metaclass=SingletonForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#
# class Errors:
#     @staticmethod
#     def type_error(value, type_value):
#         raise TypeError(f'{value} this is not {type_value}')
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
#         frame_form = LabelFrame(text=self.frame_form_title)
#         frame_form.pack()
#
#         for index, language in enumerate(languages):
#             _ = Form(frame_buttons, language["language"], language["data"], frame_form)
#             _.grid(column=index, row=len(language["data"]))
#             _.generate_lines() if index == 0 else None
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
#     def __save_file(self):
#         data = {
#
#         }
#         FILE_PATH = filedialog.asksaveasfilename(
#             defaultextension='.json', filetypes=[("json files", '*.json')],
#             title="Choose filename")
#         if FILE_PATH:
#             with open(FILE_PATH, 'w', encoding='UTF-8') as file:
#                 file.write(json.dumps(data))
#
#     def draw(self):
#         self.root.mainloop()
#
#
# if __name__ == '__main__':
#     App(title="Form", frame_buttons_title='Translate').draw()

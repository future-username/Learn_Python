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


from tkinter import *
from typing import Dict, List

LANGUAGES = {
    "Русский": ['Имя:', 'Фамилия:', 'Отчество:', 'Год рождения:', 'Город:', 'Телефон:', 'Почта:'],
    "English": ["Name:", "Surname:", "Year:", 'City:', "Phone:", "Mail:"],
    "Türkçe": ['Ad:', 'Soyadı:', 'Doğum Yılı:', 'Şehir:', 'Telefon:', 'E-posta:']
}


class Errors:
    @staticmethod
    def type_error(value, type_value):
        raise TypeError(f'{value} this is not {type_value}')


class LabelEntry:
    def __init__(self, parent, text):
        """

        :param parent:
        :param text:
        """
        self.frame = Frame(parent)
        self.label = Label(master=self.frame, text=text, fg="black")
        self.entry = Entry(master=self.frame, bg="white")

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
    def __init__(self, parent: LabelFrame, language: str, labels: list, frame: LabelFrame):
        parent = parent if isinstance(parent, LabelFrame) else Errors.type_error(parent, LabelFrame)
        language = language if isinstance(language, str) else Errors.type_error(language, str)
        self.labels = labels if isinstance(labels, list) else Errors.type_error(labels, list)
        self.frame = frame if isinstance(frame, LabelFrame) else Errors.type_error(frame, LabelFrame)

        self.button = Button(parent, text=language, fg="black", command=self.translate_label)

    def translate_label(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

        for text in self.labels:
            LabelEntry(self.frame, text).pack(fill=X)

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
            languages: Dict[str, List[str]],
            frame_buttons_title: str = '',
            frame_form_title: str = ''
    ):
        None if isinstance(languages, dict) else Errors.type_error(languages, dict)
        for key in languages.keys():
            None if isinstance(key, str) else Errors.type_error(key, str)

        for value in languages.values():
            None if isinstance(value, list) else Errors.type_error(value, list)
            for value_in_list in value:
                None if isinstance(value_in_list, str) else Errors.type_error(value_in_list, str)

        self.root = Tk()
        None if isinstance(title, str) else Errors.type_error(title, str)
        self.root.title(title)

        None if isinstance(frame_buttons_title, str) else Errors.type_error(frame_buttons_title, str)
        frame_buttons = LabelFrame(text=frame_buttons_title)
        frame_buttons.pack()

        None if isinstance(frame_form_title, str) else Errors.type_error(frame_form_title, str)
        frame_form = LabelFrame(text=frame_form_title)
        frame_form.pack()

        for index, language in enumerate(languages.keys()):
            _ = ButtonTranslate(frame_buttons, language, languages[language], frame_form)
            _.grid(column=index, row=len(languages['Русский']))
            _.translate_label() if index == 0 else None

    def draw(self):
        self.root.mainloop()


if __name__ == '__main__':
    App(title="Form", languages=LANGUAGES, frame_buttons_title='Translate').draw()

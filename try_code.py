from tkinter import *


class SingletonFrame(type):
    _instances: dict[str, LabelFrame] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class ButtonTranslate(metaclass=SingletonFrame):
    def __init__(self, parent: LabelFrame, language: str, labels: list, frame: LabelFrame):
        parent = parent if isinstance(parent, LabelFrame) else Errors.type_error(parent, LabelFrame)
        self.language = language if isinstance(language, str) else Errors.type_error(language, str)
        self.labels = labels if isinstance(labels, list) else Errors.type_error(labels, list)
        self.frame = frame if isinstance(frame, LabelFrame) else Errors.type_error(frame, LabelFrame)
        self.dict_frames: dict[str, LabelFrame] = {}

        self.button = Button(parent, text=language, fg="black", command=self.translate_label)

    def generate_lines(self):
        for widget in self.dict_frames.items().winfo_children():
            widget.pack_forget()
        for label in self.labels:
            LabelEntry(self.frame, label['label'], label['entry']).pack(fill=X)
        self.dict_frames[self.language] = self.frame
        self.frame.pack_forget()


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


class Errors:
    @staticmethod
    def type_error(value, type_value):
        raise TypeError(f'{value} this is not {type_value}')

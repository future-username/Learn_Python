# from tkinter import *
#
# root = Tk()
# root.title("Welcome to entry app")
# txt = Entry(root, width=50)
# txt.pack()
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# root.title("Welcome to the second entry app")
# txt1 = Entry(root, width=20)
# txt1.pack()
# txt2 = Entry(root, width=50)
# txt2.pack()
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# root.title("Welcome to the second entry app")
# lbl_login = Label(root, text="Login")
# lbl_login.pack()
# txt1 = Entry(root, width=50)
# txt1.pack()
# lbl_pass = Label(root, text="Password")
# lbl_pass.pack()
# txt2 = Entry(root, width=50)
# txt2.pack()
# btn = Button(root, text="Enter")
# btn.pack()
# root.mainloop()


# from tkinter import *
#
# def clicked():
#     if entry_login.get() and entry_pass.get():
#         lbl_welcome.configure(text="Welcome!!!")
#     else:
#         lbl_welcome.configure(text="Please enter the login\nand the password.")
#
# root = Tk()
# root.title("Welcome to the second entry app")
# label_login = Label(root, text="Login")
# label_login.pack()
# entry_login = Entry(root, width=10)
# entry_login.pack()
# label_pass = Label(root, text="Password")
# label_pass.pack()
# entry_pass = Entry(root, width=10, show='*')
# entry_pass.pack()
# btn = Button(root, text="Enter", command=clicked)
# btn.pack()
# lbl_welcome = Label(root)
# lbl_welcome.pack()
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# root.title("Welcome to entry app")
#
# message = StringVar()
# message.set("Any")
# txt = Entry(root, width=10, textvariable=message)
# txt.pack()
# message_2 = StringVar()
# message_2.set("hi")
# txt = Entry(root, width=120, textvariable=message_2)
# txt.pack()
# message = StringVar()
# print(message)
# print(type(message))
# message.set("Any")
# print(message)
# print(message.get())
#
# root.mainloop()


# from tkinter import *
# from tkinter import messagebox
#
# def show_message():
#     messagebox.showinfo("GUI Python", message.get())
#
# root = Tk()
# root.title("GUI на Python")
# root.geometry("300x250")
#
# message = StringVar()
# message_entry = Entry(textvariable=message)
# message_entry.pack()
#
# message_button = Button(text="Click Me", command=show_message)
# message_button.pack()
#
# root.mainloop()


# from tkinter import *
# from tkinter import messagebox
#
# def display_full_name():
#     messagebox.showinfo("GUI Python", name.get() + " " + surname.get())
#
# root = Tk()
# root.title("GUI на Python")
#
# name_label = Label(text="Введите имя:")
# name_label.grid(row=0, column=0, sticky="w")
# surname_label = Label(text="Введите фамилию:")
# surname_label.grid(row=1, column=0, sticky="w")
#
# name = StringVar()
# name_entry = Entry(textvariable=name)
# name_entry.grid(row=0, column=1)
#
# surname = StringVar()
# surname_entry = Entry(textvariable=surname)
# surname_entry.grid(row=1,column=1)
#
# message_button = Button(text="Click Me", command=display_full_name)
# message_button.grid(row=2, column=1)
#
# root.mainloop()


# from tkinter import *
# from tkinter import messagebox
#
# def clear():
#     name_entry.delete(0, END)
#     surname_entry.delete(0, END)
#
# def display():
#     messagebox.showinfo("GUI Python", name_entry.get() + " " + surname_entry.get())
#
# root = Tk()
# root.title("GUI на Python")
#
# name_label = Label(text="Введите имя:")
# name_label.grid(row=0, column=0, sticky="w")
# surname_label = Label(text="Введите фамилию:")
# surname_label.grid(row=1, column=0, sticky="w")
#
# name_entry = Entry()
# name_entry.grid(row=0,column=1)
# name_entry.insert(0, "Tom")
#
# surname_entry = Entry()
# surname_entry.grid(row=1,column=1)
# surname_entry.insert(0, "Soyer")
#
# display_button = Button(text="Display", command=display)
# display_button.grid(row=2, column=0)
# clear_button = Button(text="Clear", command=clear)
# clear_button.grid(row=2, column=1)
#
# root.mainloop()


# from tkinter import *
#
# root = Tk()
#
# message = StringVar()
# message.set("Текстовое поле вводит и выводит текст только одной строкой")
# txt = Entry(root, width=1000, textvariable=message)
# txt.pack()
#
# root.mainloop()


# from tkinter import *
#
#
# def click_button():
#     print("click button")
#
#
# root = Tk()
# button_1 = Button(root, text='Ok', command=click_button)
# button_1.pack()
# button_2 = Button(root, text='all right', command=click_button)
# button_2.pack()
#
# root.mainloop()

# from tkinter import *
#
#
# def click_button_1():
#     # print("click button")
#     root.bell()
#     root.title("new title")
#     button_1.config(text="ok", bg="pink")
#     new_entry = Entry()
#     new_entry.pack()
#     create_window()
#     # button_1.destroy()
#
#
# def create_window():
#     root = Tk()
#     root.title("new window")
#     label = Label(root, text="ball, you are stupid")
#     label.pack()
#     button = Button(root, text="ok", command=root.destroy)
#     button.pack()
#     root.mainloop()
#
#
# def click_button_2():
#     # print("Give me your money!")
#     root.title("second title")
#     root.bell()
#     # root.destroy()
#     button_1.config(text="not ok", width=60)
#
#
# root = Tk()
# button_1 = Button(root, text='Ok', command=click_button_1)
# button_1.pack()
# button_2 = Button(root, text='all right', command=click_button_2)
# button_2.pack()
#
# root.mainloop()


# from tkinter import *
#
#
# def clear_text():
#     message.set("")
#
# def paste_text():
#     # print(555)
#     message.set("The button clicked!")
#
# root = Tk()
# message = StringVar()
# # message.set("The button clicked!")
# text = Entry(root, width=100, textvariable=message)
# text.pack()
# button_paste = Button(root, text='Paste', command=paste_text)
# button_paste.pack()
# button_clear = Button(root, text='Clear', command=clear_text)
# button_clear.pack()
#
# root.mainloop()


# from tkinter import*
#
# def paste_text():
#     print(text.get())
#
# root = Tk()
#
# text = Entry(root, width=50)
# text.pack()
# button_paste = Button(root, text='Copy', command=paste_text)
# button_paste.pack()
# root.mainloop()


# from tkinter import*
#
#
# def paste_text():
#     print(message.get())
#
#
# root = Tk()
#
# message = StringVar()
# message.set("The button clicked!")
#
# text = Entry(root, width=50, textvariable=message)
# text.pack()
# button_paste = Button(root, text='Copy', command=paste_text)
# button_paste.pack()
# root.mainloop()


# from tkinter import *
#
# def paste_text():
#     text.insert(0, "The button clicked!")
#
# def clear_text():
#     text.delete(0, END)
#
# root = Tk()
#
# text = Entry(root, width=50)
# text.pack()
# button_paste = Button(root, text='Paste', command=paste_text)
# button_paste.pack()
# button_clear = Button(root, text='Clear', command=clear_text)
# button_clear.pack()
# root.mainloop()


# from tkinter import *
#
#
# def print_text_raw():
#     print(text.get())
#     print(text_1.get())
#
#
# def print_text_format():
#     print(f'"Значеине первого поля: <{text.get()}>"')
#     print(f'"Значеине второго поля: <{text_1.get()}>"')
#
#
# root = Tk()
#
# text = Entry(root, width=50)
# text.pack()
# text_1 = Entry(root, width=50)
# text_1.pack()
# button_print = Button(root, text='Print raw', command=print_text_raw)
# button_print.pack()
# button_formated = Button(root, text='Print formated', command=print_text_format)
# button_formated.pack()
# root.mainloop()


# from tkinter import *
#
#
# def paste_text():
#     # print(text.get())
#     text_1.insert(0, text.get())
#
#
# root = Tk()
#
# text = Entry(root, width=50)
# text.pack()
# text_1 = Entry(root, width=50)
# text_1.pack()
# button_paste = Button(root, text='Copy', command=paste_text)
# button_paste.pack()
# root.mainloop()


# from tkinter import *
#
#
# def paste_text():
#     text_1.insert(0, f'''"<{text.get()}>", - it is the first entry's contents.''')
#
#
# root = Tk()
#
# text = Entry(root, width=50)
# text.pack()
# text_1 = Entry(root, width=50)
# text_1.pack()
# button_paste = Button(root, text='Copy', command=paste_text)
# button_paste.pack()
# root.mainloop()


from tkinter import *


class SingletonFrame(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Data(metaclass=SingletonFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__text = ''

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, value: str):
        self.__text = value


class MyEntry(Entry):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.insert(0, Data().text)
        root.bind('<Key>', self.update_entry)

    def update_entry(self, _):
        print(self.get())
        Data().text = self.get()
        self.delete(0, END)
        self.insert(0, Data().text)


counter = 0


def paste_text():
    global counter
    if counter % 2 == 0:
        MyEntry().pack()
    else:
        root.winfo_children()[1].destroy()
    counter += 1


root = Tk()

Button(root, text='Create', command=paste_text).pack()
root.mainloop()

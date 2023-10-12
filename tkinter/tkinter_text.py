# from tkinter import *
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.insert(END, "Bye Bye.....")
# text.pack()
#
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.insert(END, "Bye Bye.....")
# text.pack(fill=BOTH, expand=1)
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def add_text():
#     text.insert(END, "This is a new text!")
#
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.pack(fill=BOTH, expand=1)
# button_add = Button(text="add", command=add_text)
# button_add.pack()
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# buffer = ""
#
#
# def copy_all():
#     global buffer
#     buffer = text.get(1.0, END)
#
#
# def paste():
#     text.insert(END, buffer)
#
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.pack(fill=BOTH, expand=1)
# frame_buttons = Frame()
# frame_buttons.pack()
# button_copy_all = Button(frame_buttons, text="copy_all", command=copy_all)
# button_copy_all.pack(side=LEFT)
# button_paste = Button(frame_buttons, text="paste", command=paste)
# button_paste.pack(side=LEFT)
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# buffer = ""
#
#
# def copy_all():
#     global buffer
#     buffer = text.get(1.0, END)
#
#
# def copy():
#     global buffer
#     buffer = text.selection_get()
#
#
# def paste():
#     text.insert(END, buffer)
#
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.pack(fill=BOTH, expand=1)
# frame_buttons = Frame()
# frame_buttons.pack()
# button_copy_all = Button(frame_buttons, text="copy_all", command=copy_all)
# button_copy_all.pack(side=LEFT)
# button_copy = Button(frame_buttons, text="copy", command=copy)
# button_copy.pack(side=LEFT)
# button_paste = Button(frame_buttons, text="paste", command=paste)
# button_paste.pack(side=LEFT)
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# buffer = ""
#
#
# def cut():
#     global buffer
#     buffer = text.selection_get()
#     text.delete(SEL_FIRST, SEL_LAST)
#
#
# def copy():
#     global buffer
#     buffer = text.selection_get()
#
#
# def paste():
#     text.insert(END, buffer)
#
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.pack(fill=BOTH, expand=1)
# frame_buttons = Frame()
# frame_buttons.pack()
# button_copy = Button(frame_buttons, text="copy", command=copy)
# button_copy.pack(side=LEFT)
# button_cut = Button(frame_buttons, text="cut", command=cut)
# button_cut.pack(side=LEFT)
# button_paste = Button(frame_buttons, text="paste", command=paste)
# button_paste.pack(side=LEFT)
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def capitalize():
#     user_text = text.selection_get()
#     text.delete(SEL_FIRST, SEL_LAST)
#     text.insert(INSERT, user_text.capitalize())
#
#
# def lower():
#     user_text = text.selection_get()
#     text.delete(SEL_FIRST, SEL_LAST)
#     text.insert(INSERT, user_text.lower())
#
#
# def upper():
#     user_text = text.selection_get()
#     text.delete(SEL_FIRST, SEL_LAST)
#     text.insert(INSERT, user_text.upper())
#
#
# def title():
#     user_text = text.selection_get()
#     text.delete(SEL_FIRST, SEL_LAST)
#     text.insert(INSERT, user_text.title())
#
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.pack(fill=BOTH, expand=1)
# frame_buttons = Frame()
# frame_buttons.pack()
# button_capitalize = Button(frame_buttons, text="capitalize", command=capitalize)
# button_capitalize.pack(side=LEFT)
# button_lower = Button(frame_buttons, text="lower", command=lower)
# button_lower.pack(side=LEFT)
# button_upper = Button(frame_buttons, text="upper", command=upper)
# button_upper.pack(side=LEFT)
# button_title = Button(frame_buttons, text="title", command=title)
# button_title.pack(side=LEFT)
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def get_status():
#     user_text = text.get(1.0, END)
#     symbols = len(user_text)
#     lines = user_text.count("\n")
#     line = text.index(INSERT).split(".")[0]
#     symbol = text.index(INSERT).split(".")[1]
#     # print(text.index(INSERT))
#     label.config(text=f"symbols: {symbols} \t | lines: {lines} \t | line: {line} \t | symbol: {symbol} ".expandtabs(30))
#
#
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.pack(fill=BOTH, expand=1)
# frame_status = Frame()
# frame_status.pack(side=TOP, fill=X, expand=1)
# button_capitalize = Button(frame_status, text="Get status", command=get_status)
# button_capitalize.pack(side=LEFT)
# label = Label(frame_status, text=f"symbols: \t|lines: \t|line: \t|symbol: ".expandtabs(30))
# label.pack(side=LEFT)
#
#
# root.mainloop()


from tkinter import *
from tkinter.ttk import *


def get_status():
    user_text = text.get(1.0, END)
    symbols = len(user_text)
    lines = user_text.count("\n")
    line = text.index(INSERT).split(".")[0]
    symbol = text.index(INSERT).split(".")[1]
    # print(text.index(INSERT))
    label.config(text=f"symbols: {symbols} \t | lines: {lines} \t | line: {line} \t | symbol: {symbol} ".expandtabs(30))


def delete_left_symbol():
    index = text.index(INSERT)
    # print(f'{text.index(INSERT).split(".")[0]}.{int(text.index(INSERT).split(".")[1]) - 1}')
    index_1 = f'{text.index(INSERT).split(".")[0]}.{int(text.index(INSERT).split(".")[1]) - 1}'
    text.delete(index_1, index)
    # result_index = index
    # text.delete(result_index)


root = Tk()
text = Text(root)
text.insert(INSERT, "Hello.....")
text.pack(fill=BOTH, expand=1)
frame_status = Frame()
frame_status.pack(side=TOP, fill=X, expand=1)
button_capitalize = Button(frame_status, text="Get status", command=get_status)
button_capitalize.pack(side=LEFT)
button_capitalize = Button(frame_status, text="<- BackSpace", command=delete_left_symbol)
button_capitalize.pack(side=RIGHT)
label = Label(frame_status, text=f"symbols: \t|lines: \t|line: \t|symbol: ".expandtabs(30))
label.pack(side=LEFT)


root.mainloop()



# from tkinter import *
#
# root = Tk()
# main_menu = Menu(root)
# root.config(menu=main_menu)
# filemenu = Menu(main_menu, tearoff=0)
# main_menu.add_cascade(label='Файл', menu=filemenu)
# main_menu.add_cascade(label='Справка', menu=filemenu)
#
# root.mainloop()


# from tkinter import *
#
# root = Tk()
#
# mainmenu = Menu(root)
# root.config(menu=mainmenu)
#
# filemenu = Menu(mainmenu, tearoff=0)
# mainmenu.add_cascade(label="Файл", menu=filemenu)
# filemenu.add_command(label="Открыть...", command=lambda: print(2))
# filemenu.add_command(label="Новый")
# filemenu.add_command(label="Сохранить...")
# filemenu.add_command(label="Выход")
#
# helpmenu = Menu(mainmenu, tearoff=0)
# mainmenu.add_cascade(label="Справка", menu=helpmenu)
# helpmenu.add_command(label="Помощь")
# helpmenu.add_command(label="О программе")
#
# helpmenu2 = Menu(helpmenu, tearoff=0)
# helpmenu2.add_command(label="Локальная справка")
# helpmenu2.add_command(label="На сайте")
#
# helpmenu.add_cascade(label="Помощь", menu=helpmenu2)
#
# helpmenu.add_command(label="О программе")

# root.mainloop()


# from tkinter import *
# from tkinter import messagebox
#
#
# def edit_click():
#     messagebox.showinfo("GUI Python", "Нажата опция О программе")
#
#
# root = Tk()
# root.title("GUI на Python")
# root.geometry("300x250")
#
# main_menu = Menu()
#
# filemenu = Menu(main_menu, tearoff=0)
# main_menu.add_cascade(label="File", menu=filemenu)
# main_menu.add_cascade(label="Edit", menu=filemenu)
# main_menu.add_cascade(label="View", menu=filemenu)
#
# helpmenu = Menu(main_menu, tearoff=0)
# main_menu.add_cascade(label="Помощь", menu=helpmenu)
# helpmenu.add_command(label="О программе", command=edit_click)
#
# root.config(menu=main_menu)
#
# root.mainloop()


# from tkinter import *
#
#
# def showMenu(event):
#     print(event)
#     menu.post(event.x_root, event.y_root)
#
#
# def onQuit():
#     quit()
#
#
# root = Tk()
# root.geometry("250x150+300+300")
# root.title("Popup menu")
#
# menu = Menu(root, tearoff=0)
# menu.add_command(label="Exit", command=root.destroy)
# menu.add_command(label="Quit", command=onQuit)
#
# root.bind("<Button-1>", showMenu)
# root.mainloop()


# from tkinter import *
#
# x = 0
# y = 0
#
#
# def circle():
#     c.create_oval(x, y, x + 30, y + 30)
#
#
# def square():
#     c.create_rectangle(x, y, x + 30, y + 30)
#
#
# def triangle():
#     c.create_polygon(x, y, x - 15, y + 30, x + 15, y + 30,
#                      fill='white', outline='black')
#
#
# def popup(event):
#     global x, y
#     x = event.x
#     y = event.y
#     menu.post(event.x_root, event.y_root)
#
#
# root = Tk()
#
# c = Canvas(width=300, height=300, bg='white')
# c.pack()
#
# menu = Menu(tearoff=0)
# menu.add_command(label="Круг", command=circle)
# menu.add_command(label="Квадрат", command=square)
# menu.add_command(label="Треугольник", command=triangle)
#
# c.bind("<Button-1>", popup)
#
# root.mainloop()


# from tkinter import *
#
#
# def on_menu_select(option):
#     print('Selected:', option)
#
#
# menu_example = [
#     ['file', ['new', 'open', 'close']],
#     ['edit', ['undo', 'cut', 'paste', 'delete']],
#     ['format', ['word wrap', 'font']],
#     ['view', ['zoom', 'status bar']],
#     ['help', ['view help', 'about notepad']]
# ]
#
# root = Tk()
#
# menu_bar = Menu()
# root.config(menu=menu_bar)
#
# for menu_cascade, menu_command in menu_example:
#     menu = Menu(menu_bar, tearoff=False)
#     menu_bar.add_cascade(label=menu_cascade, menu=menu)
#
#     for sub_menu_item in menu_command:
#         menu.add_command(label=sub_menu_item, command=lambda option=sub_menu_item: on_menu_select(option))
#
# root.mainloop()


# from tkinter import *
# from tkinter import messagebox
# from tkinter import filedialog
#
# buffer = ""
#
#
# def create_new_file():
#     answer = messagebox.askyesnocancel(title='New File', message='Хотите сохранить файл?')
#     if answer:
#         save_file()
#
#
# def open_file():
#     file_name = filedialog.askopenfilename()
#     if not file_name:
#         return
#     with open(file_name, 'r') as file_text:
#         text.insert(1.0, file_text.read())
#
#
# def save_file():
#     file_name = filedialog.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
#                                                         ("HTML files", "*.html;*.htm"),
#                                                         ("All files", "*.*")))
#     if not file_name:
#         return
#     with open(file_name, 'w') as file:
#         file.write(text.get(1.0, END))
#
#
# def exit_program():
#     answer = messagebox.askyesnocancel(title='New File', message='Хотите сохранить файл?')
#     if answer:
#         save_file()
#         exit(0)
#     elif answer is None:
#         return
#     elif not answer:
#         exit(0)
#
#
# def undo():
#     try:
#         text.edit_undo()
#     except TclError:
#         pass
#
#
# def redo():
#     try:
#         text.edit_redo()
#     except TclError:
#         pass
#
#
# def cut():
#     global buffer
#     try:
#         buffer = text.selection_get()
#         text.delete(SEL_FIRST, SEL_LAST)
#     except TclError:
#         pass
#
#
# def paste():
#     text.insert(END, buffer) if buffer else None
#
#
# def delete():
#     try:
#         text.delete(SEL_FIRST, SEL_LAST)
#     except TclError:
#         pass
#
#
# def word_wrap():
#     text['wrap'] = WORD if text['wrap'] == 'none' else NONE
#
#
# def font():
#     pass
#
#
# def zoom():
#     pass
#
#
# def status_bar():
#     pass
#
#
# def view_help():
#     pass
#
#
# def about_notepad():
#     pass
#
#
# menu_example = [
#     ['file', {'new': [create_new_file, []],
#               'open': [open_file, ['<Command-o>']],
#               'save': [save_file, ['<Command-s>']],
#               'exit': [exit_program, ['<Command-q>']]}],
#     ['edit', {'undo': [undo, ['<Command-z>', '<Command-Cyrillic_ya>']],
#               'redo': [redo, ['<Command-Shift-Z>', '<Command-Shift-Cyrillic_YA>']],
#               'cut': [cut, ['<Command-c>', '<Command-Cyrillic_es>']],
#               'paste': [paste, ['<Command-v>', '<Command-Cyrillic_em>']],
#               'delete': [delete, ['Backspace']]}],
#     ['format', {'word wrap': [word_wrap, []], 'font': [font, []]}],
#     ['view', {'zoom': [zoom, []], 'status bar': [status_bar, []]}],
#     ['help', {'view help': [view_help, []], 'about notepad': [about_notepad, []]}]
# ]
#
# root = Tk()
#
# menu_bar = Menu()
# root.config(menu=menu_bar)
#
# for menu_cascade, menu_command in menu_example:
#     menu = Menu(menu_bar, tearoff=False)
#     menu_bar.add_cascade(label=menu_cascade, menu=menu)
#
#     for sub_menu_item, params in menu_command.items():
#         if sub_menu_item == 'word wrap':
#             menu.add_checkbutton(label=sub_menu_item, command=params[0])
#         else:
#             menu.add_command(label=sub_menu_item, command=params[0])
#         for command in params[1]:
#             root.bind(func=lambda _: params[0], sequence=command)
#
# text = Text(undo=True, wrap=NONE)
# text.pack(fill=BOTH, expand=1)
#
# root.mainloop()


# from tkinter import *
#
# x = 0
# y = 0
#
#
# def circle():
#     c.create_oval(x, y, x + 30, y + 30)
#
#
# def square():
#     c.create_rectangle(x, y, x + 30, y + 30)
#
#
# def triangle():
#     c.create_polygon(x, y, x - 15, y + 30, x + 15, y + 30, fill='white', outline='black')
#
#
# def popup(event):
#     global x, y
#     x = event.x
#     y = event.y
#     menu.post(event.x_root, event.y_root)
#
#
# root = Tk()
#
# c = Canvas(width=300, height=300, bg='white')
# c.pack()
#
# menu = Menu(tearoff=0)
# menu.add_command(label="Круг", command=circle)
# menu.add_command(label="Квадрат", command=square)
# menu.add_command(label="Треугольник", command=triangle)
#
# c.bind("<Button-1>", popup)
#
# root.mainloop()

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

clipboard = ""

x, y = 0, 0


def create_new_file():
    answer = messagebox.askyesnocancel(title='New File', message='Хотите сохранить файл?')
    if answer:
        save_file()


def open_file():
    file_name = filedialog.askopenfilename()
    if not file_name:
        return
    with open(file_name, 'r') as file_text:
        text.insert(1.0, file_text.read())


def save_file():
    file_name = filedialog.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                        ("HTML files", "*.html;*.htm"),
                                                        ("All files", "*.*")))
    if not file_name:
        return
    with open(file_name, 'w') as file:
        file.write(text.get(1.0, END))


def exit_program():
    answer = messagebox.askyesnocancel(title='New File', message='Хотите сохранить файл?')
    if answer:
        save_file()
        exit(0)
    elif answer is None:
        return
    elif not answer:
        exit(0)


def undo():
    try:
        text.edit_undo()
    except TclError:
        pass


def redo():
    try:
        text.edit_redo()
    except TclError:
        pass


def cut():
    global clipboard
    try:
        clipboard = text.selection_get()
        text.delete(SEL_FIRST, SEL_LAST)
    except TclError:
        pass


def copy():
    global clipboard
    try:
        clipboard = text.selection_get()
    except TclError:
        pass


def paste():
    text.insert(END, clipboard) if clipboard else None


def delete():
    try:
        text.delete(SEL_FIRST, SEL_LAST)
    except TclError:
        pass


def word_wrap():
    text['wrap'] = WORD if text['wrap'] == 'none' else NONE


def font():
    pass


def zoom():
    pass


def status_bar():
    pass


def view_help():
    pass


def about_notepad():
    pass


def popup(event):
    global x, y
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)


menu_example = [
    ['file', {'new': [create_new_file, []],
              'open': [open_file, ['<Command-o>']],
              'save': [save_file, ['<Command-s>']],
              'exit': [exit_program, ['<Command-q>']]}],
    ['edit', {'undo': [undo, ['<Command-z>', '<Command-Cyrillic_ya>']],
              'redo': [redo, ['<Command-Shift-Z>', '<Command-Shift-Cyrillic_YA>']],
              'cut': [cut, ['<Command-x>', '<Command-Cyrillic_che>']],
              'copy': [copy, ['<Command-c>', '<Command-Cyrillic_es>']],
              'paste': [paste, ['<Command-v>', '<Command-Cyrillic_em>']],
              'delete': [delete, ['Backspace']]}],
    ['format', {'word wrap': [word_wrap, []], 'font': [font, []]}],
    ['view', {'zoom': [zoom, []], 'status bar': [status_bar, []]}],
    ['help', {'view help': [view_help, []], 'about notepad': [about_notepad, []]}]
]

root = Tk()

menu_bar = Menu()
root.config(menu=menu_bar)

for menu_cascade, menu_command in menu_example:
    menu = Menu(menu_bar, tearoff=False)
    menu_bar.add_cascade(label=menu_cascade, menu=menu)

    for sub_menu_item, params in menu_command.items():
        if sub_menu_item == 'word wrap':
            menu.add_checkbutton(label=sub_menu_item, command=params[0])
        else:
            menu.add_command(label=sub_menu_item, command=params[0])
        for command in params[1]:
            root.bind(func=lambda _: params[0], sequence=command)

text = Text(undo=True, wrap=NONE)
text.pack(fill=BOTH, expand=1)

text.bind("<Button-2>", popup)

menu = Menu(tearoff=0)
menu.add_command(label="Cut", command=cut)
menu.add_command(label="Copy", command=copy)
menu.add_command(label="Paste", command=paste)

root.mainloop()

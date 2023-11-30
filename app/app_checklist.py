from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import json

added_tasks = []
FILE_PATH = ''


def save_file():
    global FILE_PATH
    data = {
        "form": {
            "title": list_title.get(),
            "list_description": list_description.get(1.0, END),
            "tasks": [(text.children['!checkbutton']['text'].split(':')[1].strip()) for text in added_tasks],
        }
    }
    if FILE_PATH:
        with open(FILE_PATH, 'w', encoding='UTF-8') as file:
            file.write(json.dumps(data))
    else:
        save_file_as()


def save_file_as():
    global FILE_PATH
    data = {
        "form": {
            "title": list_title.get(),
            "list_description": list_description.get(1.0, END),
            "tasks": [(text.children['!checkbutton']['text'].split(':')[1].strip()) for text in added_tasks],
        }
    }
    FILE_PATH = filedialog.asksaveasfilename(
        defaultextension='.json', filetypes=[("json files", '*.json')],
        title="Choose filename")
    if FILE_PATH:
        with open(FILE_PATH, 'w', encoding='UTF-8') as file:
            file.write(json.dumps(data))


def open_file():
    file_name = filedialog.askopenfilename(filetypes=[("json files", '*.json')])
    if file_name:
        with open(file_name, 'r', encoding='UTF-8') as file:
            file_data = json.load(file)
        add_data(file_data) if file_data else None


def add_data(data):
    list_title.delete(0, END)
    list_title.insert(0, data["form"]["title"]) if data["form"]["title"] else None
    list_description.delete(1.0, END)
    list_description.insert(1.0, data["form"]["list_description"]) if data["form"]["title"] else None

    if frame_tasks.children:
        [i.pack_forget() for i in frame_tasks.children.values()]
        added_tasks.clear()

    for text_task in data["form"]["tasks"]:
        add_task(text_task)


def add_task(text: str):
    if frame_tasks.children.get('!label'):
        frame_tasks.children['!label'].pack_forget()
    frame_checkbutton = Frame(frame_tasks)
    frame_checkbutton.pack(side=TOP, fill=X)

    Checkbutton(frame_checkbutton, text=f"Задание № {len(added_tasks) + 1}: {text}").pack(side=LEFT)
    Button(frame_checkbutton, text='-', command=lambda: delete_task(frame_checkbutton)).pack(side=RIGHT)
    added_tasks.append(frame_checkbutton)


def delete_task(task: Frame):
    number = int(task.children['!checkbutton']['text'].split(':')[0].split('№')[1].strip())
    task.destroy()
    added_tasks.remove(task)
    update_count_tasks(number)


def update_count_tasks(number: int):
    for task in added_tasks:
        current_number = int(task.children['!checkbutton']['text'].split(':')[0].split('№')[1].strip())
        text_task = task.children['!checkbutton']['text'].split(':')[1].strip()
        if current_number > number:
            task.children['!checkbutton'].config(text=f"Задание № {current_number - 1}: {text_task}")


root = Tk()

frame_buttons = Frame()
frame_buttons.pack(side=TOP)
Button(frame_buttons, text='Save', command=save_file).pack(side=LEFT)
Button(frame_buttons, text='Save AS', command=save_file_as).pack(side=LEFT)
Button(frame_buttons, text='Open', command=open_file).pack(side=LEFT)

frame_title = Labelframe(text="Title")
label_title = Label(frame_title, text="The list title:")
label_title.pack(side=LEFT)
list_title = Entry(frame_title)
list_title.pack(side=LEFT, fill=X, expand=1)
frame_title.pack(fill=X)

list_description = Text(height=2, width=50)
list_description.pack(fill=X)

text_note = StringVar()
frame_add = Labelframe(text="Add a note")
frame_add.pack(fill=X)
note_add = Entry(frame_add, textvariable=text_note)
note_add.pack(side=LEFT, fill=X, expand=1)
Button(frame_add, text="+", width=5, command=lambda: add_task(text_note.get())).pack(side=LEFT)

frame_tasks = Labelframe(text="Tasks")
Label(frame_tasks, text="Here will be added new tasks...").pack()
frame_tasks.pack(fill=BOTH, expand=1)

root.mainloop()

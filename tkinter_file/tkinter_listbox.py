# from tkinter import *
# from tkinter.ttk import *
#
# root = Tk()
#
# lbox = Listbox()
# lbox.pack(side=LEFT, expand=1, fill=BOTH)
# scroll = Scrollbar(command=lbox.yview)
# scroll.pack(side=LEFT, fill=Y)
# lbox.config(yscrollcommand=scroll.set)
#
# for i in range(20):
#     lbox.insert(END, f"{i} next line")
#
# root.mainloop()


# from tkinter import *
#
#
# def add_item():
#     lbox.insert(END, entry.get())
#     entry.delete(0, END)
#
#
# def del_list():
#     select = list(lbox.curselection())
#     select.reverse()
#     for i in select:
#         lbox.delete(i)
#
#
# def print_list():
#     print(lbox.get(0, END))
#
#
# root = Tk()
#
# lbox = Listbox(selectmode=EXTENDED)
# lbox.pack(side=LEFT)
# scroll = Scrollbar(command=lbox.yview)
# scroll.pack(side=LEFT, fill=Y)
# lbox.config(yscrollcommand=scroll.set)
#
# f = Frame()
# f.pack(side=LEFT, padx=10)
# entry = Entry(f, bg='white')
# entry.pack(anchor=N)
# Button(f, text="Add", fg='black', command=add_item).pack(fill=X)
# Button(f, text="Delete", fg='black', command=del_list).pack(fill=X)
# Button(f, text="Print", fg='black', command=print_list).pack(fill=X)
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
# from random import *
#
#
# def random_numbers():
#     list_box.insert(END, randrange(-100, 100))
#
#
# root = Tk()
#
# Button(text="Add", command=random_numbers).pack()
# list_box = Listbox(selectmode=EXTENDED)
# list_box.pack(side=LEFT)
# scroll = Scrollbar(command=list_box.yview)
# scroll.pack(side=LEFT, fill=Y)
# list_box.config(yscrollcommand=scroll.set)
#
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
# from random import *
#
#
# def random_numbers():
#     number = list_box.get(END)
#     if not number:
#         list_box.insert(END, randrange(-100000, 100000))
#     else:
#         list_box.insert(END, number + 5)
#
#
# root = Tk()
# Button(text="Add", command=random_numbers).pack()
# list_box = Listbox(selectmode=EXTENDED)
# list_box.pack(side=LEFT)
# scroll = Scrollbar(command=list_box.yview)
# scroll.pack(side=LEFT, fill=Y)
# list_box.config(yscrollcommand=scroll.set)
#
# root.mainloop()


# from tkinter import *
#
# elements = ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt']
#
#
# def add_elements():
#     for element in elements:
#         list_box.insert(0, element)
#
#
# def print_to_console():
#     if len(list_box.get(0, END)) > 1:
#         print(list_box.get(0, END))
#
#
# def print_text():
#     list_elements = list_box.get(0, END)
#     for line in list_elements:
#         if len(text.get(1.0, END)) > 1:
#             text.insert(END, ", ")
#         text.insert(END, line)
#
#
# root = Tk()
# frame_all_left = Frame()
# frame_all_left.pack(side=LEFT, fill=Y)
#
# frame_button = Frame(frame_all_left)
# frame_button.pack(side=TOP)
# Button(frame_button, text="Add elements", command=add_elements).pack(fill=X)
# Button(frame_button, text="Print to console", command=print_to_console).pack(fill=X)
# Button(frame_button, text="Print Text()", command=print_text).pack(fill=X)
#
# frame_left_list_box = Frame(frame_all_left)
# frame_left_list_box.pack(fill=Y, expand=1)
# list_box = Listbox(frame_left_list_box, selectmode=EXTENDED)
# list_box.pack(side=LEFT, fill=Y, expand=1)
# scroll_left = Scrollbar(frame_left_list_box, command=list_box.yview)
# scroll_left.pack(side=LEFT, fill=Y)
# list_box.config(yscrollcommand=scroll_left.set)
#
# frame_all_right = Frame()
# frame_all_right.pack(side=RIGHT, fill=BOTH)
# text = Text()
# text.pack(side=LEFT, fill=BOTH, expand=1)
# scroll_right = Scrollbar()
# scroll_right.pack(side=LEFT, fill=Y)
# text.config(yscrollcommand=scroll_right.set)
#
# root.mainloop()


# from tkinter import *
#
# elements = ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt']
#
#
# def add_elements():
#     for element in elements:
#         list_box.insert(0, element)
#
#
# def print_the_first_element():
#     list_elements = list_box.get(0)
#     if text.get(1.0, END) != '\n':
#         text.insert(END, f'\n{list_elements}')
#     else:
#         text.insert(END, list_elements)
#
#
# def print_the_last_element():
#     list_elements = list_box.get(END)
#     if text.get(1.0, END) != '\n':
#         text.insert(END, f'\n{list_elements}')
#     else:
#         text.insert(END, list_elements)
#
#
# def print_elements():
#     list_elements = list_box.get(0, END)
#     if text.get(1.0, END) == '\n':
#         text.insert(END, 'All: ')
#     for line in list_elements:
#         if len(text.get(1.0, END)) > 6:
#             text.insert(END, ", ")
#         text.insert(END, line)
#
#
# root = Tk()
# frame_all_left = Frame()
# frame_all_left.pack(side=LEFT, fill=Y)
#
# frame_button = Frame(frame_all_left)
# frame_button.pack(side=TOP)
# Button(frame_button, text="Add elements", command=add_elements).pack(fill=X)
# Button(frame_button, text="Print elements", command=print_elements).pack(fill=X)
# Button(frame_button, text="Print the first element", command=print_the_first_element).pack(fill=X)
# Button(frame_button, text="Print the last element", command=print_the_last_element).pack(fill=X)
#
# frame_left_list_box = Frame(frame_all_left)
# frame_left_list_box.pack(fill=Y, expand=1)
# list_box = Listbox(frame_left_list_box, selectmode=EXTENDED)
# list_box.pack(side=LEFT, fill=Y, expand=1)
# scroll_left = Scrollbar(frame_left_list_box, command=list_box.yview)
# scroll_left.pack(side=LEFT, fill=Y)
# list_box.config(yscrollcommand=scroll_left.set)
#
# frame_all_right = Frame()
# frame_all_right.pack(side=RIGHT, fill=BOTH)
# text = Text()
# text.pack(side=LEFT, fill=BOTH, expand=1)
# scroll_right = Scrollbar()
# scroll_right.pack(side=LEFT, fill=Y)
# text.config(yscrollcommand=scroll_right.set)
#
# root.mainloop()


# from tkinter import *
#
# elements = ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt']
#
#
# def add_elements():
#     for element in elements:
#         list_box.insert(0, element)
#
#
# def delete_elements():
#     list_box.delete(0, END)
#
#
# def delete_the_first_element():
#     list_box.delete(0)
#
#
# def delete_the_last_element():
#     list_box.delete(END)
#
#
# root = Tk()
# frame_all_left = Frame()
# frame_all_left.pack(side=LEFT, fill=Y)
#
# frame_button = Frame(frame_all_left)
# frame_button.pack(side=TOP)
# Button(frame_button, text="Add elements", command=add_elements).pack(fill=X)
# Button(frame_button, text="Delete elements", command=delete_elements).pack(fill=X)
# Button(frame_button, text="Delete the first element", command=delete_the_first_element).pack(fill=X)
# Button(frame_button, text="Delete the last element", command=delete_the_last_element).pack(fill=X)
#
# frame_left_list_box = Frame(frame_all_left)
# frame_left_list_box.pack(fill=Y, expand=1)
# list_box = Listbox(frame_left_list_box, selectmode=EXTENDED)
# list_box.pack(side=LEFT, fill=Y, expand=1)
# scroll_left = Scrollbar(frame_left_list_box, command=list_box.yview)
# scroll_left.pack(side=LEFT, fill=Y)
# list_box.config(yscrollcommand=scroll_left.set)
#
#
# root.mainloop()


# from tkinter import *
#
# elements = ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt']
#
#
# def add_elements():
#     for element in elements:
#         list_box.insert(0, element)
#
#
# def print_an_index_element():
#     select = list_box.curselection()
#     if text.get(1.0, END) == '\n' and select:
#         text.insert(END, f'The Index {select}')
#     elif select:
#         text.insert(END, f'\nThe Index {select}')
#
#
# def print_the_selected_element():
#     select = list(list_box.curselection())
#     if text.get(1.0, END) != '\n':
#         text.insert(END, '\n')
#     if select:
#         text.insert(END, 'Select:')
#     for index in select:
#         text.insert(END, f' {list_box.get(index)}')
#         if select[-1] != index:
#             text.insert(END, ',')
#
#
# root = Tk()
# frame_all_left = Frame()
# frame_all_left.pack(side=LEFT, fill=Y)
#
# frame_button = Frame(frame_all_left)
# frame_button.pack(side=TOP)
# Button(frame_button, text="Add elements", command=add_elements).pack(fill=X)
# Button(frame_button, text="Print an index element", command=print_an_index_element).pack(fill=X)
# Button(frame_button, text="Print the selected element", command=print_the_selected_element).pack(fill=X)
#
# frame_left_list_box = Frame(frame_all_left)
# frame_left_list_box.pack(fill=Y, expand=1)
# list_box = Listbox(frame_left_list_box, selectmode=EXTENDED)
# list_box.pack(side=LEFT, fill=Y, expand=1)
# scroll_left = Scrollbar(frame_left_list_box, command=list_box.yview)
# scroll_left.pack(side=LEFT, fill=Y)
# list_box.config(yscrollcommand=scroll_left.set)
#
# frame_all_right = Frame()
# frame_all_right.pack(side=RIGHT, fill=BOTH)
# text = Text()
# text.pack(side=LEFT, fill=BOTH, expand=1)
# scroll_right = Scrollbar()
# scroll_right.pack(side=LEFT, fill=Y)
# text.config(yscrollcommand=scroll_right.set)
#
# root.mainloop()


# from tkinter import *
#
# elements = ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt']
#
#
# def add_elements():
#     for element in elements:
#         list_box.insert(0, element)
#
#
# def print_an_index_element():
#     select = list_box.curselection()
#     if text.get(1.0, END) == '\n' and select:
#         text.insert(END, f'The Index {select}')
#     elif select:
#         text.insert(END, f'\nThe Index {select}')
#
#
# def print_the_selected_element():
#     select = list(list_box.curselection())
#     select_elements = []
#     if text.get(1.0, END) != '\n':
#         text.insert(END, '\n')
#     if select:
#         text.insert(END, 'Select: ')
#     for index in select:
#         select_elements.append(list_box.get(index))
#     text.insert(END, ', '.join(select_elements))
#
#
# root = Tk()
# frame_all_left = Frame()
# frame_all_left.pack(side=LEFT, fill=Y)
#
# frame_button = Frame(frame_all_left)
# frame_button.pack(side=TOP)
# Button(frame_button, text="Add elements", command=add_elements).pack(fill=X)
# Button(frame_button, text="Print an index element", command=print_an_index_element).pack(fill=X)
# Button(frame_button, text="Print the selected element", command=print_the_selected_element).pack(fill=X)
#
# frame_left_list_box = Frame(frame_all_left)
# frame_left_list_box.pack(fill=Y, expand=1)
# list_box = Listbox(frame_left_list_box, selectmode=EXTENDED)
# list_box.pack(side=LEFT, fill=Y, expand=1)
# scroll_left = Scrollbar(frame_left_list_box, command=list_box.yview)
# scroll_left.pack(side=LEFT, fill=Y)
# list_box.config(yscrollcommand=scroll_left.set)
#
# frame_all_right = Frame()
# frame_all_right.pack(side=RIGHT, fill=BOTH)
# text = Text()
# text.pack(side=LEFT, fill=BOTH, expand=1)
# scroll_right = Scrollbar()
# scroll_right.pack(side=LEFT, fill=Y)
# text.config(yscrollcommand=scroll_right.set)
#
# root.mainloop()


# from tkinter import *
#
#
# def add_elements():
#     if entry.get():
#         list_box.insert(END, entry.get())
#     if entry.get():
#         entry.delete(0, END)
#
#
# root = Tk()
# frame_top = LabelFrame()
# frame_top.pack(side=TOP, fill=X)
# entry = Entry(frame_top)
# entry.pack(fill=X, expand=1)
# Button(frame_top, text="Add elements", command=add_elements).pack(fill=X, expand=1)
# frame_bottom = Frame()
# frame_bottom.pack(fill=BOTH, expand=1)
# list_box = Listbox(frame_bottom, selectmode=EXTENDED)
# list_box.pack(side=LEFT, fill=BOTH, expand=1)
# scroll = Scrollbar(frame_bottom, command=list_box.yview)
# scroll.pack(side=LEFT)
# list_box.config(yscrollcommand=scroll.set)
#
# root.mainloop()


# from tkinter import *
#
# purchases = ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt']
#
#
# def move_left():
#     select = list(right_list_box.curselection())
#     select.reverse()
#     if select and right_list_box:
#         for index in select:
#             select_element = right_list_box.get(index)
#             left_list_box.insert(END, select_element)
#         for index in select:
#             right_list_box.delete(index)
#
#
# def move_right():
#     select = list(left_list_box.curselection())
#     select.reverse()
#     if select and left_list_box:
#         for index in select:
#             select_element = left_list_box.get(index)
#             right_list_box.insert(END, select_element)
#         for index in select:
#             left_list_box.delete(index)
#
#
# root = Tk()
# frame_left = Frame()
# frame_left.pack(side=LEFT, fill=BOTH, expand=1)
# left_list_box = Listbox(frame_left, selectmode=EXTENDED)
# left_list_box.pack(side=LEFT, fill=BOTH, expand=1)
# for purchase in purchases:
#     left_list_box.insert(END, purchase)
# scroll_left = Scrollbar(frame_left, command=left_list_box.yview)
# scroll_left.pack(side=LEFT)
# left_list_box.config(yscrollcommand=scroll_left.set)
#
# frame_center = Frame()
# frame_center.pack(side=LEFT)
# move_to_left = Button(frame_center, text='<<<', command=move_left)
# move_to_left.pack()
# move_to_right = Button(frame_center, text='>>>', command=move_right)
# move_to_right.pack()
#
# frame_right = Frame()
# frame_right.pack(side=RIGHT, fill=BOTH, expand=1)
# right_list_box = Listbox(frame_right, selectmode=EXTENDED)
# right_list_box.pack(side=LEFT, fill=BOTH, expand=1)
# scroll_right = Scrollbar(frame_right, command=right_list_box.yview)
# scroll_right.pack(side=LEFT)
# right_list_box.config(yscrollcommand=scroll_right.set)
#
# root.mainloop()


from tkinter import *

purchases = ['a hat', 'a dress', 'a tie', 'a shirt', 'a belt', 'a skirt']


def move_to_left():
    select = list(right_list_box.curselection())
    select.reverse()
    if select and right_list_box:
        for index in select:
            select_element = right_list_box.get(index)
            left_list_box.insert(END, select_element)
        for index in select:
            right_list_box.delete(index)


def move_to_right():
    select = list(left_list_box.curselection())
    select.reverse()
    if select and left_list_box:
        for index in select:
            select_element = left_list_box.get(index)
            right_list_box.insert(END, select_element)
        for index in select:
            left_list_box.delete(index)


def move_to_first():
    select = text.get(SEL_FIRST, SEL_LAST)
    if select and text:
        selected_elements = select.split(',')
        for element in selected_elements:
            left_list_box.insert(END, element.strip())
        text.delete(SEL_FIRST, SEL_LAST)


def move_to_second():
    select = text.get(SEL_FIRST, SEL_LAST)
    if select and text:
        selected_elements = select.split(',')
        for element in selected_elements:
            right_list_box.insert(END, element.strip())
        text.delete(SEL_FIRST, SEL_LAST)


def move_from_left_to_down():
    select = list(left_list_box.curselection())
    select.reverse()
    for index in select:
        select_element = left_list_box.get(index)
        result_text = f', {select_element}' if text.get(1.0, END) != '\n' else select_element
        text.insert(END, result_text) if select and left_list_box else None
        left_list_box.delete(index)


def move_from_right_to_down():
    select = list(right_list_box.curselection())
    select.reverse()
    for index in select:
        select_element = right_list_box.get(index)
        result_text = f', {select_element}' if text.get(1.0, END) != '\n' else select_element
        text.insert(END, result_text) if select and right_list_box else None
        right_list_box.delete(index)


root = Tk()
frame_top = LabelFrame(text='Frame header')
frame_top.pack(side=TOP, fill=BOTH, expand=1)

frame_left = LabelFrame(frame_top)
frame_left.pack(side=LEFT, fill=BOTH, expand=1)
left_list_box = Listbox(frame_left, selectmode=EXTENDED)
left_list_box.pack(side=LEFT, fill=BOTH, expand=1)
for purchase in purchases:
    left_list_box.insert(END, purchase)
scroll_left = Scrollbar(frame_left, command=left_list_box.yview)
scroll_left.pack(side=LEFT)
left_list_box.config(yscrollcommand=scroll_left.set)

frame_buttons = LabelFrame(frame_top, text='Frame buttons')
frame_buttons.pack(side=LEFT)
Button(frame_buttons, text='<<<', command=move_to_left).pack()
Button(frame_buttons, text='>>>', command=move_to_right).pack()

frame_right = LabelFrame(frame_top)
frame_right.pack(side=RIGHT, fill=BOTH, expand=1)
right_list_box = Listbox(frame_right, selectmode=EXTENDED)
right_list_box.pack(side=LEFT, fill=BOTH, expand=1)
scroll_right = Scrollbar(frame_right, command=right_list_box.yview)
scroll_right.pack(side=LEFT)
right_list_box.config(yscrollcommand=scroll_right.set)

frame_center = LabelFrame(text='Frame Center')
frame_center.pack(fill=BOTH)

frame_left_in_center = LabelFrame(frame_center, text='Frame Left')
frame_left_in_center.pack(side=LEFT)
Button(frame_left_in_center, text='Up to 1', command=move_to_first).pack(side=LEFT)
Button(frame_left_in_center, text='Down to 3', command=move_from_left_to_down).pack(side=LEFT)

frame_right_in_center = LabelFrame(frame_center, text='Frame Right')
frame_right_in_center.pack(side=RIGHT)
Button(frame_right_in_center, text='Up to 2', command=move_to_second).pack(side=LEFT)
Button(frame_right_in_center, text='Down to 3', command=move_from_right_to_down).pack(side=LEFT)

frame_bottom = LabelFrame(text='Frame Text')
frame_bottom.pack(side=BOTTOM, fill=BOTH, expand=1)

text = Text(frame_bottom)
text.insert(END, 'apple, tomato')
text.pack(fill=BOTH, expand=1)

root.mainloop()

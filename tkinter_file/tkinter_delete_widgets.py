# from tkinter import *
# from tkinter.ttk import *
#
#
# def hide_element(element) -> None:
#     element.pack_forget()
#
#
# def show_element(element) -> None:
#     element.pack()
#
#
# root = Tk()
#
# frame_hide = Frame()
# frame_hide.pack(side=TOP)
#
# label = Label(frame_hide, text="The button will be hidden...")
# label.pack()
# button_hide = Button(text="Hidden me", command=lambda: hide_element(element=label))
# button_hide.pack()
#
# frame_show = Frame()
# frame_show.pack(side=TOP)
# button_show = Button(text="Show me", command=lambda: show_element(element=label))
# button_show.pack()
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def add_button():
#     _ = Button(text="I am here.)", command=lambda: _.pack_forget())
#     _.pack()
#
#
# root = Tk()
# button = Button(root, text="Add button", command=add_button)
# button.pack()
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
# i = 1
#
#
# def add_button():
#     global i
#     _ = Button(text=f"I am {i}", command=lambda: _.pack_forget())
#     _.pack(side=LEFT)
#     i += 1
#
#
# root = Tk()
# button = Button(root, text="Add button", command=add_button)
# button.pack()
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
# i = 1
#
#
# def add_button():
#     global i
#     _ = Button(text=f"I am {i}", command=lambda: _.pack_forget())
#     _.pack(side=RIGHT)
#     i += 1
#
#
# root = Tk()
# button = Button(root, text="Add button", command=add_button)
# button.pack()
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
# i = 1
#
#
# def add_button():
#     global i
#     label = (Label(text=f'Column{i}'))
#     label.grid(row=0, column=i+1)
#     button_new = Button(text=f"I am {i}", command=lambda: (button_new.grid_forget(), label.grid_forget()))
#     button_new.grid(row=i, column=0, columnspan=i+1, stick=NSEW)
#     i += 1
#
#
# root = Tk()
# button = Button(root, text="Add button", command=add_button)
# button.grid(row=0, column=0)
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
# i = 1
#
#
# def add_widgets():
#     global i
#     lbl_frm = Labelframe(text="Frame {}".format(i))
#     lbl_frm.pack()
#     Label(master=lbl_frm, text=f"Label {i}").grid(row=0, column=0, stick=NSEW)
#     button = Button(lbl_frm, text=f"Delete frame {i}", command=lambda: lbl_frm.destroy())
#     button.grid(row=0, column=1)
#     i += 1
#
#
# root = Tk()
# Button(text="Add button", command=add_widgets).pack()
# root.mainloop()


from tkinter import *
from tkinter.ttk import *

history = []


def delete_widgets(frame: Frame):
    history.remove(frame)
    frame.destroy()
    for index, frame_dict in enumerate(history):
        frame_dict.children['!label'].config(text=index+1)


def add_widgets():
    frame = Frame()
    frame.pack()
    Label(master=frame, text=len(history) + 1).grid(row=0, column=0, stick=NSEW)
    Entry(master=frame).grid(row=0, column=1, stick=NSEW)
    history.append(frame)
    Button(frame, text="Delete", command=lambda: delete_widgets(frame)).grid(row=0, column=2)


root = Tk()
Button(text="Add button", command=add_widgets).pack()
root.mainloop()

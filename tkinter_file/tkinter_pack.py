# from tkinter import *
#
# root = Tk()
# btn1 = Button(root, text="Button 1", fg="red", bg="yellow")
# btn1.pack(side=LEFT)
# btn2 = Button(root, text="Button 2", fg="orange", bg="green")
# btn2.pack(side=LEFT)
# btn3 = Button(root, text="Button 3", fg="white", bg="blue")
# btn3.pack(side=LEFT)
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# btn1 = Button(root, text="Button 1", fg="red")
# btn1.pack()
# btn2 = Button(root, text="Button 2", fg="green")
# btn2.pack(side=TOP)
# btn3 = Button(root, text="Button 3", fg="black")
# btn3.pack(side=LEFT)
# btn4 = Button(root, text="Button 4", fg="purple")
# btn4.pack(side=RIGHT)
# btn5 = Button(root, text="Button 5", fg="blue")
# btn5.pack(side=BOTTOM)
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# btn1 = Button(root, text="Button 1", fg="red")
# btn1.pack()
# btn2 = Button(root, text="Button 2", fg="green")
# btn2.pack(side=TOP)
# btn3 = Button(root, text="Button 3", fg="black")
# btn3.pack(side=TOP)
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# btn1 = Button(root, text="Button 1", fg="red")
# btn1.pack(side=BOTTOM)
# btn2 = Button(root, text="Button 2", fg="green")
# btn2.pack(side=BOTTOM)
# btn3 = Button(root, text="Button 3", fg="black")
# btn3.pack(side=BOTTOM)
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# btn1 = Button(root, text="Button 1", fg="red")
# btn1.pack(side=LEFT)
# btn2 = Button(root, text="Button 2", fg="green")
# btn2.pack(side=LEFT)
# btn3 = Button(root, text="Button 3", fg="black")
# btn3.pack(side=LEFT)
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# btn1 = Button(root, text="Button 1", fg="red")
# btn1.pack(side=RIGHT)
# btn2 = Button(root, text="Button 2", fg="green")
# btn2.pack(side=RIGHT)
# btn3 = Button(root, text="Button 3", fg="black")
# btn3.pack(side=RIGHT)
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# btn1 = Button(root, text="One", bg="red", fg="white")
# btn1.pack()
# btn2 = Button(root, text="Two", bg="green", fg="black")
# btn2.pack(side=TOP, fill=X)
# btn3 = Button(root, text="Three", bg="blue", fg="yellow")
# btn3.pack(side=LEFT, fill=Y)
# btn4 = Button(root, text="Four", bg="purple", fg="lightblue")
# btn4.pack(side=RIGHT, fill=Y)
# btn5 = Button(root, text="Five", bg="blue", fg="pink")
# btn5.pack(side=BOTTOM, fill=X)
# root.mainloop()


# from tkinter import *
# root = Tk()
# l1 = Label(bg="lightgreen", width=30, height=10, text="This is a label")
# l1.pack(expand=1, fill=Y)
# root.mainloop()


# from tkinter import *
# root = Tk()
# l1 = Label(bg="lightgreen", width=30, height=10, text="This is a label")
# # l1.pack(expand=1, anchor=SE)
# l1.pack(anchor=SE)
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# btn1 = Button(root, text="Button 1", fg="red")
# btn1.pack(side=TOP, fill=X)
# btn2 = Button(root, text="Button 2", fg="green")
# btn2.pack(side=BOTTOM, fill=X)
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# btn1 = Button(root, text="Button 1", fg="red")
# btn1.pack(side=LEFT, fill=Y)
# btn2 = Button(root, text="Button 2", fg="green")
# btn2.pack(side=RIGHT, fill=Y)
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# btn1 = Button(root, text="Button 1", fg="red")
# btn1.pack(expand=1, fill=BOTH)
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# btn1 = Button(root, text="Button 1", fg="red")
# btn1.pack(side=TOP,anchor=NE)
# btn3 = Button(root, text="Button 3", fg="black")
# btn3.pack(side=TOP, anchor=NW)
# btn4 = Button(root, text="Button 4", fg="purple")
# btn4.pack(side=BOTTOM, anchor=SE)
# btn5 = Button(root, text="Button 5", fg="blue")
# btn5.pack(side=BOTTOM, anchor=SW)
# root.mainloop()


# from tkinter import *
# root = Tk()
# l1 = Label(bg="lightgreen", width=30, height=10, text="This is a label")
# l1.pack(anchor=CENTER, expand=1)
# root.mainloop()


from tkinter import *


def print_red():
    color_name.config(text="red", fg="red")
    color_code.delete(0, END)
    color_code.insert(0, "#ff0000")
    color_code.config(bg="red")


def print_orange():
    color_name.config(text="Orange", fg="orange")
    color_code.delete(0, END)
    color_code.insert(0, "#ff7d00")
    color_code.config(bg="orange")


def print_yellow():
    color_name.config(text="yellow", fg="yellow")
    color_code.delete(0, END)
    color_code.insert(0, "#ffff00")
    color_code.config(bg="yellow")


def print_green():
    color_name.config(text="green", fg="green")
    color_code.delete(0, END)
    color_code.insert(0, "#00ff00")
    color_code.config(bg="green")


def print_lightblue():
    color_name.config(text="lightblue", fg="lightblue")
    color_code.delete(0, END)
    color_code.insert(0, "#007dff")
    color_code.config(bg="lightblue")


def print_blue():
    color_name.config(text="blue", fg="blue")
    color_code.delete(0, END)
    color_code.insert(0, "#0000ff")
    color_code.config(bg="blue")


def print_purple():
    color_name.config(text="purple", fg="purple")
    color_code.delete(0, END)
    color_code.insert(0, "#7d00ff")
    color_code.config(bg="purple")


root = Tk()


root.title('Colors')
color_name = Label(text="Color name")
color_name.pack()
color_code = Entry(justify=CENTER)
color_code.insert(0, "Color code")
color_code.pack()
button_red = Button(root, text='1', bg="red", command=print_red)
button_red.pack(fill=X)
button_orange = Button(root, text='2', bg="orange", command=print_orange)
button_orange.pack(fill=X)
button_yellow = Button(root, text='3', bg="yellow", command=print_yellow)
button_yellow.pack(fill=X)
button_green = Button(root, text='4', bg="green", command=print_green)
button_green.pack(fill=X)
button_lightblue = Button(root, text='5', bg="lightblue", command=print_lightblue)
button_lightblue.pack(fill=X)
button_blue = Button(root, text='6', bg="blue", command=print_blue)
button_blue.pack(fill=X)
button_purple = Button(root, text='7', bg="purple", command=print_purple)
button_purple.pack(fill=X)
root.mainloop()

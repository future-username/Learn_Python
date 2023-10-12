# from tkinter import *
#
# root = Tk()
# root.title("Welcome to grid app!")
# root.geometry('350x200')
# label = Label(root, text="Hello!")
# label.grid(column=5, row=1)
# button = Button(root, text="Click Me!")
# button.grid(column=1, row=0)
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# root.title("Welcome to grid app!")
# label = Label(root, text="Hello!")
# label.grid(column=1, row=0)
# button_1 = Button(root, text="Left")
# button_1.grid(column=0, row=0)
# button_2 = Button(root, text="Right")
# button_2.grid(column=2, row=0)
# button_3 = Button(root, text="Bottom")
# button_3.grid(column=1, row=1)
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# root.title("Welcome to the second entry app")
#
# label_login = Label(root, text="Login")
# label_login.grid(column=0, row=0, sticky=E)
# field_login = Entry(root, width=10)
# field_login.grid(column=1, row=0)
#
# label_pass = Label(root, text="Password")
# label_pass.grid(column=0, row=1, sticky=E)
# field_pass = Entry(root, width=10)
# field_pass.grid(column=1, row=1)
#
# button = Button(root, text="Enter")
# button.grid(column=0, row=2, columnspan=2, sticky=NSEW)
#
# root.mainloop()


# from tkinter import *
# from tkinter import Entry
#
#
# def calculate_numbers():
#     # print(first_number.get())
#     # print(second_number.get())
#     # print(float(first_number.get()))
#     # print(float(second_number.get()))
#     # print(float(first_number.get())+float(second_number.get()))
#     # print(first_number.get() != "")
#     # print(second_number.get() != "")
#     if first_number.get() != '' and second_number.get() != "":
#         result_plus.delete(0,END)
#         result_plus.insert(0, float(first_number.get())+float(second_number.get()))
#
# root = Tk()
# root.title("Calculate example")
#
# first_number = Entry(root, width=10)
# first_number.grid(column=0, row=0)
#
# label_plus = Label(root, text="+")
# label_plus.grid(column=1, row=0)
#
# second_number = Entry(root, width=10)
# second_number.grid(column=3, row=0)
#
# button = Button(root, text="=", command=calculate_numbers)
# button.grid(column=4, row=0)
#
# result_plus: Entry = Entry(root, width=10)
# result_plus.grid(column=5, row=0)

# root.mainloop()


from tkinter import *


def calculate_plus():
    # print(first_number.get())
    # print(second_number.get())
    # print(float(first_number.get()))
    # print(float(second_number.get()))
    # print(float(first_number.get())+float(second_number.get()))
    # print(first_number.get() != "")
    # print(second_number.get() != "")
    if first_plus.get() != '' and second_plus.get() != "" and \
            first_plus.get().isnumeric() and second_plus.get().isnumeric():
        result_plus.delete(0, END)
        result_plus.insert(0, float(first_plus.get())+float(second_plus.get()))
        # print(word_1.isnumeric())


def calculate_minus():
    if first_minus.get() != '' and second_minus.get() != "" and first_minus.get().isnumeric() and \
            second_minus.get().isnumeric():
        result_minus.delete(0, END)
        result_minus.insert(0, float(first_minus.get())-float(second_minus.get()))


def calculate_multiplication():
    if first_multiplication.get() != '' and second_multiplication.get() != "" and \
            first_multiplication.get().isnumeric() and second_multiplication.get().isnumeric():
        result_multiplication.delete(0, END)
        result_multiplication.insert(0, float(first_multiplication.get())*float(second_multiplication.get()))


def calculate_division():
    # print(first_division.get() != '' and second_division.get() != "" and second_division.get() != 0)
    # print(first_division.get() != '' and second_division.get() != "")
    # print(second_division.get() != "0")
    # print(type(second_division.get()))
    if first_division.get() != '' and second_division.get() != "" and second_division.get() != "0" and \
            first_division.get().isnumeric() and second_division.get().isnumeric():
        result_division.delete(0, END)
        result_division.insert(0, float(first_division.get())/float(second_division.get()))


root = Tk()
root.title("Calculate example")

first_plus = Entry(root, width=10)
first_plus.grid(column=0, row=0)
label_plus = Label(root, text="+")
label_plus.grid(column=1, row=0)
second_plus = Entry(root, width=10)
second_plus.grid(column=3, row=0)
button_plus = Button(root, text="=", command=calculate_plus)
button_plus.grid(column=4, row=0)
result_plus: Entry = Entry(root, width=10)
result_plus.grid(column=5, row=0)

first_minus = Entry(root, width=10)
first_minus.grid(column=0, row=1)
label_minus = Label(root, text="-")
label_minus.grid(column=1, row=1)
second_minus = Entry(root, width=10)
second_minus.grid(column=3, row=1)
button_minus = Button(root, text="=", command=calculate_minus)
button_minus.grid(column=4, row=1)
result_minus: Entry = Entry(root, width=10)
result_minus.grid(column=5, row=1)

first_division = Entry(root, width=10)
first_division.grid(column=0, row=3)
label_division = Label(root, text="/")
label_division.grid(column=1, row=3)
second_division = Entry(root, width=10)
second_division.grid(column=3, row=3)
button_division = Button(root, text="=", command=calculate_division)
button_division.grid(column=4, row=3)
result_division: Entry = Entry(root, width=10)
result_division.grid(column=5, row=3)

first_multiplication = Entry(root, width=10)
first_multiplication.grid(column=0, row=2)
label_multiplication = Label(root, text="*")
label_multiplication.grid(column=1, row=2)
second_multiplication = Entry(root, width=10)
second_multiplication.grid(column=3, row=2)
button_multiplication = Button(root, text="=", command=calculate_multiplication)
button_multiplication.grid(column=4, row=2)
result_multiplication: Entry = Entry(root, width=10)
result_multiplication.grid(column=5, row=2)

root.mainloop()


from tkinter import *


def paste_a8():
    # print(text.get(1.0, END))
    # print(list(text.get(1.0, END)))
    # print(len(text.get(1.0, END)))
    # print(len(text.get(1.0, END)) > 1)
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", ")
    text.insert(END, "A8")


def paste_a7():
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", ")
    text.insert(END, "A7")


def paste_a6():
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", ")
    text.insert(END, "A6")


def paste_a5():
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", ")
    text.insert(END, "A5")


def paste_b8():
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", ")
    text.insert(END, "B8")


def paste_b7():
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", ")
    text.insert(END, "B7")


def paste_b6():
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", ")
    text.insert(END, "B6")


def paste_b5():
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", ")
    text.insert(END, "B5")


def paste_c8():
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", ")
    text.insert(END, "C8")


def paste_c7():
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", ")
    text.insert(END, "C7")


def paste_c6():
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", ")
    text.insert(END, "C6")


def paste_c5():
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", ")
    text.insert(END, "C5")


def paste_d8():
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", ")
    text.insert(END, "D8")


def paste_d7():
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", ")
    text.insert(END, "D7")


def paste_d6():
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", ")
    text.insert(END, "D6")


def paste_d5():
    if len(text.get(1.0, END)) > 1:
        text.insert(END, ", ")
    text.insert(END, "D5")


root = Tk()
root.title("Chess board")

button_0 = Button(root, bg="yellow")
button_0.grid(column=0, row=0, ipadx=8)
button_A0 = Button(root, bg="yellow", text="A")
button_A0.grid(column=1, row=0, ipadx=20)
button_B0 = Button(root, bg="yellow", text="B")
button_B0.grid(column=2, row=0, ipadx=20)
button_C0 = Button(root, bg="yellow", text="C")
button_C0.grid(column=3, row=0, ipadx=20)
button_D0 = Button(root, bg="yellow", text="D")
button_D0.grid(column=4, row=0, ipadx=20)

button_8 = Button(root, bg="yellow", text="8")
button_8.grid(column=0, row=1, ipadx=5, ipady=20)
button_A8 = Button(root, bg="yellow", command=paste_a8)
button_A8.grid(column=1, row=1, ipadx=24, ipady=20)
button_B8 = Button(root, bg="brown", command=paste_b8)
button_B8.grid(column=2, row=1, ipadx=24, ipady=20)
button_C8 = Button(root, bg="yellow",command=paste_c8)
button_C8.grid(column=3, row=1, ipadx=24, ipady=20)
button_D8 = Button(root, bg="brown", command=paste_d8)
button_D8.grid(column=4, row=1, ipadx=24, ipady=20)

button_7 = Button(root, bg="yellow", text="7")
button_7.grid(column=0, row=2, ipadx=5, ipady=20)
button_A7 = Button(root, bg="brown", command=paste_a7)
button_A7.grid(column=1, row=2, ipadx=24, ipady=20)
button_B7 = Button(root, bg="yellow", command=paste_b7)
button_B7.grid(column=2, row=2, ipadx=24, ipady=20)
button_C7 = Button(root, bg="brown", command=paste_c7)
button_C7.grid(column=3, row=2, ipadx=24, ipady=20)
button_D7 = Button(root, bg="yellow", command=paste_d7)
button_D7.grid(column=4, row=2, ipadx=24, ipady=20)

button_6 = Button(root, bg="yellow", text="6")
button_6.grid(column=0, row=3, ipadx=5, ipady=20)
button_A6 = Button(root, bg="yellow", command=paste_a6)
button_A6.grid(column=1, row=3, ipadx=24, ipady=20)
button_B6 = Button(root, bg="brown", command=paste_b6)
button_B6.grid(column=2, row=3, ipadx=24, ipady=20)
button_C6 = Button(root, bg="yellow", command=paste_c6)
button_C6.grid(column=3, row=3, ipadx=24, ipady=20)
button_D6 = Button(root, bg="brown", command=paste_d6)
button_D6.grid(column=4, row=3, ipadx=24, ipady=20)

button_5 = Button(root, bg="yellow", text="5")
button_5.grid(column=0, row=4, ipadx=5, ipady=20)
button_A5 = Button(root, bg="brown", command=paste_a5)
button_A5.grid(column=1, row=4, ipadx=24, ipady=20)
button_B5 = Button(root, bg="yellow", command=paste_b5)
button_B5.grid(column=2, row=4, ipadx=24, ipady=20)
button_C5 = Button(root, bg="brown", command=paste_c5)
button_C5.grid(column=3, row=4, ipadx=24, ipady=20)
button_D5 = Button(root, bg="yellow", command=paste_d5)
button_D5.grid(column=4, row=4, ipadx=24, ipady=20)

text = Text(root, heigh=10, width=20)
text.grid(column=5, row=0, rowspan=6, sticky=NS)

root.mainloop()


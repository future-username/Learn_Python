# from tkinter import *
#
# root = Tk()
# root.title("Calculator")
# label_first = LabelFrame(root, text="1 ряд")
# label_first.pack()
# label_entry = Entry(label_first, justify=RIGHT)
# label_entry.pack()
# label_entry.insert(END, 0)
#
# label_second = LabelFrame(root, text="2 ряд")
# label_second.pack()
# button1 = Button(label_second, text=1).pack(side=LEFT)
# button2 = Button(label_second, text=2).pack(side=LEFT)
# button3 = Button(label_second, text=3).pack(side=LEFT)
# button4 = Button(label_second, text=4).pack(side=LEFT)
# button5 = Button(label_second, text=5).pack(side=LEFT)
#
# label_third = LabelFrame(root, text="3 ряд")
# label_third.pack()
# button6 = Button(label_third, text=6).pack(side=LEFT)
# button7 = Button(label_third, text=7).pack(side=LEFT)
# button8 = Button(label_third, text=8).pack(side=LEFT)
# button9 = Button(label_third, text=9).pack(side=LEFT)
# button0 = Button(label_third, text=0).pack(side=LEFT)
#
# label_forth = LabelFrame(root, text="4 ряд")
# label_forth.pack()
# button_plus = Button(label_forth, text="+").pack(side=LEFT)
# button_minus = Button(label_forth, text="-").pack(side=LEFT)
# button_subtract = Button(label_forth, text="-").pack(side=LEFT)
# button_slash = Button(label_forth, text="/").pack(side=LEFT)
# button_equal = Button(label_forth, text="=").pack(side=LEFT)
#
#
# root.mainloop()


# from tkinter import *
# # from tkinter.ttk import *
#
#
# def paste_zero():
#     if label_entry.get() == "0":
#         label_entry.delete(0, END)
#
#     label_entry.insert(END, "0")
#
#
# def paste_one():
#     # print(label_entry.get() == "0")
#     if label_entry.get() == "0":
#         label_entry.delete(0, END)
#
#     label_entry.insert(END, "1")
#
#
# def paste_two():
#     if label_entry.get() == "0":
#         label_entry.delete(0, END)
#
#     label_entry.insert(END, "2")
#
#
# def paste_three():
#     if label_entry.get() == "0":
#         label_entry.delete(0, END)
#
#     label_entry.insert(END, "3")
#
#
# def paste_four():
#     if label_entry.get() == "0":
#         label_entry.delete(0, END)
#
#     label_entry.insert(END, "4")
#
#
# def paste_five():
#     if label_entry.get() == "0":
#         label_entry.delete(0, END)
#
#     label_entry.insert(END, "5")
#
#
# def paste_six():
#     if label_entry.get() == "0":
#         label_entry.delete(0, END)
#
#     label_entry.insert(END, "6")
#
#
# def paste_seven():
#     if label_entry.get() == "0":
#         label_entry.delete(0, END)
#
#     label_entry.insert(END, "7")
#
#
# def paste_eight():
#     if label_entry.get() == "0":
#         label_entry.delete(0, END)
#
#     label_entry.insert(END, "8")
#
#
# def paste_nine():
#     if label_entry.get() == "0":
#         label_entry.delete(0, END)
#
#     label_entry.insert(END, "9")
#
#
# def clean():
#     label_entry.delete(0, END)
#     label_entry.insert(END, "0")
#
#
# def ce():
#     label_entry.delete(0, END)
#     label_entry.insert(END, "0")
#
#
# def paste_dot():
#     # print("." in label_entry.get())
#     if "." not in label_entry.get():
#         label_entry.insert(END, ".")
#
#
# def paste_plus():
#     if "+" == label_entry.get()[-1] or "-" == label_entry.get()[-1] or "*" == label_entry.get()[-1]\
#             or "/" == label_entry.get()[-1]:
#         label_entry.delete(len(label_entry.get()) - 1, END)
#     label_entry.insert(END, "+")
#
#
# def paste_minus():
#     if "+" == label_entry.get()[-1] or "-" == label_entry.get()[-1] or "*" == label_entry.get()[-1] \
#             or "/" == label_entry.get()[-1]:
#         label_entry.delete(len(label_entry.get()) - 1, END)
#     label_entry.insert(END, "-")
#
#
# def paste_multiplication():
#     if "+" == label_entry.get()[-1] or "-" == label_entry.get()[-1] or "*" == label_entry.get()[-1] \
#             or "/" == label_entry.get()[-1]:
#         label_entry.delete(len(label_entry.get()) - 1, END)
#     label_entry.insert(END, "*")
#
#
# def paste_slash():
#     if "+" == label_entry.get()[-1] or "-" == label_entry.get()[-1] or "*" == label_entry.get()[-1] \
#             or "/" == label_entry.get()[-1]:
#         label_entry.delete(len(label_entry.get()) - 1, END)
#     label_entry.insert(END, "/")
#
#
# def paste_percent():
#     if "+" == label_entry.get()[-1] or "-" == label_entry.get()[-1] or "*" == label_entry.get()[-1] \
#             or "/" == label_entry.get()[-1]:
#         label_entry.delete(len(label_entry.get()) - 1, END)
#     label_entry.insert(END, "%")
#
#
# def paste_equal():
#     # label_entry.insert(END, "=")
#     if "+" == label_entry.get()[-1] or "-" == label_entry.get()[-1] or "*" == label_entry.get()[-1] \
#             or "/" == label_entry.get()[-1]:
#         label_entry.delete(len(label_entry.get()) - 1, END)
#     save = label_entry.get()
#     label_entry.delete(0, END)
#     try:
#         label_entry.insert(END, eval(save))
#     except ZeroDivisionError:
#         label_entry.insert(END, "0")
#     # print(len(label_entry.get()))
#     # label_entry.delete(len(label_entry.get()) - 1, END)
#
#
# def paste_delete():
#     label_entry.delete(len(label_entry.get()) - 1, END)
#     if not label_entry.get():
#         label_entry.insert(END, "0")
#
#
# root = Tk()
# root.title("Calculator")
# label_entry = Entry(justify=RIGHT)
# label_entry.grid(column=0, row=0, columnspan=5, sticky=NSEW)
# label_entry.insert(END, 0)
#
# button_mc = Button(text="MC").grid(column=0, row=1)
# button_mr = Button(text="MR").grid(column=1, row=1)
# button_ms = Button(text="MS").grid(column=2, row=1)
# button_m_plus = Button(text="M+").grid(column=3, row=1)
# button_m_minus = Button(text="M-").grid(column=4, row=1)
#
# button_delete = Button(text="<-", command=paste_delete).grid(column=0, row=2)
# button_ce = Button(text="CE", command=ce).grid(column=1, row=2)
# button_c = Button(text="C", command=clean).grid(column=2, row=2)
# button_plus_minus = Button(text=chr(177)).grid(column=3, row=2)
# button_root = Button(text=chr(8730)).grid(column=4, row=2)
#
# button7 = Button(text=7, command=paste_seven).grid(column=0, row=3)
# button8 = Button(text=8, command=paste_eight).grid(column=1, row=3)
# button9 = Button(text=9, command=paste_nine).grid(column=2, row=3)
# button_slash = Button(text="/", command=paste_slash).grid(column=3, row=3)
# button_percent = Button(text="%", command=paste_percent).grid(column=4, row=3)
#
# button4 = Button(text=4, command=paste_four).grid(column=0, row=4)
# button5 = Button(text=5, command=paste_five).grid(column=1, row=4)
# button6 = Button(text=6, command=paste_six).grid(column=2, row=4)
# button_multiplication = Button(text="*", command=paste_multiplication).grid(column=3, row=4)
# button_part_one = Button(text="1/x").grid(column=4, row=4)
#
# button_1 = Button(text=1, command=paste_one).grid(column=0, row=5)
# button_2 = Button(text=2, command=paste_two).grid(column=1, row=5)
# button_3 = Button(text=3, command=paste_three).grid(column=2, row=5)
# button_minus = Button(text="-", command=paste_minus).grid(column=3, row=5)
#
# button_0 = Button(text=0, command=paste_zero).grid(column=0, row=6, columnspan=2, sticky=NSEW)
# button_dot = Button(text=".", command=paste_dot).grid(column=2, row=6)
# button_plus = Button(text="+", command=paste_plus).grid(column=3, row=6)
#
# button_equal = Button(text="=", command=paste_equal).grid(column=4, row=5, rowspan=2, sticky=NSEW)
#
#
# root.mainloop()


from tkinter import *


def paste_zero():
    if label_entry.get() == "0":
        label_entry.delete(0, END)

    label_entry.insert(END, "0")


def paste_one():
    if label_entry.get() == "0":
        label_entry.delete(0, END)

    label_entry.insert(END, "1")


def paste_two():
    if label_entry.get() == "0":
        label_entry.delete(0, END)

    label_entry.insert(END, "2")


def paste_three():
    if label_entry.get() == "0":
        label_entry.delete(0, END)

    label_entry.insert(END, "3")


def paste_four():
    if label_entry.get() == "0":
        label_entry.delete(0, END)

    label_entry.insert(END, "4")


def paste_five():
    if label_entry.get() == "0":
        label_entry.delete(0, END)

    label_entry.insert(END, "5")


def paste_six():
    if label_entry.get() == "0":
        label_entry.delete(0, END)

    label_entry.insert(END, "6")


def paste_seven():
    if label_entry.get() == "0":
        label_entry.delete(0, END)

    label_entry.insert(END, "7")


def paste_eight():
    if label_entry.get() == "0":
        label_entry.delete(0, END)

    label_entry.insert(END, "8")


def paste_nine():
    if label_entry.get() == "0":
        label_entry.delete(0, END)

    label_entry.insert(END, "9")


def clean():
    label_entry.delete(0, END)
    label_entry.insert(END, "0")


def ce():
    label_entry.delete(0, END)
    label_entry.insert(END, "0")


def paste_dot():
    if "." not in label_entry.get():
        label_entry.insert(END, ".")


def paste_plus():
    if label_entry.get()[-1] in "+-*/":
        label_entry.delete(len(label_entry.get()) - 1, END)
    label_entry.insert(END, "+")


def paste_minus():
    if label_entry.get()[-1] in "+-*/":
        label_entry.delete(len(label_entry.get()) - 1, END)
    label_entry.insert(END, "-")


def paste_multiplication():
    if label_entry.get()[-1] in "+-*/":
        label_entry.delete(len(label_entry.get()) - 1, END)
    label_entry.insert(END, "*")


def paste_slash():
    if label_entry.get()[-1] in "+-*/":
        label_entry.delete(len(label_entry.get()) - 1, END)
    label_entry.insert(END, "/")


def paste_percent():
    if label_entry.get()[-1] in "+-*/":
        label_entry.delete(len(label_entry.get()) - 1, END)
    label_entry.insert(END, "%")


def paste_equal():
    if label_entry.get()[-1] in "+-*/":
        label_entry.delete(len(label_entry.get()) - 1, END)
    save = label_entry.get()
    label_entry.delete(0, END)
    try:
        label_entry.insert(END, eval(save))
    except ZeroDivisionError:
        label_entry.insert(END, "0")


def paste_delete():
    label_entry.delete(len(label_entry.get()) - 1, END)
    if not label_entry.get():
        label_entry.insert(END, "0")


root = Tk()
root.title("Calculator")
label_entry = Entry(justify=RIGHT)
label_entry.grid(column=0, row=0, columnspan=5, sticky=NSEW)
label_entry.insert(END, 0)

button_mc = Button(text="MC", fg='black').grid(column=0, row=1)
button_mr = Button(text="MR", fg='black').grid(column=1, row=1)
button_ms = Button(text="MS", fg='black').grid(column=2, row=1)
button_m_plus = Button(text="M+", fg='black').grid(column=3, row=1)
button_m_minus = Button(text="M-", fg='black').grid(column=4, row=1)

button_delete = Button(text="<-", fg='black', command=paste_delete).grid(column=0, row=2)
button_ce = Button(text="CE", fg='black', command=ce).grid(column=1, row=2)
button_c = Button(text="C", fg='black', command=clean).grid(column=2, row=2)
button_plus_minus = Button(text=chr(177), fg='black').grid(column=3, row=2)
button_root = Button(text=chr(8730), fg='black').grid(column=4, row=2)

button7 = Button(text=7, fg='black', command=paste_seven).grid(column=0, row=3)
button8 = Button(text=8, fg='black', command=paste_eight).grid(column=1, row=3)
button9 = Button(text=9, fg='black', command=paste_nine).grid(column=2, row=3)
button_slash = Button(text="/", fg='black', command=paste_slash).grid(column=3, row=3)
button_percent = Button(text="%", fg='black', command=paste_percent).grid(column=4, row=3)

button4 = Button(text=4, fg='black', command=paste_four).grid(column=0, row=4)
button5 = Button(text=5, fg='black', command=paste_five).grid(column=1, row=4)
button6 = Button(text=6, fg='black', command=paste_six).grid(column=2, row=4)
button_multiplication = Button(text="*", fg='black', command=paste_multiplication).grid(column=3, row=4)
button_part_one = Button(text="1/x", fg='black').grid(column=4, row=4)

button_1 = Button(text=1, fg='black', command=paste_one).grid(column=0, row=5)
button_2 = Button(text=2, fg='black', command=paste_two).grid(column=1, row=5)
button_3 = Button(text=3, fg='black', command=paste_three).grid(column=2, row=5)
button_minus = Button(text="-", fg='black', command=paste_minus).grid(column=3, row=5)

button_0 = Button(text=0, fg='black', command=paste_zero).grid(column=0, row=6, columnspan=2, sticky=NSEW)
button_dot = Button(text=".", fg='black', command=paste_dot).grid(column=2, row=6)
button_plus = Button(text="+", fg='black', command=paste_plus).grid(column=3, row=6)

button_equal = Button(text="=", fg='black', command=paste_equal).grid(column=4, row=5, rowspan=2, sticky=NSEW)


root.mainloop()



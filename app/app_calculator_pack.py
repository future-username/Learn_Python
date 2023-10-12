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
#
# button_texts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "+", "-", "*", "/", "="]
#
# root = Tk()
# root.title("Calculator")
# label_first = LabelFrame(root, text="1 ряд", fg="black")
# label_first.pack()
# label_entry = Entry(label_first, justify=RIGHT)
# label_entry.pack()
# label_entry.insert(END, 0)
#
# label_second = LabelFrame(root, text="2 ряд", fg="black")
# label_second.pack()
# for i in range(5):
#     Button(label_second, text=button_texts[i], fg="black").pack(side=LEFT)
#
# label_third = LabelFrame(root, text="3 ряд", fg="black")
# label_third.pack()
# for i in range(5):
#     Button(label_third, text=button_texts[i+5], fg="black").pack(side=LEFT)
#
# label_forth = LabelFrame(root, text="4 ряд", fg="black")
# label_forth.pack()
# for i in range(5):
#     Button(label_forth, text=button_texts[i+10], fg="black").pack(side=LEFT)
#
# root.mainloop()


# from tkinter import *
#
# button_texts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "+", "-", "*", "/", "="]
#
# root = Tk()
# root.title("Calculator")
# label_first = LabelFrame(root, text="1 ряд", fg="black")
# label_first.pack()
# label_entry = Entry(label_first, justify=RIGHT)
# label_entry.pack()
# label_entry.insert(END, 0)
#
# for n in range(3):
#     label_second = LabelFrame(root, text=f"{n+2} ряд", fg="black")
#     label_second.pack()
#     for i in range(5):
#         Button(label_second, text=button_texts[i+n*5], fg="black").pack(side=LEFT)
#
# root.mainloop()


from tkinter import *

button_texts = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0],
    ["+", "-", "*", "/", "="]
]

root = Tk()
root.title("Calculator")
label_first = LabelFrame(root, text="1 ряд", fg="black")
label_first.pack()
label_entry = Entry(label_first, justify=RIGHT)
label_entry.pack()
label_entry.insert(END, 0)

for index, texts in enumerate(button_texts):
    print(texts)
    label_second = LabelFrame(root, text=f"{index+2} ряд", fg="black")
    label_second.pack()
    for element in texts:
        Button(label_second, text=element, fg="black").pack(side=LEFT)

root.mainloop()


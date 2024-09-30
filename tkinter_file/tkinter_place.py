# from tkinter import *
#
# clicks = 0
#
# def click_button():
#     global clicks
#     clicks += 1
#     btn.config(text="Clicks {}".format(clicks))
#
# root = Tk()
# root.title("GUI на Python")
# root.geometry("300x250")
#
#
# btn = Button(text="Clicks 0", background="#555", foreground="#ccc",
#              padx="20", pady="8", font="16", command=click_button)
# btn.place(relx=.5, rely=.5, anchor="c", height=30, width=130, bordermode=OUTSIDE)
#
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# root.title("GUI на Python")
# # root.geometry("300x250")
#
# btn1 = Button(text="x=10, y=20", background="#555", foreground="#ccc", padx="14", pady="7", font="13")
# btn1.place(x=10, y=20)
#
# btn2 = Button(text="x=50, y=100", background="#555", foreground="#ccc", padx="14", pady="7", font="13")
# btn2.place(x=50, y=100)
#
# btn3 = Button(text="x=140, y=160", background="#555", foreground="#ccc", padx="14", pady="7", font="13")
# btn3.place(x=140, y=160)
#
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# root.title("GUI на Python")
# root.geometry("400x400")
#
# btn1 = Button(text="x=10, y=20")
# btn1.place(x=0, y=0)
#
# btn2 = Button(text="x=50, y=100")
# btn2.place(x=325, y=0)
#
# btn3 = Button(text="x=140, y=160")
# btn3.place(x=0, y=375)
#
# btn4 = Button(text="x=140, y=160")
# btn4.place(x=320, y=375)
#
# btn4 = Button(text="x=140, y=160")
# btn4.place(x=160, y=188)
#
# root.mainloop()


# from tkinter import *
#
#
# def translate_label():
#     label_name.config(text="Имя:")
#     label_surname.config(text="Фамилия:")
#     label_year.config(text="Год рождения:")
#
#
# root = Tk()
# root.title("GUI на Python")
# root.geometry("235x130")
#
# label_name = Label(root, text="Name:")
# label_name.place(x=10, y=10)
#
# entry_name = Entry(root)
# entry_name.place(x=100, y=10)
#
# label_surname = Label(root, text="Surname:")
# label_surname.place(x=10, y=40)
#
# entry_surname = Entry(root)
# entry_surname.place(x=100, y=40)
#
# label_year = Label(root, text="Year:")
# label_year.place(x=10, y=70)
#
# entry_year = Entry(root)
# entry_year.place(x=100, y=70)
#
# button_translate = Button(root, text="Russia",command=translate_label)
# button_translate.place(x=100, y=100)
#
#
# root.mainloop()

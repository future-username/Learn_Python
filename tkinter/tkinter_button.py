# from tkinter import *
#
# root = Tk()
# button_ok = Button(root, text="OK")
# button_ok.pack()
# button_notok = Button(root, text="NOT OK")
# button_notok.pack()
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# root.title("GUI на Python")
# root.geometry("300x250")
# btn = Button(root, text="Click me!", fg="white", bg="pink", activeforeground="yellow")
# btn.pack()
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# button_ok = Button(root, text="OK")
# button_ok.pack()
# button_sure = Button(root, text="Are you sure")
# button_sure.pack()
# button_not = Button(root, text="May be NOT")
# button_not.pack()
# root.mainloop()


from tkinter import *

root = Tk()
button_ok = Button(root, text="OK", underline=1)
button_ok.pack()
button_sure = Button(root, text="Are you sure", underline=1)
button_sure.pack()
print(button_sure)
root.mainloop()
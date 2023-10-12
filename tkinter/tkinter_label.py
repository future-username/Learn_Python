# from tkinter import *
#
# root = Tk()
# label_1 = Label(root, text="This text wrote in the first label!")
# label_1.pack()
# label_2 = Label(root, text="This text wrote in the first label!")
# label_2.pack()
# root.mainloop()


from tkinter import *

root = Tk()
lbl_1 = Label(root, text="1-st label", font=("Arial Bold", 100), bg="darkgreen", anchor=CENTER, fg="red")
lbl_1.pack()
lbl_2 = Label(root, text="2-nd label")
lbl_2.pack()
lbl_3 = Label(root, text="It is the first string \n and the second string")
lbl_3.pack()
root.mainloop()

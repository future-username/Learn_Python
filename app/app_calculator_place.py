from tkinter import *

button_texts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "+", "-", "*", "/", "="]

root = Tk()
root.geometry("300x200")
root.title("Calculator")
label_entry = Entry(justify=RIGHT)
label_entry.place(x=10, y=10)
label_entry.insert(END, 0)

for i in range(15):
    Button(text=button_texts[i], fg="black").place(x=i%5*50+10, y=i//5*50+40)
    print(i, i%5*50+60, end=" ")

root.mainloop()


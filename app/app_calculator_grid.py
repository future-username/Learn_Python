from tkinter import *

button_texts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "+", "-", "*", "/", "="]

root = Tk()

root.title("Calculator")
label_entry = Entry(justify=RIGHT)
label_entry.grid(column=0, row=0, columnspan=5, sticky=EW)
label_entry.insert(END, 0)

for i in range(len(button_texts)):
    Button(text=button_texts[i], fg="black").grid(column=i % 5, row=i//5 + 1)
    print(i % 5, end=' ')
root.mainloop()

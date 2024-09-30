# from tkinter import *
#
# window = Tk()
# window.title("Message box title")
# window.geometry("300x75")
# lbl = Label(window, text="My message content!")
# btn = Button(window, text="Ok", width=10, command=window.destroy)
# lbl.pack()
# btn.pack(side=RIGHT)
# window.mainloop()


# from tkinter import messagebox
#
# messagebox.showinfo('Are you here?', 'hello')


# from tkinter import messagebox
#
# messagebox.showwarning('Message warning title', 'Message warning content5')
# messagebox.showwarning('Message warning title', 'Message warning content4')


# from tkinter import messagebox
#
# messagebox.showerror('Message error title', 'Message error content')


# from tkinter import messagebox
#
# res = messagebox.askquestion('Message title', 'Message ask content')
# print(res)
# res = messagebox.askyesno('Message title', 'Message y/n content')
# print(res)
# res = messagebox.askyesnocancel('Message title', 'Message y/n/cancel content')
# print(res)
# res = messagebox.askokcancel('Message title', 'Message ok/cancel content')
# print(res)
# res = messagebox.askretrycancel('Message title', 'Message retry/cancel content')
# print(res)


# from tkinter import *
# from tkinter import filedialog
#
# root = Tk()
# op = filedialog.askopenfilename()
# print(op)
# sa = filedialog.asksaveasfilename()
# print(sa)
# filedialog.ask
# root.mainloop()


from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog as fd


def insertText():
    file_name = fd.askopenfilename()
    if file_name:
        f = open(file_name)
        s = f.read()
        text.insert(1.0, s)
        f.close()
    else:
        text.insert(1.0, 'Select file')


def extractText():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                ("HTML files", "*.html;*.htm"),
                                                ("All files", "*.*")))
    if file_name:
        f = open(file_name, 'w')
        s = text.get(1.0, END).replace('\n\nSelect file', '')
        f.write(s)
        f.close()
    else:
        text.insert(END, '\n\nSelect file')


root = Tk()
text = Text(width=50, height=25)
text.grid(columnspan=2)
b1 = Button(text="Открыть", command=insertText)
b1.grid(row=1, sticky=E)
b2 = Button(text="Сохранить", command=extractText)
b2.grid(row=1, column=1, sticky=W)

root.mainloop()

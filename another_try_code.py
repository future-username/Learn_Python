from tkinter import *

counter = 0


class AddForm:
    previous_frame = None

    @classmethod
    def add_form(cls):
        global counter
        print(cls.previous_frame, len(root.winfo_children()))
        cls.previous_frame.destroy() if cls.previous_frame else None
        frame_label = LabelFrame(text=counter)
        frame_label.pack()
        Frame().pack()
        Label(frame_label, text=counter).pack()
        cls.previous_frame = frame_label
        counter += 1


root = Tk()

Button(text='form', command=AddForm.add_form).pack()
Button(text='form1', command=AddForm.add_form).pack()

root.mainloop()

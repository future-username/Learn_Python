# from tkinter import *
# from tkinter.ttk import *
#
#
# def change(event):
#     b['text'] = 'Thanks for your click. ;)'
#
#
# root = Tk()
#
# b = Button(text='Click me!')
# b.bind('<Button-1>', change)
# b.bind('<Return>', change)
# b.pack()
#
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
#
# def font1(event):
#     root['font'] = "Verdana"
#
#
# def font2(event):
#     root['font'] = "Times"
#
#
# root = Tk()
#
# l = Label(text="Hello World")
# l.bind('<Button-1>', font1)  # ЛКМ
# l.bind('<Button-3>', font2)  # ПКМ
# l.pack()
#
# root.mainloop()


# from tkinter import *
#
#
# def changeFont(font):
#     l['font'] = font
#
#
# root = Tk()
# l = Label(text="Hello World")
# l.pack()
# Button(text="Verdana", command=lambda f="Verdana": changeFont(f)).pack()
# Button(text="Times", command=lambda f="Times": changeFont(f)).pack()
#
# root.mainloop()


from tkinter import *


def show_key(event):
    root.title(str(event))


root = Tk()
root.bind('<Key>', show_key)
root.mainloop()


# from tkinter import *
#
#
# def b1(event: Event):
#     root.title("Левая кнопка мыши")
#
#
# def b3(event: Event):
#     root.title("Правая кнопка мыши")
#
#
# def move(event: Event):
#     x = event.x
#     y = event.y
#     s = "Движение мышью {}x{}".format(x, y)
#     root.title(s)
#
#
# root = Tk()
# root.minsize(width=500, height=400)
#
# root.bind('<Button-1>', b1)
# root.bind('<Button-3>', b3)
# root.bind('<Motion>', move)
#
# root.mainloop()


# from tkinter import *
#
#
# def exitWin(event):
#     root.destroy()
#
#
# def inLabel(event):
#     t = ent.get()
#     label.configure(text=t)
#
#
# def selectAll(event):
#     root.after(10, select_all, event.widget)
#
#
# def select_all(widget):
#     widget.selection_range(0, END)
#     widget.icursor(END)  # курсор в конец
#
#
# root = Tk()
#
# ent = Entry(width=40)
# ent.focus_set()
# ent.pack()
# label = Label(height=3, fg='orange', bg='darkgreen', font="Verdana 24")
# label.pack(fill=X)
#
# ent.bind('<Return>', inLabel)
# ent.bind('<Control-a>', selectAll)
# root.bind('<Control-q>', exitWin)
#
# root.mainloop()


# from tkinter import *
#
#
# def show_key(event: Event):
#     listbox.insert(END, str(event))
#
#
# root = Tk()
# listbox = Listbox()
# listbox.pack(fill=BOTH, expand=1)
# root.bind('<Key>', show_key)
# root.mainloop()


# import time
#
# for _ in range(5):
#     print(int(time.time()))         # общее количество секунд
#     print(time.strftime("%H:%M:%S"))    # время ввиде строки
#     time.sleep(1)


# from tkinter import *
# from time import strftime as time
#
# counter = 0
# labels = []
# times_from_label = []
# frames = []
#
#
# def tick(time_zone: int, clock: Label, current_time_zone=3):
#     time_hour = time('%H')
#     time_minute_second = time('%M:%S')
#
#     result_time = (24 + int(time_hour) + time_zone - current_time_zone) % 24
#
#     clock.config(text=f"{result_time}:{time_minute_second}")
#     clock.after(200, lambda: tick(time_zone, clock, current_time_zone))
#
#
# def interface(event: Event, frame_text: str, label_text: str):
#     frame_start_time = Frame()
#     frame_start_time.pack(side=TOP)
#     frame_count_time = LabelFrame(frame_start_time, text=frame_text)
#     frame_count_time.pack(side=LEFT)
#     label_count_time = Label(frame_count_time, text=label_text)
#     label_count_time.pack(fill=BOTH, expand=1)
#
#     frames.append(frame_start_time)
#     labels.append(label_count_time)
#     times_from_label.append(time("%H.%M.%S"))
#
#
# def count_time_difference() -> tuple:
#     start, finish = times_from_label[0], times_from_label[1]
#
#     start_hour, start_minute, start_second = start.split('.')
#     finish_hour, finish_minute, finish_second = finish.split('.')
#
#     # TODO this func
#     result_hour = int(finish_hour) - int(start_hour)
#     result_minute = int(finish_minute) - int(start_minute)
#     result_second = int(finish_second) - int(start_second)
#
#     return result_hour, result_minute, result_second
#
#
# def main(event: Event):
#     global counter, labels, frames
#     label_text = f"Hour: {time('%H')} Minute: {time('%M')} Second: {time('%S')}"
#     if counter == 0:
#         interface(event=event, frame_text='Start time', label_text=label_text)
#         counter += 1
#     elif counter == 1:
#         interface(event=event, frame_text='Finish time', label_text=label_text)
#         counter += 1
#     elif counter == 2:
#         result_hour, result_minute, result_second = count_time_difference()
#         label_text = f"Hour: {result_hour} Minute: {result_minute} Second: {result_second}"
#         interface(event=event, frame_text='Spend time', label_text=label_text)
#         counter += 1
#     elif counter == 3:
#         for time_label in labels:
#             time_label.config(text="Hour: 0 Minute: 0 Second: 0")
#         counter += 1
#     elif counter == 4:
#         for time_frame in frames:
#             time_frame.destroy()
#         labels, frames = [], []
#         counter = 0
#
#
# root = Tk()
# root.title('Time')
# frame_time = Frame()
# frame_time.pack(side=TOP)
# frame = LabelFrame(frame_time, text='Moscow time')
# frame.pack(side=LEFT)
# label = Label(frame, font=('times', 20, 'bold'), bg='green')
# label.pack(fill=BOTH, expand=1)
# tick(time_zone=3, clock=label)
# root.bind('<space>', main)
#
# root.mainloop()


# from tkinter import *
# from time import time

# start_second, counter = [0, 0, 0], [0, 0, 0]


# def timer(event: Event, label: Label, index: int):
#     if not start_second[index]:
#         start_second[index] = time()
#     time_second = int(time()) - int(start_second[index])
#     hour = time_second // 3600
#     minute = (time_second % 3600) // 60
#     second = time_second % 60
#     label.config(text=f'{hour}:{minute}:{second}')
#     if counter[index] <= 1:
#         label.after(200, lambda: timer(event, label, index))
#
#
# def process_timer(event: Event, label: Label, index):
#     if counter[index] == 0:
#         timer(event, label, index)
#         counter[index] += 1
#     elif counter[index] == 1:
#         counter[index] += 1
#     elif counter[index] == 2:
#         label.config(text='0:0:0')
#         counter[index] = 0
#         start_second[index] = 0
#
#
# root = Tk()
# root.title('Timer')
# frame_1 = LabelFrame(text='timer1')
# frame_1.pack(side=LEFT)
# label_1 = Label(frame_1, font=('times', 20, 'bold'))
# label_1.pack(fill=BOTH, expand=1)
#
# frame_2 = LabelFrame(text='timer1')
# frame_2.pack(side=LEFT)
# label_2 = Label(frame_2, font=('times', 20, 'bold'))
# label_2.pack(fill=BOTH, expand=1)
#
# frame_3 = LabelFrame(text='timer1')
# frame_3.pack(side=LEFT)
# label_3 = Label(frame_3, font=('times', 20, 'bold'))
# label_3.pack(fill=BOTH, expand=1)
#
# root.bind('1', lambda event: process_timer(event, label_1, 0))
# root.bind('2', lambda event: process_timer(event, label_2, 1))
# root.bind('3', lambda event: process_timer(event, label_3, 2))
#
# root.mainloop()

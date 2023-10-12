# # from tkinter import *
# # from time import time
# #
# # start_second, counter = [], []
# #
# #
# # def timer(event: Event, label: Label, index: int):
# #     if not start_second[index]:
# #         start_second[index] = time()
# #     time_second = int(time()) - int(start_second[index])
# #     hour = time_second // 3600
# #     minute = (time_second % 3600) // 60
# #     second = time_second % 60
# #     label.config(text=f'{hour}:{minute}:{second}')
# #     if counter[index] <= 1:
# #         label.after(200, lambda: timer(event, label, index))
# #
# #
# # def process_timer(event: Event, label: Label, index):
# #     if counter[index] == 0:
# #         timer(event, label, index)
# #         counter[index] += 1
# #     elif counter[index] == 1:
# #         counter[index] += 1
# #     elif counter[index] == 2:
# #         label.config(text='0:0:0')
# #         counter[index] = 0
# #         start_second[index] = 0
# #
# #
# # amount_label = int(input('Введите количество таймеров\t'))
# # root = Tk()
# # root.title('Timer')
# # label_list = []
# # for index in range(amount_label):
# #     start_second.append(0)
# #     counter.append(0)
# #     frame = LabelFrame(text=f'timer{index + 1}')
# #     frame.pack(side=LEFT)
# #     label = Label(frame, font=('times', 20, 'bold'))
# #     label.pack(fill=BOTH, expand=1)
# #     label_list.append(label)
# #     root.bind(str(index + 1), lambda event, widget=label_list[index], i=index: process_timer(event, widget, i))
# #
# # root.mainloop()


from tkinter import Tk, Label, LabelFrame, LEFT, BOTH
from tkinter import simpledialog
from time import time

start_second, counter = [], []


def tick_timer(label: Label, index: int):
    if not start_second[index]:
        start_second[index] = time()
    time_second = int(time()) - int(start_second[index])
    hour = time_second // 3600
    minute = (time_second % 3600) // 60
    second = time_second % 60
    label.config(text=f'{str(hour).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}')
    if counter[index] <= 1:
        label.after(200, lambda: tick_timer(label, index))


def process_timer(label: Label, index: int):
    if counter[index] == 0:
        tick_timer(label, index)
    elif counter[index] == 2:
        label.config(text='00:00:00')
        counter[index] = -1
        start_second[index] = 0
    counter[index] += 1


def process_all_timers():
    min_counter = min(counter)
    for index, label in enumerate(label_list):
        if min_counter == counter[index]:
            process_timer(label, index)


root = Tk()
root.title('Timer')
label_list = []
amount_label = simpledialog.askinteger("Input", "Введите количество таймеров:", parent=root, minvalue=1, maxvalue=9)

for index_timer in range(amount_label):
    start_second.append(0)
    counter.append(0)
    frame = LabelFrame(text=f'timer{index_timer + 1}')
    frame.pack(side=LEFT)
    label_timer = Label(frame, text='00:00:00', font=('times', 20, 'bold'))
    label_timer.pack(fill=BOTH, expand=1)
    label_list.append(label_timer)
    root.bind(str(index_timer + 1), lambda event, widget=label_timer, i=index_timer: process_timer(widget, i))

root.bind('<space>', lambda event: process_all_timers())

root.mainloop()

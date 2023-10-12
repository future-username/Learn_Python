# from tkinter import *
#
# root = Tk()
# frame_top = Frame(root)  # root можно не указывать
# frame_top.pack(fill=X)
# label_1 = Label(frame_top, width=7, height=4, bg='yellow', text="1")
# label_1.pack(side=LEFT, expand=1, fill=X)
# label_2 = Label(frame_top, width=7, height=4, bg='orange', text="2")
# label_2.pack(side=RIGHT, expand=1, fill=X)
#
# frame_bottom = Frame(root)
# frame_bottom.pack(expand=1, fill=BOTH)
# label_3 = Label(frame_bottom, width=7, height=4, bg='lightgreen', text="3")
# label_3.pack(side=LEFT)
# label_4 = Label(frame_bottom, width=7, height=4, bg='lightblue', text="4")
# label_4.pack(side=RIGHT)
#
# root.mainloop()


# from tkinter import *
#
# root = Tk()
#
# frame_top = LabelFrame(text="Верх")
# frame_top.pack(fill=BOTH, expand=1, side=LEFT)
# label_1 = Label(frame_top, width=7, height=4, bg='yellow', text="1")
# label_1.pack(side=LEFT)
# label_2 = Label(frame_top, width=7, height=4, bg='orange', text="2")
# label_2.pack(side=RIGHT)
#
# frame_bottom = LabelFrame(text="Низ")
# frame_bottom.pack(side=LEFT)
# label_3 = Label(frame_bottom, width=7, height=4, bg='lightgreen', text="3")
# label_3.pack(side=LEFT)
# label_4 = Label(frame_bottom, width=7, height=4, bg='lightblue', text="4")
# label_4.pack(side=LEFT)
#
# root.mainloop()


# from tkinter import *
#
# root = Tk()
#
# frame_button = LabelFrame(text="Header")
# frame_button.pack(fill=X)
# button_file = Button(frame_button, width=7, height=4, bg='lightgreen', text="Файл")
# button_file.pack(side=LEFT, fill=X, expand=1)
# button_view = Button(frame_button, width=7, height=4, bg='lightgreen', text="Вид")
# button_view.pack(side=LEFT, fill=X, expand=1)
# button_about = Button(frame_button, width=7, height=4, bg='lightgreen', text="О программе")
# button_about.pack(side=LEFT, fill=X, expand=1)
#
# frame_top = LabelFrame(text="Верх")
# frame_top.pack()
# label_1 = Label(frame_top, width=7, height=4, bg='yellow', text="1")
# label_1.pack(side=LEFT)
# label_2 = Label(frame_top, width=7, height=4, bg='orange', text="2")
# label_2.pack(side=LEFT)
#
# frame_main = LabelFrame(text="Средний")
# frame_main.pack()
# label_3 = Label(frame_main, width=7, height=4, bg='lightgreen', text="3")
# label_3.pack(side=LEFT)
# label_4 = Label(frame_main, width=7, height=4, bg='lightblue', text="4")
# label_4.pack(side=LEFT)
#
# frame_footer = LabelFrame(text="Низ")
# frame_footer.pack()
# label_5 = Label(frame_footer, width=7, height=4, bg='lightgreen', text="5")
# label_5.pack(side=LEFT)
# label_6 = Label(frame_footer, width=7, height=4, bg='lightblue', text="6")
# label_6.pack(side=LEFT)
#
# root.mainloop()


# from tkinter import *
#
#
# def change_view():
#     frame_top.pack(fill=NONE)
#
#
# def return_view():
#     frame_top.pack(fill=X)
#
#
# def change_view_footer():
#     button_left.pack(fill=X, expand=1)
#     button_right.pack(fill=X, expand=1)
#
#
# def return_view_footer():
#     button_left.pack(fill=NONE, expand=0)
#     button_right.pack(fill=NONE, expand=0)
#
#
# root = Tk()
#
# frame_top = LabelFrame()
# frame_top.pack(fill=X)
# button_file = Button(frame_top, width=7, height=4, bg='lightgreen', text="1", command=change_view)
# button_file.pack(side=LEFT)
# button_view = Button(frame_top, width=7, height=4, bg='lightgreen', text="2", command=return_view)
# button_view.pack(side=RIGHT)
#
# frame_button = LabelFrame()
# frame_button.pack(side=BOTTOM, fill=X)
# button_left = Button(frame_button, width=7, height=4, bg='lightgreen', text="3", command=change_view_footer)
# button_left.pack(side=LEFT)
# button_right = Button(frame_button, width=7, height=4, bg='lightgreen', text="4", command=return_view_footer)
# button_right.pack(side=RIGHT)
#
# root.mainloop()


# from tkinter import *
# import time
#
#
# def tick_moscow():
#     # get the current local time from the PC
#     time3 = time.strftime('%H:%M:%S')
#
#     # if time string has changed, update it
#     clock_moscow.config(text=time3)
#
#     # calls itself every 200 milliseconds to update the time
#     # display as needed could use >200 ms
#     clock_moscow.after(200, tick_moscow)
#
#
# def tick_london():
#     # get the current local time from the PC
#     time3 = time.strftime('%H:%M:%S')
#
#     # if time string has changed, update it
#     clock_london.config(text=time3)
#
#     # calls itself every 200 milliseconds to update the time
#     # display as needed could use >200 ms
#     clock_london.after(200, tick_london)
#
#
# def tick_tokyo():
#     # get the current local time from the PC
#     time3 = time.strftime('%H:%M:%S')
#
#     # if time string has changed, update it
#     clock_tokyo.config(text=time3)
#
#     # calls itself every 200 milliseconds to update the time
#     # display as needed could use >200 ms
#     clock_tokyo.after(200, tick_tokyo)
#
#
# root = Tk()
#
#
# frame_london = LabelFrame(text="London")
# frame_london.pack(side=LEFT)
# clock_london = Label(frame_london, font=('times', 20, 'bold'), bg='green')
# clock_london.pack(fill=BOTH, expand=1)
#
# frame_moscow = LabelFrame(text="Moscow")
# frame_moscow.pack(side=LEFT)
# clock_moscow = Label(frame_moscow, font=('times', 20, 'bold'), bg='green')
# clock_moscow.pack(fill=BOTH, expand=1)
#
# frame_tokyo = LabelFrame(text="Tokyo")
# frame_tokyo.pack(side=LEFT)
# clock_tokyo = Label(frame_tokyo, font=('times', 20, 'bold'), bg='green')
# clock_tokyo.pack(fill=BOTH, expand=1)
#
# tick_london()
# tick_moscow()
# tick_tokyo()
#
# root.mainloop()


# from tkinter import *
# import time
#
#
# def tick():
#     # get the current local time from the PC
#     time_hour = time.strftime('%H')
#     time_minute_second = time.strftime('%M:%S')
#
#     # if time string has changed, update it
#     clock_moscow.config(text=f"{int(time_hour)}:{time_minute_second}")
#
#     if int(time_hour) - 3 >= 0:
#         clock_london.config(text=f"{int(time_hour) - 3}:{time_minute_second}")
#     else:
#         clock_london.config(text=f"{22 - int(time_hour)}:{time_minute_second}")
#
#     if int(time_hour) + 6 <= 23:
#         clock_tokyo.config(text=f"{int(time_hour) + 6}:{time_minute_second}")
#     else:
#         clock_tokyo.config(text=f"{int(time_hour) + 6 - 24}:{time_minute_second}")
#
#     # calls itself every 200 milliseconds to update the time
#     # display as needed could use >200 ms
#     clock_moscow.after(200, tick)
#
#
# root = Tk()
#
#
# frame_london = LabelFrame(text="London")
# frame_london.pack(side=LEFT)
# clock_london = Label(frame_london, font=('times', 20, 'bold'), bg='green')
# clock_london.pack(fill=BOTH, expand=1)
#
# frame_moscow = LabelFrame(text="Moscow")
# frame_moscow.pack(side=LEFT)
# clock_moscow = Label(frame_moscow, font=('times', 20, 'bold'), bg='green')
# clock_moscow.pack(fill=BOTH, expand=1)
#
# frame_tokyo = LabelFrame(text="Tokyo")
# frame_tokyo.pack(side=LEFT)
# clock_tokyo = Label(frame_tokyo, font=('times', 20, 'bold'), bg='green')
# clock_tokyo.pack(fill=BOTH, expand=1)
#
# tick()
#
# root.mainloop()


# from tkinter import *
# import time
#
#
# def tick_moscow_time():
#     # get the current local time from the PC
#     time2 = time.strftime('%H:%M:%S')
#
#     # if time string has changed, update it
#     clock_moscow.config(text=f'Moscow time: {time2}')
#
#     # calls itself every 200 milliseconds to update the time
#     # display as needed could use >200 ms
#     clock_moscow.after(200, tick_moscow_time)
#
#
# def tick_current_time():
#     # get the current local time from the PC
#     time_hour = time.strftime('%H')
#     time_minute = time.strftime('%M')
#     time_second = time.strftime('%S')
#
#     # if time string has changed, update it
#     clock_moscow_current_time.config(text=f'Hour: {time_hour} Minute: {time_minute} Second: {time_second}')
#
#     # calls itself every 200 milliseconds to update the time
#     # display as needed could use >200 ms
#     clock_moscow_current_time.after(200, tick_current_time)
#
#
# def tick_left_time():
#     # get the current local time from the PC
#     time_hour = time.strftime('%H')
#     time_minute = time.strftime('%M')
#     time_second = time.strftime('%S')
#
#     # if time string has changed, update it
#     left_hour = 23 - int(time_hour)
#     left_time = f'Left hours: {left_hour} Left minutes: {59 - int(time_minute)} Left seconds: {60 - int(time_second)}'
#     clock_left.config(text=left_time)
#
#     # calls itself every 200 milliseconds to update the time
#     # display as needed could use >200 ms
#     clock_left.after(200, tick_left_time)
#
#
# root = Tk()
#
# frame_clock = LabelFrame(text="Moscow clock")
# frame_clock.pack(side=TOP, fill=X)
# clock_moscow = Label(frame_clock, text="Moscow time", font=('times', 20, 'bold'))
# clock_moscow.pack(fill=X)
#
# frame_current_time = LabelFrame(text="Current time")
# frame_current_time.pack(side=TOP, fill=X)
# clock_moscow_current_time = Label(frame_current_time, font=('times', 20, 'bold'))
# clock_moscow_current_time.pack(fill=X)
#
# frame_left = LabelFrame(text="Left time until the new day")
# frame_left.pack(side=TOP, fill=X)
# clock_left = Label(frame_left, font=('times', 20, 'bold'))
# clock_left.pack(fill=X)
#
# tick_moscow_time()
# tick_current_time()
# tick_left_time()
#
# root.mainloop()


from tkinter import *


def calculate_plus():
    # print(first_number.get())
    # print(second_number.get())
    # print(float(first_number.get()))
    # print(float(second_number.get()))
    # print(float(first_number.get())+float(second_number.get()))
    # print(first_number.get() != "")
    # print(second_number.get() != "")
    if first_plus.get() != '' and second_plus.get() != "" and \
            first_plus.get().isnumeric() and second_plus.get().isnumeric():
        result_plus.delete(0, END)
        result_plus.insert(0, float(first_plus.get()) + float(second_plus.get()))
        # print(word_1.isnumeric())


def calculate_minus():
    if first_minus.get() != '' and second_minus.get() != "" and first_minus.get().isnumeric() and \
            second_minus.get().isnumeric():
        result_minus.delete(0, END)
        result_minus.insert(0, float(first_minus.get()) - float(second_minus.get()))


def calculate_multiplication():
    if first_multiplication.get() != '' and second_multiplication.get() != "" and \
            first_multiplication.get().isnumeric() and second_multiplication.get().isnumeric():
        result_multiplication.delete(0, END)
        result_multiplication.insert(0, float(first_multiplication.get()) * float(second_multiplication.get()))


def calculate_division():
    # print(first_division.get() != '' and second_division.get() != "" and second_division.get() != 0)
    # print(first_division.get() != '' and second_division.get() != "")
    # print(second_division.get() != "0")
    # print(type(second_division.get()))
    if first_division.get() != '' and second_division.get() != "" and second_division.get() != "0" and \
            first_division.get().isnumeric() and second_division.get().isnumeric():
        result_division.delete(0, END)
        result_division.insert(0, float(first_division.get()) / float(second_division.get()))


def calculate_exponentiation():
    if first_exponentiation.get() != '' and second_exponentiation.get() != "" and \
            first_exponentiation.get().isnumeric() and second_exponentiation.get().isnumeric():
        result_exponentiation.delete(0, END)
        result_exponentiation.insert(0, float(first_exponentiation.get()) ** float(second_exponentiation.get()))


def calculate_integer_division():
    if first_integer_division.get() != '' and second_integer_division.get() != "" and \
            first_integer_division.get().isnumeric() and second_integer_division.get().isnumeric():
        result_integer_division.delete(0, END)
        result_integer_division.insert(0, float(first_integer_division.get()) // float(second_integer_division.get()))


def calculate_division_remained():
    if first_division_remained.get() != '' and second_division_remained.get() != "" and \
            first_division_remained.get().isnumeric() and second_division_remained.get().isnumeric():
        result_division_remained.delete(0, END)
        result_division_remained.insert(0, float(first_division_remained.get()) % float(second_division_remained.get()))


root = Tk()

frame_plus = LabelFrame(text="addition")
frame_plus.pack(side=TOP, fill=X, expand=1)
first_plus = Entry(frame_plus, width=10)
first_plus.pack(side=LEFT, fill=X, expand=1)
label_plus = Label(frame_plus, text="+")
label_plus.pack(side=LEFT)
second_plus = Entry(frame_plus, width=10)
second_plus.pack(side=LEFT, fill=X, expand=1)
button_plus = Button(frame_plus, text="=", command=calculate_plus)
button_plus.pack(side=LEFT)
result_plus: Entry = Entry(frame_plus, width=10)
result_plus.pack(side=LEFT, fill=X, expand=1)

frame_minus = LabelFrame(text="subtraction")
frame_minus.pack(side=TOP, fill=X, expand=1)
first_minus = Entry(frame_minus, width=10)
first_minus.pack(side=LEFT, fill=X, expand=1)
label_minus = Label(frame_minus, text="-")
label_minus.pack(side=LEFT)
second_minus = Entry(frame_minus, width=10)
second_minus.pack(side=LEFT, fill=X, expand=1)
button_minus = Button(frame_minus, text="=", command=calculate_minus)
button_minus.pack(side=LEFT)
result_minus: Entry = Entry(frame_minus, width=10)
result_minus.pack(side=LEFT, fill=X, expand=1)

frame_multiplication = LabelFrame(text="multiplication")
frame_multiplication.pack(side=TOP, fill=X, expand=1)
first_multiplication = Entry(frame_multiplication, width=10)
first_multiplication.pack(side=LEFT, fill=X, expand=1)
label_multiplication = Label(frame_multiplication, text="*")
label_multiplication.pack(side=LEFT)
second_multiplication = Entry(frame_multiplication, width=10)
second_multiplication.pack(side=LEFT, fill=X, expand=1)
button_multiplication = Button(frame_multiplication, text="=", command=calculate_multiplication)
button_multiplication.pack(side=LEFT)
result_multiplication: Entry = Entry(frame_multiplication, width=10)
result_multiplication.pack(side=LEFT, fill=X, expand=1)

frame_division = LabelFrame(text="division")
frame_division.pack(side=TOP, fill=X, expand=1)
first_division = Entry(frame_division, width=10)
first_division.pack(side=LEFT, fill=X, expand=1)
label_division = Label(frame_division, text="/")
label_division.pack(side=LEFT)
second_division = Entry(frame_division, width=10)
second_division.pack(side=LEFT, fill=X, expand=1)
button_division = Button(frame_division, text="=", command=calculate_division)
button_division.pack(side=LEFT, fill=X, expand=1)
result_division: Entry = Entry(frame_division, width=10)
result_division.pack(side=LEFT, fill=X, expand=1)

frame_exponentiation = LabelFrame(text="exponentiation")
frame_exponentiation.pack(side=TOP, fill=X, expand=1)
first_exponentiation = Entry(frame_exponentiation, width=10)
first_exponentiation.pack(side=LEFT, fill=X, expand=1)
label_exponentiation = Label(frame_exponentiation, text="**")
label_exponentiation.pack(side=LEFT)
second_exponentiation = Entry(frame_exponentiation, width=10)
second_exponentiation.pack(side=LEFT, fill=X, expand=1)
button_exponentiation = Button(frame_exponentiation, text="=", command=calculate_exponentiation)
button_exponentiation.pack(side=LEFT)
result_exponentiation: Entry = Entry(frame_exponentiation, width=10)
result_exponentiation.pack(side=LEFT, fill=X, expand=1)

frame_integer_division = LabelFrame(text="integer_division")
frame_integer_division.pack(side=TOP, fill=X, expand=1)
first_integer_division = Entry(frame_integer_division, width=10)
first_integer_division.pack(side=LEFT, fill=X, expand=1)
label_integer_division = Label(frame_integer_division, text="//")
label_integer_division.pack(side=LEFT)
second_integer_division = Entry(frame_integer_division, width=10)
second_integer_division.pack(side=LEFT, fill=X, expand=1)
button_integer_division = Button(frame_integer_division, text="=", command=calculate_integer_division)
button_integer_division.pack(side=LEFT, fill=X, expand=1)
result_integer_division = Entry(frame_integer_division, width=10)
result_integer_division.pack(side=LEFT, fill=X, expand=1)

frame_division_remained = LabelFrame(text="division_remained ")
frame_division_remained.pack(side=TOP, fill=X, expand=1)
first_division_remained = Entry(frame_division_remained, width=10)
first_division_remained.pack(side=LEFT, fill=X, expand=1)
label_division_remained = Label(frame_division_remained, text="%")
label_division_remained.pack(side=LEFT)
second_division_remained = Entry(frame_division_remained, width=10)
second_division_remained.pack(side=LEFT, fill=X, expand=1)
button_division_remained = Button(frame_division_remained, text="=", command=calculate_division_remained)
button_division_remained.pack(side=LEFT, fill=X, expand=1)
result_division_remained = Entry(frame_division_remained, width=10)
result_division_remained.pack(side=LEFT, fill=X, expand=1)


root.mainloop()



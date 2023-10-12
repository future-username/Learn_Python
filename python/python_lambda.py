# def to_do():
#     print('run')
#     return 56
#
#
# print(to_do())
# print(to_do)
# print(type(to_do))
# my_save = to_do
# print(my_save)
# my_save()

# def to_do(): print('run')
#
#
# b = to_do
# a = lambda: print('run')
# a(), b()
# print(a, b)


# def to_do(x): print(x)
#
#
# b = to_do
# a = lambda x: print(x)
# a(1), to_do(3), b(30)
# to_do(a), a(to_do)


# def to_do(fun): fun()
#
#
# def print_hi(): print('hi')
#
#
# print_hi()
# f = print_hi
# to_do(f)
# print_hello = lambda: print('hello')
# to_do(print_hello)


# from tkinter import *
#
# root = Tk()
# for x in range(5):
#     Button(text=x, command=lambda p=x: print(p)).pack()
#
# root.mainloop()


from tkinter import *


def click(): print(0)


def click_2(x): print(x)


root = Tk()
Button(text=0, command=click).pack()
Button(text=0, command=lambda: click()).pack()
Button(text=1, command=lambda: click_2(1)).pack()
Button(text=2, command=lambda: click_2(2)).pack()
Button(text=3, command=lambda: print(3)).pack()

root.mainloop()

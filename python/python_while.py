# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Неправильно ввели!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")


# total = 100
#
# i = 0
# while i < 5:
#     n = int(input())
#     total = total - n
#     i = i + 1
#     print(total)
#
# print("Осталось", total)


# total = 100
#
# while total > 0:
#     n = int(input())
#     total = total - n
#     print(total)
#
# print("Ресурс исчерпан")

# import random
# i = 0
# while i < 10:
#     number = random.randint(-5, 5)
#     i += 1
#     print(number, end=" ")


# i = 0
# while i < 15:
#     n = 2 ** i
#     i += 1
#     print(n, end=" ")


# import random
#
# numbers = []
#
# i = 0
# while i < 5:
#     number = random.randint(-2, 2)
#     # print(numbers.count(number) == 0)
#     if numbers.count(number) == 0:
#         numbers.append(number)
#         i += 1
# print(*numbers)


# import random
#
# numbers = []
#
# i = 0
# while i < 7:
#     number = random.randint(-10, 10)
#     # i += 1
#     # print(numbers.count(number) == 0)
#     if numbers.count(number) == 0 and number % 3 == 0:
#         numbers.append(number)
#         i += 1
# print(*numbers)


# total = 100
# n = 0
# while total > n:
#     n = int(input())
#     if n <= total:
#         total = total - n
#         print(total)
#     else:
#         print(total)
#
# print("Ресурс исчерпан")


# from tkinter import *
# from tkinter.ttk import *
#
# root = Tk()
# n = 0
# while n < 10:
#     n += 1
#     button = Button(root, text=f"Hi {n}")
#     button.grid(column=1, row=n)
#     entry = Entry(root)
#     entry.grid(column=0, row=n)
#     print(n, end="")
# root.mainloop()


# from tkinter import *
# from tkinter.ttk import *
#
# root = Tk()
# text_numbers = ["one", 'two', 'three', 'four', 'five']
#
# n = 0
# while n < 5:
#     n += 1
#     button = Button(root, text=text_numbers[n-1])
#     button.grid(column=1, row=n)
#     entry = Entry(root)
#     entry.grid(column=0, row=n)
#
#     print(n, end="")
#
# root.mainloop()


from tkinter import *
from tkinter.ttk import *
from pprint import pprint

double_list = [
    [1, 2, 3],
    [4, 5, 6],
    [0, 9, 0]
]
# pprint(double_list, width=15)
double_numbers = []
k = 0
while k < 8:
    numbers = []
    n = 0
    while n < 8:
        button = Button()
        button.pack()
        numbers.append(button)
        n += 1
    double_numbers.append(numbers)
    # print(numbers)
    k += 1
pprint(double_numbers, width=20)
# from tkinter import *
#
#
# def paste_a8():
#     # print(text.get(1.0, END))
#     # print(list(text.get(1.0, END)))
#     # print(len(text.get(1.0, END)))
#     # print(len(text.get(1.0, END)) > 1)
#     if len(text.get(1.0, END)) > 1:
#         text.insert(END, ", ")
#     text.insert(END, "A8")
#
#
# def paste_a7():
#     if len(text.get(1.0, END)) > 1:
#         text.insert(END, ", ")
#     text.insert(END, "A7")
#
#
# def paste_a6():
#     if len(text.get(1.0, END)) > 1:
#         text.insert(END, ", ")
#     text.insert(END, "A6")
#
#
# def paste_a5():
#     if len(text.get(1.0, END)) > 1:
#         text.insert(END, ", ")
#     text.insert(END, "A5")
#
#
# def paste_b8():
#     if len(text.get(1.0, END)) > 1:
#         text.insert(END, ", ")
#     text.insert(END, "B8")
#
#
# def paste_b7():
#     if len(text.get(1.0, END)) > 1:
#         text.insert(END, ", ")
#     text.insert(END, "B7")
#
#
# def paste_b6():
#     if len(text.get(1.0, END)) > 1:
#         text.insert(END, ", ")
#     text.insert(END, "B6")
#
#
# def paste_b5():
#     if len(text.get(1.0, END)) > 1:
#         text.insert(END, ", ")
#     text.insert(END, "B5")
#
#
# def paste_c8():
#     if len(text.get(1.0, END)) > 1:
#         text.insert(END, ", ")
#     text.insert(END, "C8")
#
#
# def paste_c7():
#     if len(text.get(1.0, END)) > 1:
#         text.insert(END, ", ")
#     text.insert(END, "C7")
#
#
# def paste_c6():
#     if len(text.get(1.0, END)) > 1:
#         text.insert(END, ", ")
#     text.insert(END, "C6")
#
#
# def paste_c5():
#     if len(text.get(1.0, END)) > 1:
#         text.insert(END, ", ")
#     text.insert(END, "C5")
#
#
# def paste_d8():
#     if len(text.get(1.0, END)) > 1:
#         text.insert(END, ", ")
#     text.insert(END, "D8")
#
#
# def paste_d7():
#     if len(text.get(1.0, END)) > 1:
#         text.insert(END, ", ")
#     text.insert(END, "D7")
#
#
# def paste_d6():
#     if len(text.get(1.0, END)) > 1:
#         text.insert(END, ", ")
#     text.insert(END, "D6")
#
#
# def paste_d5():
#     if len(text.get(1.0, END)) > 1:
#         text.insert(END, ", ")
#     text.insert(END, "D5")
#
#
# root = Tk()
# root.title("Chess board v1")
#
# button_0 = Button(root, bg="yellow")
# button_0.grid(column=0, row=0, ipadx=8)
# button_A0 = Button(root, bg="yellow", text="A")
# button_A0.grid(column=1, row=0, ipadx=20)
# button_B0 = Button(root, bg="yellow", text="B")
# button_B0.grid(column=2, row=0, ipadx=20)
# button_C0 = Button(root, bg="yellow", text="C")
# button_C0.grid(column=3, row=0, ipadx=20)
# button_D0 = Button(root, bg="yellow", text="D")
# button_D0.grid(column=4, row=0, ipadx=20)
#
# button_8 = Button(root, bg="yellow", text="8")
# button_8.grid(column=0, row=1, ipadx=5, ipady=20)
# button_A8 = Button(root, bg="yellow", command=paste_a8)
# button_A8.grid(column=1, row=1, ipadx=24, ipady=20)
# button_B8 = Button(root, bg="brown", command=paste_b8)
# button_B8.grid(column=2, row=1, ipadx=24, ipady=20)
# button_C8 = Button(root, bg="yellow",command=paste_c8)
# button_C8.grid(column=3, row=1, ipadx=24, ipady=20)
# button_D8 = Button(root, bg="brown", command=paste_d8)
# button_D8.grid(column=4, row=1, ipadx=24, ipady=20)
#
# button_7 = Button(root, bg="yellow", text="7")
# button_7.grid(column=0, row=2, ipadx=5, ipady=20)
# button_A7 = Button(root, bg="brown", command=paste_a7)
# button_A7.grid(column=1, row=2, ipadx=24, ipady=20)
# button_B7 = Button(root, bg="yellow", command=paste_b7)
# button_B7.grid(column=2, row=2, ipadx=24, ipady=20)
# button_C7 = Button(root, bg="brown",command=paste_c7)
# button_C7.grid(column=3, row=2, ipadx=24, ipady=20)
# button_D7 = Button(root, bg="yellow", command=paste_d7)
# button_D7.grid(column=4, row=2, ipadx=24, ipady=20)
#
# button_6 = Button(root, bg="yellow", text="6")
# button_6.grid(column=0, row=3, ipadx=5, ipady=20)
# button_A6 = Button(root, bg="yellow", command=paste_a6)
# button_A6.grid(column=1, row=3, ipadx=24, ipady=20)
# button_B6 = Button(root, bg="brown", command=paste_b6)
# button_B6.grid(column=2, row=3, ipadx=24, ipady=20)
# button_C6 = Button(root, bg="yellow", command=paste_c6)
# button_C6.grid(column=3, row=3, ipadx=24, ipady=20)
# button_D6 = Button(root, bg="brown", command=paste_d6)
# button_D6.grid(column=4, row=3, ipadx=24, ipady=20)
#
# button_5 = Button(root, bg="yellow", text="5")
# button_5.grid(column=0, row=4, ipadx=5, ipady=20)
# button_A5 = Button(root, bg="brown", command=paste_a5)
# button_A5.grid(column=1, row=4, ipadx=24, ipady=20)
# button_B5 = Button(root, bg="yellow", command=paste_b5)
# button_B5.grid(column=2, row=4, ipadx=24, ipady=20)
# button_C5 = Button(root, bg="brown", command=paste_c5)
# button_C5.grid(column=3, row=4, ipadx=24, ipady=20)
# button_D5 = Button(root, bg="yellow", command=paste_d5)
# button_D5.grid(column=4, row=4, ipadx=24, ipady=20)
#
# text = Text(root, heigh=10, width=20)
# text.grid(column=5, row=0, rowspan=6, sticky=NS)
#
# root.mainloop()


# from tkinter import *
#
#
# root = Tk()
# root.title("Chess board v2")
#
# # button_letters = ["", "A", "B", "C", "D", "E", "F", "G", "H", ""]
# # button_colors_first = ["yellow", "yellow", "brown", "yellow", "brown", "yellow", "brown", "yellow", "brown", "yellow"]
# # button_colors_second = ["yellow", "brown", "yellow", "brown", "yellow", "brown", "yellow", "brown", "yellow", "yellow"]
# # button_ipad_x = ["8", "20", "20", "20", "20", "20", "20", "20", "20", "8"]
#
# chess_buttons = [
#     ["yellow, ", "yellow, A", "yellow, B", "yellow, C", "yellow, D", "yellow, E", "yellow, F", "yellow, G", "yellow, H", "yellow, "],
#     ["yellow, 8", "yellow", "brown", "yellow", "brown", "yellow", "brown", "yellow", "brown", "yellow, 8"],
#     ["yellow, 7", "brown", "yellow", "brown", "yellow", "brown", "yellow", "brown", "yellow", "yellow, 7"],
#     ["yellow, 6", "yellow", "brown", "yellow", "brown", "yellow", "brown", "yellow", "brown", "yellow, 6"],
#     ["yellow, 5", "brown", "yellow", "brown", "yellow", "brown", "yellow", "brown", "yellow", "yellow, 5"],
#     ["yellow, 4", "yellow", "brown", "yellow", "brown", "yellow", "brown", "yellow", "brown", "yellow, 4"],
#     ["yellow, 3", "brown", "yellow", "brown", "yellow", "brown", "yellow", "brown", "yellow", "yellow, 3"],
#     ["yellow, 2", "yellow", "brown", "yellow", "brown", "yellow", "brown", "yellow", "brown", "yellow, 2"],
#     ["yellow, 1", "brown", "yellow", "brown", "yellow", "brown", "yellow", "brown", "yellow", "yellow, 1"],
#     ["yellow, ", "yellow, A", "yellow, B", "yellow, C", "yellow, D", "yellow, E", "yellow, F", "yellow, G", "yellow, H", "yellow, "],
# ]
#
# n = 0
#
# while n < 10:
#     n += 1
#     # print(chess_buttons[n-1])
#     temp_array = chess_buttons[n - 1]
#
#     k = 0
#     while k < 10:
#         k += 1
#         # print(temp_array[k - 1])
#         temp_number = temp_array[k - 1]
#         if len(temp_number.split()) == 2 or temp_number == "yellow, ":
#             # print(temp_number[0:6])
#             # print(temp_number[8])
#             Label(text=temp_number[8:], bg=temp_number[0:6]).grid(column=k-1, row=n-1, ipadx=7, sticky=NSEW)
#         elif temp_number == "yellow" or temp_number == "brown":
#             Button(bg=temp_number).grid(column=k-1, row=n-1, ipadx=24, ipady=20)
#         else:
#             Button(text=temp_number).grid(column=k-1, row=n-1, sticky=NSEW)
# text = Text(root, heigh=10, width=20)
# text.grid(column=10, row=0, rowspan=10, sticky=NS)
#
# root.mainloop()


# from tkinter import *
#
#
# chess_buttons = [
#     [11, 12, 13],
#     [4, 5, 6],
# ]
# root = Tk()
# root.title("Chess board v3")
# n = 0
# while n < 2:
#     n += 1
#     # print(chess_buttons[n - 1])
#     temp_array = chess_buttons[n - 1]
#     k = 0
#     while k < 3:
#         k += 1
#         print(temp_array[k-1])
#         temp_number = temp_array[k-1]
#         Button(text=temp_number).grid(column=k, row=n)
# root.mainloop()


# from tkinter import *
#
# chess_letters = " ABCDEFGH "
#
# root = Tk()
#
# n = 0
# while n < 10:
#     n += 1
#     # print(chess_letters[n-1])
#     k = 0
#     while k < 10:
#         k += 1
#         # print(chess_letters[k-1])
#         if n == 1 or n == 10:
#             Label(root, text=chess_letters[k-1], bg="yellow").grid(column=k, row=n, sticky=NSEW)
#         elif k == 1 or k == 10:
#             Label(text=10-n, bg="yellow").grid(column=k, row=n, ipadx=7, sticky=NSEW)
#         elif (k+1) % 2 and (n+1) % 2 or k % 2 and n % 2:
#             Button(bg="yellow").grid(column=k, row=n, ipadx=24, ipady=20, sticky=NSEW)
#         else:
#             Button(bg="brown").grid(column=k, row=n, ipadx=24, ipady=20, sticky=NSEW)
#
# root.mainloop()


# from tkinter import *
#
# chess_letters = " ABCDEFGH "
# chess_buttons = []
#
#
# # def show_allowed_steps():
# #     positioun = "A8"
# #     l = 0
# #     while l < 64:
# #         if l < 8 and l % 2 or not l % 8 and l % 16 == 8:
# #             print(chess_buttons[l])
# #             chess_buttons[l].config(bg="green")
# #         elif l < 8 and not l % 2 or not l % 8 and not l % 16:
# #             chess_buttons[l].config(bg="lightgreen")
# #         l += 1
#
#
# def show_allowed_steps():
#     positioun = "A4"
#     l = 0
#     while l < 64:
#         # if l >= 8 and l < 16 and not l % 2 or not l % 8 and l % 16 == 8:
#         #     print(chess_buttons[l])
#         # elif l > 8 and l < 16 and l % 2 or not l % 8 and not l % 16:
#         #     chess_buttons[l].config(bg="lightgreen")
#         # if l >= 56 and l < 64 and not l % 2 or not l % 8 and l % 16 == 8:
#         #     print(chess_buttons[l])
#         #     chess_buttons[l].config(bg="green")
#         # elif l > 56 and l < 64 and l % 2 or not l % 8 and not l % 16:
#         #     chess_buttons[l].config(bg="lightgreen")
#         # print(int(positioun[1]) == l)
# # x ? 5=3
# # x ? 6=2
# # 55 = 8 *(9 - 2) -1
# # 15 = 8 *  (9 - 2) -1
#         if (8 - int(positioun[1])) * 8 <= l <= 8 * (9 - int(positioun[1])) - 1:
#             print(l)
#             chess_buttons[l].config(bg="green")
#             # z = 0
#             # while z < 8:
#             #     z += 1
#             # chess_buttons[17].config(bg="green")
#             # chess_buttons[18].config(bg="green")
#             # chess_buttons[19].config(bg="green")
#             # chess_buttons[20].config(bg="green")
#             # chess_buttons[21].config(bg="green")
#             # chess_buttons[22].config(bg="green")
#             # chess_buttons[23].config(bg="green")
#         l += 1
#
#
# # 8: 0-7    8*(8-8) 8*(8-(int(positioun[1]))
# # 7: 8-15   8*(8-7)
# # 6: 16-23  8*(8-6)
# # 5: 24-31  8*(8-5)
# # 4: 32-39  8*(8-4)
# # 3: 40-47  8*(8-3)
# # 2: 48-55  8*(8-2)
# # 1: 56-63  8*(8-1)
#
#
# # 8 , 24 , 40, 56
# # 58, 60, 62, 64
# # 57, 58, 59, 60, 61, 62, 63, 64
#
#
# root = Tk()
#
# n = 0
# while n < 10:
#     n += 1
#     # print(chess_letters[n-1])
#     k = 0
#     while k < 10:
#         k += 1
#         # print(chess_letters[k-1])
#         if n == 1 or n == 10:
#             Label(root, text=chess_letters[k-1], bg="yellow").grid(column=k, row=n, sticky=NSEW)
#         elif k == 1 or k == 10:
#             Label(text=10-n, bg="yellow").grid(column=k, row=n, ipadx=7, sticky=NSEW)
#         elif not (k+n) % 2:
#             button = Button(bg="yellow", command=show_allowed_steps)
#             button.grid(column=k, row=n, ipadx=24, ipady=20, sticky=NSEW)
#             chess_buttons.append(button)
#         else:
#             button = Button(bg="brown")
#             button.grid(column=k, row=n, ipadx=24, ipady=20, sticky=NSEW)
#             chess_buttons.append(button)
# # print(chess_buttons)
# root.mainloop()


# from tkinter import *
#
# chess_letters = " ABCDEFGH "
# chess_buttons = []
#
#
# def show_allowed_steps():
#     positioun = "A4"
#     l = 0
#     while l < 64:
#         if (8 - int(positioun[1])) * 8 <= l <= 8 * (9 - int(positioun[1])) - 1:
#             chess_buttons[l].config(bg="green")
#         elif int(positioun[1])
#         l += 1
#
#
# root = Tk()
# root.title('v2')
#
# n = 0
# while n < 10:
#     n += 1
#     k = 0
#     while k < 10:
#         k += 1
#         if n == 1 or n == 10:
#             Label(root, text=chess_letters[k-1], bg="yellow").grid(column=k, row=n, sticky=NSEW)
#         elif k == 1 or k == 10:
#             Label(text=10-n, bg="yellow").grid(column=k, row=n, ipadx=7, sticky=NSEW)
#         elif not (k+n) % 2:
#             button = Button(bg="yellow", command=show_allowed_steps)
#             button.grid(column=k, row=n, ipadx=24, ipady=20, sticky=NSEW)
#             chess_buttons.append(button)
#         else:
#             button = Button(bg="brown")
#             button.grid(column=k, row=n, ipadx=24, ipady=20, sticky=NSEW)
#             chess_buttons.append(button)
#
# root.mainloop()


# from tkinter import *
# from pprint import pprint
#
# chess_letters = " ABCDEFGH "
# # chess_buttons = []
#
#
# def show_allowed_numbers():
#     positioun = "D2"
#     l = 0
#     while l < len(chess_buttons):
#         chess_buttons[l].config(text=l)
#         if 64 - int(positioun[1]) * 8 == l:
#             chess_buttons[l].config(bg="green")
#         l += 1
#
#
# def show_allowed_letters():
#     positioun = "A4"
#     l = 0
#     while l < len(chess_buttons):
#         chess_buttons[l].config(text=l)
#         # print(chess_letters.find(positioun[0]))
#         if chess_letters.find(positioun[0]) - 1 == l:
#             chess_buttons[l].config(bg="green")
#         l += 1
#
#
# def show_allowed_steps():
#     positioun = "D6"
#     l = 0
#     while l < len(chess_buttons):
#         chess_buttons[l].config(text=l)
#         # print(chess_letters.find(positioun[0]))
#         if chess_letters.find(positioun[0]) - 1 == l or 64 - int(positioun[1]) * 8 == l:
#             chess_buttons[l].config(bg="green")
#         l += 1
#
#
# def show_allowed_steps1():
#     positioun = "E5"
#     l = 0
#     while l < len(chess_buttons):
#         chess_buttons[l].config(text=l)
#         if chess_letters.find(positioun[0]) - 1 + 64 - int(positioun[1]) * 8 == l:
#             chess_buttons[l].config(bg="green")
#         l += 1
#
#
# def show_allowed_steps2():
#     positioun1 = "B7"
#     l = 0
#     while l < len(chess_buttons):
#         chess_buttons[l].config(text=l)
#         # if chess_letters.find(positioun1[0]) - 1 + 64 - int(positioun1[1]) * 8 == l\
#         #         or chess_letters.find(positioun2[0]) - 1 + 64 - int(positioun2[1]) * 8 == l:
#         if chess_letters.find(positioun1[0]) - 1 + 64 - int(positioun1[1]) * 8 < l:
#             chess_buttons[l].config(bg="green")
#         l += 1
#
#
# def paint_buttons_from_position():
#     position_1 = "B3"
#     index = 0
#     while index < len(chess_buttons):
#         chess_buttons[index].config(text=index)
#         # print(chess_letters.find(position_1[0]) - 1 + 64 - int(position_1[1]) * 8 < index)
#         # print(chess_letters.find(position_1[0]) - 1 + 64 - int(position_1[1]) * 8)
#         # print(chess_letters.find(position_1[0]) - 1 , 64 - int(position_1[1]) * 8)
#         if index <= chess_letters.find(position_1[0]) - 1 + 64 - int(position_1[1]) * 8:
#             chess_buttons[index].config(bg="green")
#         index += 1
#
#
# def paint_buttons_from_position_to_another_position():
#     position_1 = "B3"
#     position_2 = "H3"
#     index = 0
#     while index < len(chess_buttons):
#         chess_buttons[index].config(text=index)
#         if chess_letters.find(position_1[0]) - 1 + 64 - int(position_1[1]) * 8 <= index <= chess_letters.find(position_2[0]) - 1 + 64 - int(position_2[1]) * 8:
#             chess_buttons[index].config(bg="green")
#         index += 1
#
#
# def paint_line():
#     position_1 = "H4"
#     index = 0
#     while index < len(chess_buttons):
#         chess_buttons[index].config(text=index)
#         if 64 - int(position_1[1]) * 8 <= index <= 71 - int(position_1[1]) * 8:
#             chess_buttons[index].config(bg="green")
#         index += 1
#
#
# def paint_from_to_button():
#     positioun = "H8"
#     positioun_2 = "H1"
#     index = 0
#     while index < len(chess_buttons):
#         chess_buttons[index].config(text=index)
#         if chess_letters.find(positioun[0]) - 1 + 64 - int(positioun[1]) * 8 <= index <= chess_letters.find(positioun_2[0]) - 1 + 64 - int(positioun_2[1]) * 8 and index % 8 == chess_letters.find(positioun[0]) - 1:
#             chess_buttons[index].config(highlightbackground='green')
#         index += 1
#
#
# # def paint_vertical():
# #     position = "C1"
# #     index = 0
# #     while index < len(chess_buttons):
# #         chess_buttons[index].config(text=index)
# #         # positioun_from = chess_letters.find(positioun[0]) - 1 - int(positioun[1]) * 8   # -64 - -1
# #         # print(f"{positioun_from=}")
# #         # positioun_to = chess_letters.find(positioun[0]) + 127 - int(positioun[1]) * 8   # 64 - 127
# #         # print(f"{positioun_to=}")
# #         positioun_column = index % 9 == chess_letters.find(position[0]) - 1
# #         if positioun_column or 64 - int(position[1]) * 8 <= index <= 71 - int(position[1]) * 8:
# #             chess_buttons[index].config(highlightbackground='green')
# #         index += 1
#
#
# def paint_cross():
#     position = "C1"
#     index = 0
#     while index
#         index += 1
#
#
# # l
# # 56 = 1 * 8 = 64 - 8 = 64 - 1 * 8 = 64 - int(positioun[1]) * 8
# # 48 = 2 * 8 = 64 - 16
#
#
# root = Tk()
# root.title('v2')
#
# double_buttons = []
# n = 0
# while n < 10:
#     chess_buttons = []
#     n += 1
#     k = 0
#     while k < 10:
#         k += 1
#         if n == 1 or n == 10:
#             Label(root, text=chess_letters[k-1], bg="black").grid(column=k, row=n, sticky=NSEW)
#         elif k == 1 or k == 10:
#             Label(text=10-n, bg="black").grid(column=k, row=n, ipadx=7, sticky=NSEW)
#         elif not (k+n) % 2:
#             button = Button(highlightbackground='yellow', command=paint_cross)
#             button.grid(column=k, row=n, ipadx=24, ipady=20, sticky=NSEW)
#             chess_buttons.append(button)
#         else:
#             button = Button(highlightbackground='brown')
#             button.grid(column=k, row=n, ipadx=24, ipady=20, sticky=NSEW)
#             chess_buttons.append(button)
#     if chess_buttons:
#         double_buttons.append(chess_buttons)
#
# pprint(double_buttons)
# root.mainloop()
#

# from tkinter import *
# from pprint import pprint
#
# chess_letters = " ABCDEFGH "
#
#
# # def paint_all():
# #     position = "C1"
# #     x = 0
# #     while x < len(double_buttons):
# #         pprint(double_buttons[x])
# #         y = 0
# #         while y < len(double_buttons[x]):
# #             pprint(double_buttons[x][y])
# #             double_buttons[x][y].config(highlightbackground='green')
# #             y += 1
# #         x += 1
#
#
# def paint_horizont():
#     position = "C1"
#     x = 0
#     while x < len(double_buttons):
#         # pprint(double_buttons[x])
#         y = 0
#         while y < len(double_buttons[x]):
#             # pprint(double_buttons[x][y])
#             print(x == position[1])
#             print(x, position[1])
#             if x == 8 - int(position[1]):
#                 double_buttons[x][y].config(highlightbackground='green')
#             y += 1
#         x += 1
# # 8 = 0 8 - 8
# # 7 = 1 8 - 7
# # 6 = 2 8 - 6
# # 5 = 3 8 - 5
# # 4 = 4 8 - 4
# # 3 = 5 8 - 3
# # 2 = 6 8 - 2
# # 1 = 7 8 - 1
#
#
# def paint_vertical():
#     position = "H1"
#     x = 0
#     while x < len(double_buttons):
#         y = 0
#         while y < len(double_buttons[x]):
#             if y == chess_letters.find(position[0]) - 1:
#                 double_buttons[x][y].config(highlightbackground='green')
#             y += 1
#         x += 1
#
#
# def paint_cross():
#     position = "C4"
#     x = 0
#     while x < len(double_buttons):
#         y = 0
#         while y < len(double_buttons[x]):
#             if y == chess_letters.find(position[0]) - 1 and x == 8 - int(position[1]):
#                 double_buttons[x][y].config(highlightbackground='green')
#             y += 1
#         x += 1
#
#
# def paint_crossroads():
#     position = "C4"
#     x = 0
#     while x < len(double_buttons):
#         y = 0
#         while y < len(double_buttons[x]):
#             if y == chess_letters.find(position[0]) - 1 or x == 8 - int(position[1]):
#                 double_buttons[x][y].config(highlightbackground='green')
#             y += 1
#         x += 1
#
#
# def paint_main_diagonal():
#     position = "A2"
#     x = 0
#     while x < len(double_buttons):
#         y = 0
#         while y < len(double_buttons[x]):
#             if y + (8 - int(position[1])) == x + chess_letters.find(position[0]) - 1:
#                 double_buttons[x][y].config(highlightbackground='green')
#             y += 1
#         x += 1
#
#
# def paint_second_diagonal():
#     position = "A7"
#     y = 0
#     while y < len(double_buttons):
#         x = 0
#         while x < len(double_buttons[y]):
#             if y + int(position[1]) == 7 - x + chess_letters.find(position[0]):
#                 double_buttons[y][x].config(highlightbackground='green')
#             x += 1
#         y += 1
#
#
# def paint_cross_diagonals():
#     position = "D6"
#     y = 0
#     while y < len(double_buttons):
#         x = 0
#         while x < len(double_buttons[y]):
#             if x == chess_letters.find(position[0]) - 1 and y == 8 - int(position[1]):
#                 double_buttons[y][x].config(highlightbackground='black')
#             elif y + int(position[1]) == 7 - x + chess_letters.find(position[0]) or x + (8 - int(position[1])) == y + chess_letters.find(position[0]) - 1:
#                 double_buttons[y][x].config(highlightbackground='green')
#             x += 1
#         y += 1
#
#
# def paint_cross_diagonals_horizontals_verticals():
#     position = "H8"
#     y = 0
#     while y < len(double_buttons):
#         x = 0
#         while x < len(double_buttons[y]):
#             diagonal_first = x + (8 - int(position[1])) == y + chess_letters.find(position[0]) - 1
#             diagonal_second = y + int(position[1]) == 7 - x + chess_letters.find(position[0])
#             horizontal = y == 8 - int(position[1])
#             vertical = x == chess_letters.find(position[0]) - 1
#             if vertical and horizontal:
#                 double_buttons[y][x].config(highlightbackground='black')
#             elif diagonal_first or diagonal_second or horizontal or vertical:
#                 double_buttons[y][x].config(highlightbackground='green')
#             x += 1
#         y += 1
#
#
# def paint_king():
#     position = "C3"
#     y = 0
#     while y < len(double_buttons):
#         x = 0
#         while x < len(double_buttons[y]):
#             horizontal = y == 8 - int(position[1])\
#                          and chess_letters.find(position[0]) - 2 <= x <= chess_letters.find(position[0])
#             vertical = x == chess_letters.find(position[0]) - 1\
#                        and 8 - int(position[1]) - 1 <= y <= 8 - int(position[1]) + 1
#             diagonal_first = x + (8 - int(position[1])) == y + chess_letters.find(position[0]) - 1\
#                              and chess_letters.find(position[0]) - 2 <= x <= chess_letters.find(position[0])
#             diagonal_second = y + int(position[1]) == 7 - x + chess_letters.find(position[0])\
#                               and 8 - int(position[1]) - 1 <= y <= 8 - int(position[1]) + 1
#             if vertical and horizontal:
#                 double_buttons[y][x].config(highlightbackground='black')
#             elif diagonal_first or diagonal_second or horizontal or vertical:
#                 double_buttons[y][x].config(highlightbackground='green')
#             x += 1
#         y += 1
#
#
# def paint_horse():
#     position = "H4"
#     y = 0
#     while y < len(double_buttons):
#         x = 0
#         while x < len(double_buttons[y]):
#             center = chess_letters.find(position[0]) - 1 == x and 8 - int(position[1]) == y
#             c1 = chess_letters.find(position[0]) == x and 8 - int(position[1]) + 2 == y
#             c2 = chess_letters.find(position[0]) - 2 == x and 8 - int(position[1]) + 2 == y
#             c3 = chess_letters.find(position[0]) - 2 == x and 8 - int(position[1]) - 2 == y
#             c4 = chess_letters.find(position[0]) == x and 8 - int(position[1]) - 2 == y
#             c5 = chess_letters.find(position[0]) + 1 == x and 8 - int(position[1]) + 1 == y
#             c6 = chess_letters.find(position[0]) + 1 == x and 8 - int(position[1]) - 1 == y
#             c7 = chess_letters.find(position[0]) - 3 == x and 8 - int(position[1]) - 1 == y
#             c8 = chess_letters.find(position[0]) - 3 == x and 8 - int(position[1]) + 1 == y
#             if center:
#                 double_buttons[y][x].config(highlightbackground='black')
#             elif c1 or c2 or c3 or c4 or c5 or c6 or c7 or c8:
#                 double_buttons[y][x].config(highlightbackground='green')
#             x += 1
#         y += 1
#
#
# root = Tk()
# root.title('v3')
#
# double_buttons = []
# n = 0
# while n < 10:
#     chess_buttons = []
#     n += 1
#     k = 0
#     while k < 10:
#         k += 1
#         if n == 1 or n == 10:
#             Label(root, text=chess_letters[k-1], bg="black").grid(column=k, row=n, sticky=NSEW)
#         elif k == 1 or k == 10:
#             Label(text=10-n, bg="black").grid(column=k, row=n, ipadx=7, sticky=NSEW)
#         elif not (k+n) % 2:
#             button = Button(highlightbackground='yellow', command=paint_horse)
#             button.grid(column=k, row=n, ipadx=24, ipady=20, sticky=NSEW)
#             chess_buttons.append(button)
#         else:
#             button = Button(highlightbackground='brown')
#             button.grid(column=k, row=n, ipadx=24, ipady=20, sticky=NSEW)
#             chess_buttons.append(button)
#     if chess_buttons:
#         double_buttons.append(chess_buttons)
#
# # pprint(double_buttons)
# root.mainloop()
#
#
# # from tkinter import *
# #
# # chess_letters = " ABCDEFGH "
# # root = Tk()
# # root.title('v4')
# # size_desk = len(chess_letters)
# # for y in range(size_desk):
# #     for x in range(size_desk):
# #         if y == 0 or y == size_desk-1:
# #             Label(bg='black', text=chess_letters[x]).grid(column=x, row=y, ipadx=5, ipady=4, sticky=NSEW)
# #         elif x == 0 or x == size_desk-1:
# #             Label(bg='black', text=size_desk-y-1).grid(column=x, row=y, ipadx=7, ipady=7, sticky=NSEW)
# #         elif (x+y) % 2:
# #             Button(highlightbackground='yellow').grid(column=x, row=y, sticky=NSEW)
# #         else:
# #             Button(highlightbackground='brown').grid(column=x, row=y, sticky=NSEW)
# #
# # root.mainloop()


from tkinter import *

chess_letters = " ABCDEFGH "


def show_coordinate(button: Button):
    repaint_all()
    for index, buttons in enumerate(double_buttons):
        if button in buttons:
            position = f'{chess_letters[buttons.index(button) + 1]}{8 - index}'
            label.config(text=position, fg='black')
            position_column = int(chess_letters.index(position[0])) - 1
            position_row = 8 - int(position[1])
            text_radiobutton[rb_var.get()](position_column, position_row) if rb_var.get() != '0' else None


def repaint_all():
    for index_y, buttons in enumerate(double_buttons):
        for index_x, button in enumerate(buttons):
            config = button.config
            config(highlightbackground='brown') if (index_x + index_y) % 2 else config(highlightbackground='yellow')


def paint_cage(position_column: int, position_row: int):
    double_buttons[position_row][position_column].config(highlightbackground='blue')


def paint_horizontal(position_column: int, position_row: int):
    for y, buttons in enumerate(double_buttons):
        for x, button in enumerate(buttons):
            cage_black = (x + y) % 2
            cage_white = not cage_black
            line_vertical = x == position_column
            line_horizontal = y == position_row
            if line_horizontal and line_vertical:
                paint_cage(position_column, position_row)
            elif line_horizontal and cage_black:
                double_buttons[y][x].config(highlightbackground='green')
            elif line_horizontal and cage_white:
                double_buttons[y][x].config(highlightbackground='lightgreen')


def paint_vertical(position_column: int, position_row: int):
    for y, buttons in enumerate(double_buttons):
        for x, button in enumerate(buttons):
            cage_black = (x + y) % 2
            cage_white = not cage_black
            line_vertical = x == position_column
            line_horizontal = y == position_row
            if line_horizontal and line_vertical:
                paint_cage(position_column, position_row)
            elif line_vertical and cage_black:
                double_buttons[y][x].config(highlightbackground='green')
            elif line_vertical and cage_white:
                double_buttons[y][x].config(highlightbackground='lightgreen')


def paint_rook(position_column: int, position_row: int):
    paint_vertical(position_column, position_row)
    paint_horizontal(position_column, position_row)


def paint_main_diagonal(position_column: int, position_row: int):
    for y, buttons in enumerate(double_buttons):
        for x, button in enumerate(buttons):
            cage_black = (x + y) % 2
            cage_white = not cage_black
            line_vertical = x == position_column
            line_horizontal = y == position_row
            diagonal_nw_se = y + position_column == x + position_row
            if line_horizontal and line_vertical:
                paint_cage(position_column, position_row)
            elif diagonal_nw_se and cage_black:
                double_buttons[y][x].config(highlightbackground='green')
            elif diagonal_nw_se and cage_white:
                double_buttons[y][x].config(highlightbackground='lightgreen')


def paint_second_diagonal(position_column: int, position_row: int):
    for y, buttons in enumerate(double_buttons):
        for x, button in enumerate(buttons):
            cage_black = (x + y) % 2
            cage_white = not cage_black
            line_vertical = x == position_column
            line_horizontal = y == position_row
            diagonal_sw_ne = position_row - y == x - position_column
            if line_horizontal and line_vertical:
                paint_cage(position_column, position_row)
            elif diagonal_sw_ne and cage_black:
                double_buttons[y][x].config(highlightbackground='green')
            elif diagonal_sw_ne and cage_white:
                double_buttons[y][x].config(highlightbackground='lightgreen')


def paint_bishop(position_column: int, position_row: int):
    paint_main_diagonal(position_column, position_row)
    paint_second_diagonal(position_column, position_row)


def paint_queen(position_column: int, position_row: int):
    paint_rook(position_column, position_row)
    paint_bishop(position_column, position_row)


# def paint_three_horizontals(position_column: int, position_row: int):
#     for y, buttons in enumerate(double_buttons):
#         for x, button in enumerate(buttons):
#             cage_black = (x + y) % 2
#             cage_white = not cage_black
#             line_vertical = x == position_column
#             line_horizontal_top = position_row - 1 == y
#             line_horizontal_central = y == position_row
#             line_horizontal_down = position_row + 1 == y
#             if line_horizontal_central and line_vertical:
#                 paint_cage(position_column, position_row)
#             elif (line_horizontal_central or line_horizontal_top or line_horizontal_down) and cage_black:
#                 double_buttons[y][x].config(highlightbackground='green')
#             elif (line_horizontal_central or line_horizontal_top or line_horizontal_down) and cage_white:
#                 double_buttons[y][x].config(highlightbackground='lightgreen')
#
#
# def paint_three_verticals(position_column: int, position_row: int):
#     for y, buttons in enumerate(double_buttons):
#         for x, button in enumerate(buttons):
#             cage_black = (x + y) % 2
#             cage_white = not cage_black
#             line_horizontal = y == position_row
#             line_vertical = x == position_column
#             three_verticals_lines = position_column - 1 <= x <= position_column + 1
#             if line_horizontal and line_vertical:
#                 paint_cage(position_column, position_row)
#             elif three_verticals_lines and cage_black:
#                 double_buttons[y][x].config(highlightbackground='green')
#             elif three_verticals_lines and cage_white:
#                 double_buttons[y][x].config(highlightbackground='lightgreen')
#
#
# def paint_horizontal_to_end(position_column: int, position_row: int):
#     for y, buttons in enumerate(double_buttons):
#         for x, button in enumerate(buttons):
#             cage_black = (x + y) % 2
#             cage_white = not cage_black
#             line_horizontal = y == position_row
#             line_vertical = x == position_column
#             horizontal_to_end = position_row <= y
#             if line_horizontal and line_vertical:
#                 paint_cage(position_column, position_row)
#             elif horizontal_to_end and cage_black:
#                 double_buttons[y][x].config(highlightbackground='green')
#             elif horizontal_to_end and cage_white:
#                 double_buttons[y][x].config(highlightbackground='lightgreen')


def paint_king(position_column: int, position_row: int):
    for y, buttons in enumerate(double_buttons):
        for x, button in enumerate(buttons):
            cage_black = (x + y) % 2
            cage_white = not cage_black
            line_horizontal = y == position_row
            line_vertical = x == position_column
            three_verticals_lines = position_column - 1 <= x <= position_column + 1
            three_horizontals_lines = position_row - 1 <= y <= position_row + 1
            if line_horizontal and line_vertical:
                paint_cage(position_column, position_row)
            elif three_verticals_lines and three_horizontals_lines and cage_black:
                double_buttons[y][x].config(highlightbackground='green')
            elif three_verticals_lines and three_horizontals_lines and cage_white:
                double_buttons[y][x].config(highlightbackground='lightgreen')


def paint_knight(position_column: int, position_row: int):
    for y, buttons in enumerate(double_buttons):
        for x, button in enumerate(buttons):
            cage_black = (x + y) % 2
            cage_white = not cage_black

            line_horizontal = y == position_row
            line_vertical = x == position_column

            left_vertical = position_column - 1 == x
            right_vertical = position_column + 1 == x

            left_horizontal = position_row - 2 == y
            right_horizontal = position_row + 2 == y

            left_vertical_shift = position_column - 2 == x
            right_vertical_shift = position_column + 2 == x

            left_horizontal_shift = position_row - 1 == y
            right_horizontal_shift = position_row + 1 == y

            cage_two_left = left_vertical_shift and (right_horizontal_shift or left_horizontal_shift)
            cage_two_right = right_vertical_shift and (right_horizontal_shift or left_horizontal_shift)

            cage_two_down = (left_vertical and right_horizontal) or (right_vertical and right_horizontal)
            cage_two_up = (left_vertical and left_horizontal) or (right_vertical and left_horizontal)

            if line_horizontal and line_vertical:
                paint_cage(position_column, position_row)
            elif (cage_two_left or cage_two_right or cage_two_up or cage_two_down) and cage_black:
                double_buttons[y][x].config(highlightbackground='green')
            elif (cage_two_left or cage_two_right or cage_two_up or cage_two_down) and cage_white:
                double_buttons[y][x].config(highlightbackground='lightgreen')


root = Tk()
root.title('v4')

double_buttons = []

frame_board = Frame()
frame_board.pack(side=LEFT)

for index_y, y in enumerate(chess_letters):
    chess_buttons = []
    for index_x, x in enumerate(chess_letters):
        if index_y == 0 or index_y == len(chess_letters) - 1:
            _ = Label(frame_board, bg='black', text=chess_letters[index_x])
            _.grid(column=index_x, row=index_y, ipadx=5, ipady=4, sticky=NSEW)
        elif index_x == 0 or index_x == len(chess_letters) - 1:
            _ = Label(frame_board, bg='black', text=len(chess_letters) - index_y - 1)
            _.grid(column=index_x, row=index_y, ipadx=7, ipady=7, sticky=NSEW)
        elif (index_x + index_y) % 2:
            button = Button(frame_board, highlightbackground='brown')
            button.grid(column=index_x, row=index_y, sticky=NSEW)
            button.config(command=lambda x=button: show_coordinate(x))
            chess_buttons.append(button)
        else:
            button = Button(frame_board, highlightbackground='yellow')
            button.grid(column=index_x, row=index_y, sticky=NSEW)
            button.config(command=lambda x=button: show_coordinate(x))
            chess_buttons.append(button)
    if chess_buttons:
        double_buttons.append(chess_buttons)

frame_radiobutton = Frame()
frame_radiobutton.pack(side=RIGHT)
label = Label(frame_radiobutton, bg='orange')
label.pack(side=TOP, fill=X)
text_radiobutton = {
    'cell': paint_cage,
    'horizontal': paint_horizontal,
    'vertical': paint_vertical,
    'rook': paint_rook,
    'main diagonal': paint_main_diagonal,
    'second diagonal': paint_second_diagonal,
    'bishop': paint_bishop,
    'queen': paint_queen,
    'king': paint_king,
    'knight': paint_knight
    # '3 horizontals': paint_three_horizontals,
    # '3 verticals': paint_three_verticals,
    # 'from horizontal to end': paint_horizontal_to_end,
}

rb_var = StringVar()
rb_var.set('0')
for index, text in enumerate(text_radiobutton):
    Radiobutton(frame_radiobutton, variable=rb_var, value=text, text=text, fg='black').pack(anchor=W)

root.mainloop()

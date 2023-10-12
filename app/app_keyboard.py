# from tkinter import *
#
# keyboard_buttons = [
#     ['± 1', '1 2', '', '2 2', '', '3 2', ''],
#     ['--> 2', '', 'q 2', '', 'w 2', '', 'e 2', ''],
#     ['Caps 3', '', '', 'a 2', '', 's 2', '', 'd 2' ''],
#     ['Shift 2', '', '~ 2', '', 'z 2', '', 'x 2' ''],
#     ['fn 1', 'contr 2', '', 'opt 2', '', 'comm 2', '']
# ]
#
#
# root = Tk()
# root.title('Keyboard')
#
# for y, buttons in enumerate(keyboard_buttons):
#     for x, button in enumerate(buttons):
#         if button:
#             Button(text=button.split()[0], fg='black').grid(column=x, row=y, sticky=NSEW,
#             columnspan=button.split()[1])
#
#
# root.mainloop()


# from tkinter import *
#
# keyboard_buttons = [
#     ['§\n± 1', '!\n1 2', '@\n2 2', '#\n3 2', '$\n4 2', '%\n5 2', '^\n6 2', '&\n7 2', '*\n8 2', '(\n9 2', ')\n0 2',
#      '_\n- 2', '+\n= 2', '<- 3'],
#     ['--> 2', 'q 2', 'w 2', 'e 2', 'r 2', 't 2', 'y 2', 'u 2', 'i 2', 'o 2', 'p 2', '[ 2', '] 2', '| 2'],
#     ['Caps 3', 'a 2', 's 2', 'd 2', 'f 2', 'g 2', 'h 2', 'j 2', 'k 2', 'l 2', '; 2', '" 2', 'Enter 3'],
#     ['Shift 2', '~ 2', 'z 2', 'x 2', 'c 2', 'v 2', 'b 2', 'n 2', 'm 2', ', 2', '. 2', '/ 2', 'Shift 4'],
#     ['fn 1', 'contr 2', 'opt 2', 'comm 2', ' 11', 'comm 2', 'opt 2', '< 2', 'up\ndown 2', '> 2']
# ]
#
# root = Tk()
# root.title('Keyboard')
#
# for y, buttons in enumerate(keyboard_buttons):
#     n = 0
#     for button in buttons:
#         Button(text=button.split(' ')[0], fg='black').grid(column=n, row=y, sticky=NSEW,
#                                                            columnspan=button.split(' ')[1])
#         n += int(button.split(' ')[1])
#
#
#     # Button(text=buttons[0].split(' ')[0], fg='black').grid(column=n, row=y, sticky=NSEW, columnspan=buttons[0].split(' ')[1])
#     # n += int(buttons[0].split(' ')[1])
#     # Button(text=buttons[1].split(' ')[0], fg='black').grid(column=n, row=y, sticky=NSEW,
#     #                                                        columnspan=buttons[1].split(' ')[1])
#     # n += int(buttons[1].split(' ')[1])
#     # Button(text=buttons[2].split(' ')[0], fg='black').grid(column=n, row=y, sticky=NSEW,
#     #                                                        columnspan=buttons[2].split(' ')[1])
#     # n += int(buttons[2].split(' ')[1])
#     # Button(text=buttons[3].split(' ')[0], fg='black').grid(column=n, row=y, sticky=NSEW,
#     #                                                        columnspan=buttons[3].split(' ')[1])
#
#
# root.mainloop()


# from tkinter import *
#
# keyboard_buttons = [
#     ['§\n± 1', '!\n1 2', '@\n2 2', '#\n3 2', '$\n4 2', '%\n5 2', '^\n6 2', '&\n7 2', '*\n8 2', '(\n9 2', ')\n0 2',
#      '_\n- 2', '+\n= 2', '<- 3'],
#     ['--> 2', 'q 2', 'w 2', 'e 2', 'r 2', 't 2', 'y 2', 'u 2', 'i 2', 'o 2', 'p 2', '[ 2', '] 2', '| 2'],
#     ['Caps 3', 'a 2', 's 2', 'd 2', 'f 2', 'g 2', 'h 2', 'j 2', 'k 2', 'l 2', '; 2', '" 2', 'Enter 3'],
#     ['Shift 2', '~ 2', 'z 2', 'x 2', 'c 2', 'v 2', 'b 2', 'n 2', 'm 2', ', 2', '. 2', '/ 2', 'Shift 4'],
#     ['fn 1', 'contr 2', 'opt 2', 'comm 2', ' 11', 'comm 2', 'opt 2', '< 2', 'up\ndown 2', '> 2']
# ]
#
# root = Tk()
# root.title('Keyboard')
#
# for y, buttons in enumerate(keyboard_buttons):
#     n = 0
#     for button in buttons:
#         Button(text=button.split(' ')[0], fg='black').grid(column=n, row=y, sticky=NSEW,
#                                                            columnspan=button.split(' ')[1])
#         if button == 'up\ndown 2':
#             frame_button = Frame()
#             frame_button.grid(column=n, row=y, sticky=NSEW, columnspan=button.split(' ')[1])
#             Button(frame_button, text="Up", fg='black').grid(column=0, row=0, sticky=NSEW)
#             Button(frame_button, text="Down", fg='black').grid(column=0, row=1, sticky=NSEW)
#         n += int(button.split(' ')[1])
#           button = Button()
#           button.grid()
# root.mainloop()


# from tkinter import *
#
#
# def delete():
#     button.destroy()
#
#
# root = Tk()
# button = Button(command=delete)
# button.pack()
# root.mainloop()


# from tkinter import *
#
#
# def delete():
#     for button in buttons:
#         button.destroy()
#
#
# buttons = []
# root = Tk()
# for i in range(8):
#     button = Button()
#     button.pack(side=LEFT)
#     buttons.append(button)
# button1 = Button(text='Russia', fg='black', command=delete)
# button1.pack()
# root.mainloop()


# from tkinter import *
# keyboard_english = [
#     ['§\n± 1', '!\n1 2', '@\n2 2', '#\n3 2', '$\n4 2', '%\n5 2', '^\n6 2', '&\n7 2', '*\n8 2', '(\n9 2', ')\n0 2',
#      '_\n- 2', '+\n= 2', '<- 3'],
#     ['--> 2', 'q 2', 'w 2', 'e 2', 'r 2', 't 2', 'y 2', 'u 2', 'i 2', 'o 2', 'p 2', '[ 2', '] 2', '| 2'],
#     ['Caps 3', 'a 2', 's 2', 'd 2', 'f 2', 'g 2', 'h 2', 'j 2', 'k 2', 'l 2', '; 2', '" 2', 'Enter 3'],
#     ['Shift 2', '~ 2', 'z 2', 'x 2', 'c 2', 'v 2', 'b 2', 'n 2', 'm 2', ', 2', '. 2', '/ 2', 'Shift 4'],
#     ['fn 1', 'contr 2', 'opt 2', 'comm 2', ' 11', 'comm 2', 'opt 2', '< 2', 'up\ndown 2', '> 2']
# ]
# # 14
# # 14
# # 13
# # 13
# # 11
# keyboard_russian = [
#     ['§\n± 1', '!\n1 2', '@\n2 2', '#\n3 2', '$\n4 2', '%\n5 2', '^\n6 2', '&\n7 2', '*\n8 2', '(\n9 2', ')\n0 2',
#      '_\n- 2', '+\n= 2', '<- 3'],
#     ['--> 2', 'й 2', 'ц 2', 'у 2', 'к 2', 'е 2', 'н 2', 'г 2', 'ш 2', 'щ 2', 'з 2', 'х 2', 'ъ 2', 'ё 2'],
#     ['Caps 3', 'ф 2', 'ы 2', 'в 2', 'а 2', 'п 2', 'р 2', 'о 2', 'л 2', 'д 2', 'ж 2', 'э 2', 'Enter 3'],
#     ['Shift 2', '] 2', 'я 2', 'ч 2', 'с 2', 'м 2', 'и 2', 'т 2', 'ь 2', 'б 2', 'ю 2', '? 2', 'Shift 4'],
#     ['fn 1', 'contr 2', 'opt 2', 'comm 2', ' 11', 'comm 2', 'opt 2', '< 2', 'вверх \n вниз 2', '> 2']
# ]
#
#
# def change_language():
#     # print(len(root.winfo_children()))
#     # print(len(buttons))
#     for index, button in enumerate(buttons):
#         if index < 14:
#             # print(index)
#             button.config(text=keyboard_russian[0][index].split(" ")[0])
#             # print(button)
#             # print(keyboard_russian[0][index])
#         elif 13 < index < 28:
#             # print(button)
#             # print(keyboard_russian[1][index-14])
#             button.config(text=keyboard_russian[1][index-14].split(" ")[0])
#         elif 28 <= index < 41:
#             button.config(text=keyboard_russian[2][index - 28].split(" ")[0])
#         elif 41 <= index < 54:
#             button.config(text=keyboard_russian[3][index - 41].split(" ")[0])
#         elif 54 <= index < 65:
#             print(button['text'] == 'Up')
#             if button['text'] == 'Up':
#                 button.config(text=keyboard_russian[4][index - 54].split(" ")[0])
#             if button['text'] == 'Down':
#                 print(keyboard_russian[4][index - 55].split(" ")[2])
#                 button.config(text=keyboard_russian[4][index - 55].split(" ")[2])
#
#
#
# buttons = []
#
# root = Tk()
# root.title('Keyboard')
# for y_en, buttons_en in enumerate(keyboard_english):
#     x_en = 0
#     for button_en in buttons_en:
#         if button_en == 'up\ndown 2':
#             frame_button_en = Frame()
#             frame_button_en.grid(column=x_en, row=y_en, sticky=NSEW, columnspan=button_en.split(' ')[1])
#             button_up = Button(frame_button_en, text="Up", fg='black')
#             button_up.grid(column=0, row=0, sticky=NSEW)
#             buttons.append(button_up)
#             button_down = Button(frame_button_en, text="Down", fg='black')
#             button_down.grid(column=0, row=1, sticky=NSEW)
#             buttons.append(button_down)
#         elif button_en == 'fn 1':
#             button_change_language_en = Button(text=button_en.split(' ')[0], fg='black', command=change_language)
#             button_change_language_en.grid(column=x_en, row=y_en, sticky=NSEW)
#             buttons.append(button_change_language_en)
#         else:
#             all_buttons = Button(text=button_en.split(' ')[0], fg='black')
#             all_buttons.grid(column=x_en, row=y_en, sticky=NSEW, columnspan=button_en.split(' ')[1])
#             buttons.append(all_buttons)
#         x_en += int(button_en.split(' ')[1])
# root.mainloop()


# from tkinter import *
# keyboard_english = [
#     ['§\n± 1', '!\n1 2', '@\n2 2', '#\n3 2', '$\n4 2', '%\n5 2', '^\n6 2', '&\n7 2', '*\n8 2', '(\n9 2', ')\n0 2',
#      '_\n- 2', '+\n= 2', '<- 3'],
#     ['--> 2', 'q 2', 'w 2', 'e 2', 'r 2', 't 2', 'y 2', 'u 2', 'i 2', 'o 2', 'p 2', '[ 2', '] 2', '| 2'],
#     ['Caps 3', 'a 2', 's 2', 'd 2', 'f 2', 'g 2', 'h 2', 'j 2', 'k 2', 'l 2', '; 2', '" 2', 'Enter 3'],
#     ['Shift 2', '~ 2', 'z 2', 'x 2', 'c 2', 'v 2', 'b 2', 'n 2', 'm 2', ', 2', '. 2', '/ 2', 'Shift 4'],
#     ['fn 1', 'contr 2', 'opt 2', 'comm 2', ' 11', 'comm 2', 'opt 2', '< 2', 'up\ndown 2', '> 2']
# ]
#
# keyboard_russian = [
#     ['§\n± 1', '!\n1 2', '@\n2 2', '#\n3 2', '$\n4 2', '%\n5 2', '^\n6 2', '&\n7 2', '*\n8 2', '(\n9 2', ')\n0 2',
#      '_\n- 2', '+\n= 2', '<- 3'],
#     ['--> 2', 'й 2', 'ц 2', 'у 2', 'к 2', 'е 2', 'н 2', 'г 2', 'ш 2', 'щ 2', 'з 2', 'х 2', 'ъ 2', 'ё 2'],
#     ['Caps 3', 'ф 2', 'ы 2', 'в 2', 'а 2', 'п 2', 'р 2', 'о 2', 'л 2', 'д 2', 'ж 2', 'э 2', 'Enter 3'],
#     ['Shift 2', '] 2', 'я 2', 'ч 2', 'с 2', 'м 2', 'и 2', 'т 2', 'ь 2', 'б 2', 'ю 2', '? 2', 'Shift 4'],
#     ['fn 1', 'contr 2', 'opt 2', 'comm 2', ' 11', 'comm 2', 'opt 2', '< 2', 'вверх \n вниз 2', '> 2']
# ]
#
#
# def change_language():
#     for index, button in enumerate(buttons):
#         if index < 14:
#             button.config(text=keyboard_russian[0][index].split(" ")[0])
#         elif 13 < index < 28:
#             button.config(text=keyboard_russian[1][index-14].split(" ")[0])
#         elif 28 <= index < 41:
#             button.config(text=keyboard_russian[2][index - 28].split(" ")[0])
#         elif 41 <= index < 54:
#             button.config(text=keyboard_russian[3][index - 41].split(" ")[0])
#         elif 54 <= index < 65:
#             if button['text'] == 'Up':
#                 button.config(text=keyboard_russian[4][index - 54].split(" ")[0])
#             if button['text'] == 'Down':
#                 button.config(text=keyboard_russian[4][index - 55].split(" ")[2])
#
#
# buttons = []
#
# root = Tk()
# root.title('Keyboard')
# for y_en, buttons_en in enumerate(keyboard_english):
#     x_en = 0
#     for button_en in buttons_en:
#         if button_en == 'up\ndown 2':
#             frame_button_en = Frame()
#             frame_button_en.grid(column=x_en, row=y_en, sticky=NSEW, columnspan=button_en.split(' ')[1])
#             button_up = Button(frame_button_en, text="Up", fg='black')
#             button_up.grid(column=0, row=0, sticky=NSEW)
#             buttons.append(button_up)
#             button_down = Button(frame_button_en, text="Down", fg='black')
#             button_down.grid(column=0, row=1, sticky=NSEW)
#             buttons.append(button_down)
#         elif button_en == 'fn 1':
#             button_change_language_en = Button(text=button_en.split(' ')[0], fg='black', command=change_language)
#             button_change_language_en.grid(column=x_en, row=y_en, sticky=NSEW)
#             buttons.append(button_change_language_en)
#         else:
#             all_buttons = Button(text=button_en.split(' ')[0], fg='black')
#             all_buttons.grid(column=x_en, row=y_en, sticky=NSEW, columnspan=button_en.split(' ')[1])
#             buttons.append(all_buttons)
#         x_en += int(button_en.split(' ')[1])
# root.mainloop()


# from tkinter import *
# keyboard_english = [
#     ['§\n± 1', '!\n1 2', '@\n2 2', '#\n3 2', '$\n4 2', '%\n5 2', '^\n6 2', '&\n7 2', '*\n8 2', '(\n9 2', ')\n0 2',
#      '_\n- 2', '+\n= 2', '<- 3'],
#     ['--> 2', 'q 2', 'w 2', 'e 2', 'r 2', 't 2', 'y 2', 'u 2', 'i 2', 'o 2', 'p 2', '[ 2', '] 2', '| 2'],
#     ['Caps 3', 'a 2', 's 2', 'd 2', 'f 2', 'g 2', 'h 2', 'j 2', 'k 2', 'l 2', '; 2', '" 2', 'Enter 3'],
#     ['Shift 2', '~ 2', 'z 2', 'x 2', 'c 2', 'v 2', 'b 2', 'n 2', 'm 2', ', 2', '. 2', '/ 2', 'Shift 4'],
#     ['fn 1', 'contr 2', 'opt 2', 'comm 2', ' 11', 'comm 2', 'opt 2', '< 2', 'up\ndown 2', '> 2']
# ]
#
# keyboard_russian = [
#     ['§\n± 1', '!\n1 2', '@\n2 2', '#\n3 2', '$\n4 2', '%\n5 2', '^\n6 2', '&\n7 2', '*\n8 2', '(\n9 2', ')\n0 2',
#      '_\n- 2', '+\n= 2', '<- 3'],
#     ['--> 2', 'й 2', 'ц 2', 'у 2', 'к 2', 'е 2', 'н 2', 'г 2', 'ш 2', 'щ 2', 'з 2', 'х 2', 'ъ 2', 'ё 2'],
#     ['Caps 3', 'ф 2', 'ы 2', 'в 2', 'а 2', 'п 2', 'р 2', 'о 2', 'л 2', 'д 2', 'ж 2', 'э 2', 'Enter 3'],
#     ['Shift 2', '] 2', 'я 2', 'ч 2', 'с 2', 'м 2', 'и 2', 'т 2', 'ь 2', 'б 2', 'ю 2', '? 2', 'Shift 4'],
#     ['fn 1', 'contr 2', 'opt 2', 'comm 2', ' 11', 'comm 2', 'opt 2', '< 2', 'вверх\nвниз 2', '> 2']
# ]
#
#
# def change_language():
#     if buttons[15]['text'] == 'q':
#         for index, button in enumerate(buttons):
#             if index < 14:
#                 button.config(text=keyboard_russian[0][index].split(" ")[0])
#             elif 13 < index < 28:
#                 button.config(text=keyboard_russian[1][index-14].split(" ")[0])
#             elif 28 <= index < 41:
#                 button.config(text=keyboard_russian[2][index - 28].split(" ")[0])
#             elif 41 <= index < 54:
#                 button.config(text=keyboard_russian[3][index - 41].split(" ")[0])
#             elif 54 <= index < 65:
#                 if button['text'] == 'up':
#                     button.config(text=keyboard_russian[4][index - 54].split(" ")[0].split("\n")[0])
#                 if button['text'] == 'down':
#                     # print(keyboard_russian[4][index - 55].split(" ")[0][5:10])
#                     button.config(text=keyboard_russian[4][index - 55].split(" ")[0].split("\n")[1])
#     else:
#         for index, button in enumerate(buttons):
#             if index < 14:
#                 button.config(text=keyboard_english[0][index].split(" ")[0])
#             elif 13 < index < 28:
#                 button.config(text=keyboard_english[1][index-14].split(" ")[0])
#             elif 28 <= index < 41:
#                 button.config(text=keyboard_english[2][index - 28].split(" ")[0])
#             elif 41 <= index < 54:
#                 button.config(text=keyboard_english[3][index - 41].split(" ")[0])
#             elif 54 <= index < 65:
#                 if button['text'] == 'вверх':
#                     button.config(text=keyboard_english[4][index - 54].split(" ")[0].split("\n")[0])
#                 if button['text'] == 'вниз':
#                     button.config(text=keyboard_english[4][index - 55].split(" ")[0].split("\n")[1])
#
#
# buttons = []
#
# root = Tk()
# root.title('Keyboard')
# for y_en, buttons_en in enumerate(keyboard_english):
#     x_en = 0
#     for button_en in buttons_en:
#         if button_en == 'up\ndown 2':
#             frame_button_en = Frame()
#             frame_button_en.grid(column=x_en, row=y_en, sticky=NSEW, columnspan=button_en.split(' ')[1])
#             button_up = Button(frame_button_en, text=button_en.split(' ')[0].split('\n')[0], fg='black')
#             button_up.grid(column=0, row=0, sticky=NSEW)
#             buttons.append(button_up)
#             button_down = Button(frame_button_en, text=button_en.split(' ')[0].split('\n')[1], fg='black')
#             button_down.grid(column=0, row=1, sticky=NSEW)
#             buttons.append(button_down)
#         elif button_en == 'fn 1':
#             button_change_language_en = Button(text=button_en.split(' ')[0], fg='black', command=change_language)
#             button_change_language_en.grid(column=x_en, row=y_en, sticky=NSEW)
#             buttons.append(button_change_language_en)
#         else:
#             all_buttons = Button(text=button_en.split(' ')[0], fg='black')
#             all_buttons.grid(column=x_en, row=y_en, sticky=NSEW, columnspan=button_en.split(' ')[1])
#             buttons.append(all_buttons)
#         x_en += int(button_en.split(' ')[1])
# root.mainloop()


# from tkinter import *
# keyboard_english = [
#     ['§\n± 1', '!\n1 2', '@\n2 2', '#\n3 2', '$\n4 2', '%\n5 2', '^\n6 2', '&\n7 2', '*\n8 2', '(\n9 2', ')\n0 2',
#      '_\n- 2', '+\n= 2', '<- 3'],
#     ['--> 2', 'q 2', 'w 2', 'e 2', 'r 2', 't 2', 'y 2', 'u 2', 'i 2', 'o 2', 'p 2', '[ 2', '] 2', '| 2'],
#     ['Caps 3', 'a 2', 's 2', 'd 2', 'f 2', 'g 2', 'h 2', 'j 2', 'k 2', 'l 2', '; 2', '" 2', 'Enter 3'],
#     ['Shift 2', '~ 2', 'z 2', 'x 2', 'c 2', 'v 2', 'b 2', 'n 2', 'm 2', ', 2', '. 2', '/ 2', 'Shift 4'],
#     ['fn 1', 'contr 2', 'opt 2', 'comm 2', ' 11', 'comm 2', 'opt 2', '< 2', 'up\ndown 2', '> 2']
# ]
#
# keyboard_russian = [
#     ['§\n± 1', '!\n1 2', '@\n2 2', '#\n3 2', '$\n4 2', '%\n5 2', '^\n6 2', '&\n7 2', '*\n8 2', '(\n9 2', ')\n0 2',
#      '_\n- 2', '+\n= 2', '<- 3'],
#     ['--> 2', 'й 2', 'ц 2', 'у 2', 'к 2', 'е 2', 'н 2', 'г 2', 'ш 2', 'щ 2', 'з 2', 'х 2', 'ъ 2', 'ё 2'],
#     ['Caps 3', 'ф 2', 'ы 2', 'в 2', 'а 2', 'п 2', 'р 2', 'о 2', 'л 2', 'д 2', 'ж 2', 'э 2', 'Enter 3'],
#     ['Shift 2', '] 2', 'я 2', 'ч 2', 'с 2', 'м 2', 'и 2', 'т 2', 'ь 2', 'б 2', 'ю 2', '? 2', 'Shift 4'],
#     ['fn 1', 'contr 2', 'opt 2', 'comm 2', ' 11', 'comm 2', 'opt 2', '< 2', 'вверх\nвниз 2', '> 2']
# ]
#
#
# def change_language():
#     if buttons[15]['text'] == 'q':
#         current_buttons = keyboard_russian
#         key_up = 'up'
#         key_down = 'down'
#     else:
#         current_buttons = keyboard_english
#         key_up = 'вверх'
#         key_down = 'вниз'
#
#     for index, button in enumerate(buttons):
#         if index < 14:
#             button.config(text=current_buttons[0][index].split(" ")[0])
#         elif 13 < index < 28:
#             button.config(text=current_buttons[1][index-14].split(" ")[0])
#         elif 28 <= index < 41:
#             button.config(text=current_buttons[2][index - 28].split(" ")[0])
#         elif 41 <= index < 54:
#             button.config(text=current_buttons[3][index - 41].split(" ")[0])
#         elif 54 <= index < 65:
#             if button['text'] == key_up:
#                 button.config(text=current_buttons[4][index - 54].split(" ")[0].split("\n")[0])
#             if button['text'] == key_down:
#                 button.config(text=current_buttons[4][index - 55].split(" ")[0].split("\n")[1])
#
#
# buttons = []
#
# root = Tk()
# root.title('Keyboard_v3')
# for y_en, buttons_en in enumerate(keyboard_english):
#     x_en = 0
#     for button_en in buttons_en:
#         if button_en == 'up\ndown 2':
#             frame_button_en = Frame()
#             frame_button_en.grid(column=x_en, row=y_en, sticky=NSEW, columnspan=button_en.split(' ')[1])
#             button_up = Button(frame_button_en, text=button_en.split(' ')[0].split('\n')[0], fg='black')
#             button_up.grid(column=0, row=0, sticky=NSEW)
#             buttons.append(button_up)
#             button_down = Button(frame_button_en, text=button_en.split(' ')[0].split('\n')[1], fg='black')
#             button_down.grid(column=0, row=1, sticky=NSEW)
#             buttons.append(button_down)
#         elif button_en == 'fn 1':
#             button_change_language_en = Button(text=button_en.split(' ')[0], fg='black', command=change_language)
#             button_change_language_en.grid(column=x_en, row=y_en, sticky=NSEW)
#             buttons.append(button_change_language_en)
#         else:
#             all_buttons = Button(text=button_en.split(' ')[0], fg='black')
#             all_buttons.grid(column=x_en, row=y_en, sticky=NSEW, columnspan=button_en.split(' ')[1])
#             buttons.append(all_buttons)
#         x_en += int(button_en.split(' ')[1])
# root.mainloop()


from tkinter import *
keyboard_english = [
    ['§\n± 1', '!\n1 2', '@\n2 2', '#\n3 2', '$\n4 2', '%\n5 2', '^\n6 2', '&\n7 2', '*\n8 2', '(\n9 2', ')\n0 2',
     '_\n- 2', '+\n= 2', '<- 3'],
    ['--> 2', 'q 2', 'w 2', 'e 2', 'r 2', 't 2', 'y 2', 'u 2', 'i 2', 'o 2', 'p 2', '[ 2', '] 2', '| 2'],
    ['Caps 3', 'a 2', 's 2', 'd 2', 'f 2', 'g 2', 'h 2', 'j 2', 'k 2', 'l 2', '; 2', '" 2', 'Enter 3'],
    ['Shift 2', '~ 2', 'z 2', 'x 2', 'c 2', 'v 2', 'b 2', 'n 2', 'm 2', ', 2', '. 2', '/ 2', 'Shift 4'],
    ['fn 1', 'contr 2', 'opt 2', 'comm 2', ' 11', 'comm 2', 'opt 2', '< 2', 'up\ndown 2', '> 2']
]

keyboard_russian = [
    ['§\n± 1', '!\n1 2', '@\n2 2', '#\n3 2', '$\n4 2', '%\n5 2', '^\n6 2', '&\n7 2', '*\n8 2', '(\n9 2', ')\n0 2',
     '_\n- 2', '+\n= 2', '<- 3'],
    ['--> 2', 'й 2', 'ц 2', 'у 2', 'к 2', 'е 2', 'н 2', 'г 2', 'ш 2', 'щ 2', 'з 2', 'х 2', 'ъ 2', 'ё 2'],
    ['Caps 3', 'ф 2', 'ы 2', 'в 2', 'а 2', 'п 2', 'р 2', 'о 2', 'л 2', 'д 2', 'ж 2', 'э 2', 'Enter 3'],
    ['Shift 2', '] 2', 'я 2', 'ч 2', 'с 2', 'м 2', 'и 2', 'т 2', 'ь 2', 'б 2', 'ю 2', '? 2', 'Shift 4'],
    ['fn 1', 'contr 2', 'opt 2', 'comm 2', ' 11', 'comm 2', 'opt 2', '< 2', 'вверх\nвниз 2', '> 2']
]


def change_language():
    if buttons[15]['text'] == 'q':
        current_buttons = keyboard_russian
        key_up = 'up'
        key_down = 'down'
    else:
        current_buttons = keyboard_english
        key_up = 'вверх'
        key_down = 'вниз'

    for index, button in enumerate(buttons):
        if index < 14:
            button.config(text=current_buttons[0][index].split(" ")[0])
        elif 13 < index < 28:
            button.config(text=current_buttons[1][index-14].split(" ")[0])
        elif 28 <= index < 41:
            button.config(text=current_buttons[2][index - 28].split(" ")[0])
        elif 41 <= index < 54:
            button.config(text=current_buttons[3][index - 41].split(" ")[0])
        elif 54 <= index < 65:
            if button['text'] == key_up:
                button.config(text=current_buttons[4][index - 54].split(" ")[0].split("\n")[0])
            if button['text'] == key_down:
                button.config(text=current_buttons[4][index - 55].split(" ")[0].split("\n")[1])


buttons = []

root = Tk()
root.title('Keyboard_v4')

for y_en, buttons_en in enumerate(keyboard_english):
    x_en = 0
    for button_en in buttons_en:
        if button_en == 'up\ndown 2':
            frame_button_en = Frame()
            frame_button_en.grid(column=x_en, row=y_en, sticky=NSEW, columnspan=button_en.split(' ')[1])
            button_up = Button(frame_button_en, text=button_en.split(' ')[0].split('\n')[0], fg='black')
            button_up.grid(column=0, row=0, sticky=NSEW)
            buttons.append(button_up)
            button_down = Button(frame_button_en, text=button_en.split(' ')[0].split('\n')[1], fg='black')
            button_down.grid(column=0, row=1, sticky=NSEW)
            buttons.append(button_down)
        elif button_en == 'fn 1':
            button_change_language_en = Button(text=button_en.split(' ')[0], fg='black', command=change_language)
            button_change_language_en.grid(column=x_en, row=y_en, sticky=NSEW)
            buttons.append(button_change_language_en)
        else:
            all_buttons = Button(text=button_en.split(' ')[0], fg='black')
            all_buttons.grid(column=x_en, row=y_en, sticky=NSEW, columnspan=button_en.split(' ')[1])
            buttons.append(all_buttons)
        x_en += int(button_en.split(' ')[1])
root.mainloop()



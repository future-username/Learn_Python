# from tkinter import *
#
# keyboard_russian = [
#     ['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х'],
#     ['ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э'],
#     ['Shift', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '<-'],
#     ['123', 'en', 'Пробел', 'Найти']
# ]
#
# keyboard_english = [
#     ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
#     ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
#     ['Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<-'],
#     ['123', 'ru', 'space', 'search']
# ]
#
#
# def change_language():
#     if buttons[34]['text'] == 'en':
#         for index, current_button in enumerate(buttons):
#             if index <= 9:
#                 current_button.config(text=keyboard_english[0][index])
#             elif 11 <= index <= 19:
#                 current_button.config(text=keyboard_english[1][index-11])
#             elif 22 <= index <= 30:
#                 current_button.config(text=keyboard_english[2][index-22])
#             elif 33 <= index <= 39:
#                 current_button.config(text=keyboard_english[3][index - 33])
#             elif index == 10 or index == 20 or index == 21 or index == 31 or index == 32:
#                 current_button.pack_forget()
#     else:
#         for index, current_button in enumerate(buttons):
#             current_button.pack(side=LEFT)
#             if index <= 9:
#                 current_button.config(text=keyboard_russian[0][index])
#             elif 11 <= index <= 21:
#                 current_button.config(text=keyboard_russian[1][index-11])
#             elif 22 <= index <= 30:
#                 current_button.config(text=keyboard_russian[2][index-22])
#             elif 33 <= index <= 39:
#                 current_button.config(text=keyboard_russian[3][index - 33])
#
#
# buttons = []
#
# root = Tk()
# root.title('Keyboard_phone_v1')
# for titles in keyboard_russian:
#     label = Frame()
#     label.pack(fill=X)
#     for text_button in titles:
#         if text_button != '123' and text_button != 'en' and text_button != 'Найти':
#             button = Button(label, text=text_button, fg='black')
#             button.pack(side=LEFT, fill=X, expand=1)
#             buttons.append(button)
#         elif text_button == 'en':
#             button = Button(label, text=text_button, fg='black', command=change_language)
#             button.pack(side=LEFT)
#             buttons.append(button)
#         else:
#             button = Button(label, text=text_button, fg='black')
#             button.pack(side=LEFT)
#             buttons.append(button)
#
#
# root.mainloop()


# from tkinter import *
#
# keyboard_russian = [
#     ['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х'],
#     ['ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э'],
#     ['Shift', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '<-'],
#     ['123', 'en', 'Пробел', 'Найти']
# ]
#
# keyboard_english = [
#     ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
#     ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
#     ['Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<-'],
#     ['123', 'ru', 'space', 'search']
# ]
#
#
# def change_language():
#     if buttons[34]['text'] == 'en':
#         current_keyboard = keyboard_english
#     else:
#         current_keyboard = keyboard_russian
#
#     for index, current_button in enumerate(buttons):
#         if index <= 9:
#             current_button.config(text=current_keyboard[0][index])
#         elif 11 <= index <= 19:
#             current_button.config(text=current_keyboard[1][index-11])
#         elif 22 <= index <= 30:
#             current_button.config(text=current_keyboard[2][index-22])
#         elif 33 <= index <= 39:
#             current_button.config(text=current_keyboard[3][index - 33])
#
#         if current_keyboard == keyboard_english and (index == 10 or index == 20 or
#                                                      index == 21 or index == 31 or index == 32):
#             current_button.pack_forget()
#         else:
#             current_button.pack(side=LEFT)
#
#
# buttons = []
#
# root = Tk()
# root.title('Keyboard_phone_v2')
# for titles in keyboard_russian:
#     label = Frame()
#     label.pack(fill=X)
#     for text_button in titles:
#         if text_button != '123' and text_button != 'en' and text_button != 'Найти':
#             button = Button(label, text=text_button, fg='black')
#             button.pack(side=LEFT, fill=X, expand=1)
#             buttons.append(button)
#         elif text_button == 'en':
#             button = Button(label, text=text_button, fg='black', command=change_language)
#             button.pack(side=LEFT)
#             buttons.append(button)
#         else:
#             button = Button(label, text=text_button, fg='black')
#             button.pack(side=LEFT)
#             buttons.append(button)
#
# root.mainloop()


# from tkinter import *
#
# keyboard_russian = [
#     ['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х'],
#     ['ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э'],
#     ['Shift', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '<-'],
#     ['123', 'en', 'Пробел', 'Найти']
# ]
#
# keyboard_english = [
#     ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
#     ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
#     ['Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<-'],
#     ['123', 'ru', 'space', 'search']
# ]
#
#
# def change_language():
#     if buttons[34]['text'] == 'en':
#         current_keyboard = keyboard_english
#     else:
#         current_keyboard = keyboard_russian
#
#     for index, current_button in enumerate(buttons):
#         if index <= 9:
#             current_button.config(text=current_keyboard[0][index])
#         elif 11 <= index <= 19:
#             current_button.config(text=current_keyboard[1][index-11])
#         elif 22 <= index <= 30:
#             current_button.config(text=current_keyboard[2][index-22])
#         elif 33 <= index <= 39:
#             current_button.config(text=current_keyboard[3][index - 33])
#
#         if current_keyboard == keyboard_english and (index == 10 or index == 20 or
#                                                      index == 21 or index == 31 or index == 32):
#             current_button.pack_forget()
#         else:
#             current_button.pack(side=LEFT)
#
#
# buttons = []
#
# root = Tk()
# root.title('Keyboard_phone_v2')
# for titles in keyboard_russian:
#     new_buttons = []
#     label = Frame()
#     label.pack(fill=X)
#     for text_button in titles:
#         if text_button != '123' and text_button != 'en' and text_button != 'Найти':
#             button = Button(label, text=text_button, fg='black')
#             button.pack(side=LEFT, fill=X, expand=1)
#             buttons.append(button)
#         elif text_button == 'en':
#             button = Button(label, text=text_button, fg='black', command=change_language)
#             button.pack(side=LEFT)
#             buttons.append(button)
#         else:
#             button = Button(label, text=text_button, fg='black')
#             button.pack(side=LEFT)
#             buttons.append(button)
#
# root.mainloop()


# from tkinter import *
#
# keyboard_russian = [
#     ['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ'],
#     ['ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'ё'],
#     ['Shift', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '<-'],
#     ['123', 'en', 'Пробел', 'Найти']
# ]
#
# keyboard_english = [
#     ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
#     ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
#     ['Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<-'],
#     ['123', 'ru', 'space', 'search']
# ]
#
#
# def change_language():
#     if buttons[-1][1]['text'] == 'en':
#         current_keyboard = keyboard_english
#     else:
#         current_keyboard = keyboard_russian
#     for y, key_inscriptions in enumerate(buttons):
#         for x, key_inscription in enumerate(key_inscriptions):
#             if x < len(current_keyboard[y]):
#                 key_inscription.config(text=current_keyboard[y][x])
#             if current_keyboard == keyboard_english and\
#                     (keyboard_russian[y][x] == 'х' or keyboard_russian[y][x] == 'ъ' or
#                      keyboard_russian[y][x] == 'ж' or keyboard_russian[y][x] == 'э' or
#                      keyboard_russian[y][x] == 'ё' or keyboard_russian[y][x] == 'ю' or keyboard_russian[y][x] == '<-'):
#                 key_inscription.pack_forget()
#             else:
#                 key_inscription.pack(side=LEFT)
#
#
# buttons = []
# root = Tk()
# root.title('Keyboard_phone_v3')
# for titles in keyboard_russian:
#     new_buttons = []
#     label = Frame()
#     label.pack(fill=X)
#     for text_button in titles:
#         if text_button != '123' and text_button != 'en' and text_button != 'Найти':
#             button = Button(label, text=text_button, fg='black')
#             button.pack(side=LEFT, fill=X, expand=1)
#             new_buttons.append(button)
#         elif text_button == 'en':
#             button = Button(label, text=text_button, fg='black', command=change_language)
#             button.pack(side=LEFT)
#             new_buttons.append(button)
#         else:
#             button = Button(label, text=text_button, fg='black')
#             button.pack(side=LEFT)
#             new_buttons.append(button)
#     buttons.append(new_buttons)
# root.mainloop()


from tkinter import *

keyboard_russian = [
    ['й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ'],
    ['ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'ё'],
    ['Shift', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю', '<-'],
    ['123', 'en', 'Пробел', 'Найти']
]

keyboard_english = [
    ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    ['Shift', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '<-'],
    ['123', 'ru', 'space', 'search']
]


def change_language():
    extra_simbols = []
    if buttons[-1][1]['text'] == 'en':
        current_keyboard = keyboard_english
    else:
        current_keyboard = keyboard_russian

    for y, key_inscriptions in enumerate(buttons):
        different_simbols = len(keyboard_russian[y]) - len(keyboard_english[y])
        different_list = keyboard_russian[y][-different_simbols:]
        if different_simbols:
            extra_simbols.extend(different_list)
        for x, key_inscription in enumerate(key_inscriptions):
            if x < len(current_keyboard[y]):
                key_inscription.config(text=current_keyboard[y][x])
            if current_keyboard == keyboard_english and keyboard_russian[y][x] in extra_simbols:
                key_inscription.pack_forget()
            else:
                key_inscription.pack(side=LEFT)


buttons = []
root = Tk()
root.title('Keyboard_phone_v3')
for titles in keyboard_russian:
    new_buttons = []
    label = Frame()
    label.pack(fill=X)
    for text_button in titles:
        if text_button != '123' and text_button != 'en' and text_button != 'Найти':
            button = Button(label, text=text_button, fg='black')
            button.pack(side=LEFT, fill=X, expand=1)
            new_buttons.append(button)
        elif text_button == 'en':
            button = Button(label, text=text_button, fg='black', command=change_language)
            button.pack(side=LEFT)
            new_buttons.append(button)
        else:
            button = Button(label, text=text_button, fg='black')
            button.pack(side=LEFT)
            new_buttons.append(button)
    buttons.append(new_buttons)
root.mainloop()



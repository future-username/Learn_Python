# file_read = open('data.txt', 'w+')
# print(file_read.read(10))      # 'one - 1 - '
# print(file_read.read(2))       # 'I\n'
# print(file_read.read())        # 'two - 2 - II\nthree - 3 - III\nfour - 4 - IV\nfive - 5 - V\n'
# print(file_read.read())        # ''
# print(type(file_read.read()))
# file_read.write('1')


# file_read = open('data.txt')
# print(file_read.readline())    # 'one - 1 - I\n'
# print(file_read.readline())    # 'two - 2 - II\n'
# print(file_read.readline())


# for line in open('data.txt'):
#     print(line)


# numbers = []
# for line in open('data.txt'):
#     numbers.append(line.strip())
#
# print(numbers)


# file_read = open('new_numbers.txt')
# numbers = file_read.readlines()
# s = 0
# for number in numbers:
#     list_numbers = number.split()
#     for new_number in list_numbers:
#         if new_number.isdigit():
#             s += int(new_number)
# print(s)


# s = 0
# for number in open('new_numbers.txt'):
#     for new_number in number.split():
#         s = s + int(new_number) if new_number.isdigit() else s
# print(s)


# s = 0
# for number in open('goods.txt'):
#     for new_number in number.split():
#         s = s + int(new_number) if new_number.isdigit() else s
# print(s)


# s = 0
# for number in open('goods.txt'):
#     for new_number in number.split('-'):
#         new_number = new_number.strip('\n')
#         count_dots = new_number.replace(" ", "").replace(",", ".").count(".") == 1
#         float_number = new_number.replace(",", ".").replace(".", "").replace(" ", "").isdigit()
#         int_number = new_number.replace(' ', '').isdigit()
#         if count_dots and float_number or int_number:
#             s = s + float(new_number.replace(' ', '').replace(",", "."))
# print(s.__round__(2))


# summery = 0
# for purchase in open('goods.txt'):
#     purchase_price = purchase.strip('\n').partition(' - ')[2].replace(",", ".").replace(' ', '')
#     float_number = purchase_price.count(".") == 1 and purchase_price.replace(".", "").isdigit() or purchase_price.isdigit()
#     summery = summery + float(purchase_price) if float_number else summery
# print(summery.__round__(2))


from tkinter import *
from tkinter.ttk import *


def check_answers():
    true_answers = []
    win_positions = 0
    lose_positions = 0
    for index_question, question_answers in enumerate(questions):
        for index_line, text_item in enumerate(question_answers):
            if '+' in text_item:
                true_answers.append(index_line)
    for index, user_answer in enumerate(value_answer):
        if user_answer.get() == true_answers[index]:
            win_positions += 1
        else:
            lose_positions += 1
    label.config(text=f'Correct:{win_positions}\tWrong:{lose_positions}'.expandtabs(38))


root = Tk()

button_check = Button(text='Check', command=check_answers)
button_check.pack(side=TOP)
label = Label()
label.pack(side=TOP)
questions = []
question = []
for text in open('new'):
    text = text.replace('-', '').strip()
    if text[:1].isdigit():
        question = []
        questions.append(question)
    if text:
        question.append(text)

value_answer = []
for number_question, lines in enumerate(questions):
    choose_value = IntVar()
    for number_line, line in enumerate(lines):
        line = line.replace('+', '').strip()
        if number_question != 0 and line[:1].isdigit():
            Label().pack(anchor=W)
        if line[:1].isdigit():
            Label(text=line).pack(anchor=W)
        else:
            user_answers = Radiobutton(text=line, variable=choose_value, value=number_line)
            user_answers.pack(side=TOP, fill=X)
    value_answer.append(choose_value)

root.mainloop()


# list_numbers = ['tree', 'four']
# file_write = open('new_data.txt', 'w')
# print(file_write.write('one\n'))                # 4
# print(file_write.write('two'))                  # 3
# print(file_write.writelines(list_numbers))      # None
# file_read.close()
# print(file_read.closed)         # True
# print(file_write.closed)        # False

# week_days = [
#     ["1. Monday"],
#     ['2. Tuesday'],
#     ['3. Wednesday'],
#     ['4. Thursday'],
#     ['5. Friday'],
#     ['6. Saturday'],
#     ['7. Sunday']
# ]
# week_days = ["1. Monday", '2. Tuesday', '3. Wednesday', '4. Thursday', '5. Friday', '6. Saturday', '7. Sunday']
# open('weak_days.txt', 'w').write('\n'.join(week_days))

# data_en = ['four - 4 - IV', 'two - 2 - II', 'one - 1 - I', 'three - 3 - III', 'five - 5 - V',
#            'four - 4 - IV', 'one - 1 - I']
# open('data.txt', 'w').write('\n'.join(data_en))


# data_en = ['one', 'two', 'three', 'four', 'five']
# data_ru = ['один', 'два', 'три', 'четыре', 'пять']
# data_result = []
# data_translate = []
# for data in open('data.txt'):
#     data_result.append(data.strip())
# for line_numbers in data_result:
#     number_name = line_numbers.replace(' ', '').split('-')[0]
#     if number_name in data_en:
#         index_data_en = data_en.index(number_name)
#         number_ru = number_name.replace(number_name, data_ru[index_data_en])
#         data_translate.append(line_numbers.replace(number_name, number_ru))
#
# file_numbers = open('data_ru.txt', 'w')
# file_numbers.write('\n'.join(data_translate))
# file_numbers.close()


# from tkinter import *
#
#
# def save_to_file():
#     select = list(list_box.curselection())
#     select_element = []
#     if select and list_box:
#         for index in select:
#             select_element.append(list_box.get(index))
#     file = open('listbox_text.txt', 'w')
#     file.write('\n'.join(select_element))
#     file.close()
#
#
# root = Tk()
# Button(text='save to file', command=save_to_file).pack()
# list_box = Listbox(selectmode=EXTENDED)
# list_box.pack(side=LEFT, fill=BOTH, expand=1)
# list_box.insert(END, '1', '2', '3')
# scroll = Scrollbar(command=list_box.yview)
# scroll.pack(side=LEFT)
# list_box.config(yscrollcommand=scroll.set)
#
# root.mainloop()


# from tkinter import *
#
#
# def upload_to_file():
#     for data in open('listbox_text.txt'):
#         list_box.insert(END, data)
#
#
# root = Tk()
# Button(text='upload to file', command=upload_to_file).pack()
# list_box = Listbox(selectmode=EXTENDED)
# list_box.pack(side=LEFT, fill=BOTH, expand=1)
# scroll = Scrollbar(command=list_box.yview)
# scroll.pack(side=LEFT)
# list_box.config(yscrollcommand=scroll.set)
#
# root.mainloop()


# from tkinter import *
#
#
# def add_item():
#     if entry.get():
#         list_box.insert(END, entry.get())
#         entry.delete(0, END)
#
#
# def del_list():
#     select = list(list_box.curselection())
#     select.reverse()
#     for element in select:
#         list_box.delete(element)
#
#
# def upload_to_file():
#     for data in open('new'):
#         list_box.insert(END, data.strip())
#
#
# def save_to_file():
#     data = list_box.get(0, END)
#     file = open('listbox_text_new.txt', 'w')
#     file.write('\n'.join(data))
#     # file.writelines(data)
#     file.close()
#
#
# root = Tk()
# entry = Entry()
# entry.pack(anchor=N)
# Button(text="Add", command=add_item).pack()
# Button(text="Delete", command=del_list).pack()
# Button(text='Upload to file', command=upload_to_file).pack()
# Button(text='Save to file', command=save_to_file).pack()
# list_box = Listbox(selectmode=EXTENDED)
# list_box.pack(side=LEFT, fill=BOTH, expand=1)
# scroll = Scrollbar(command=list_box.yview)
# scroll.pack(side=LEFT)
# list_box.config(yscrollcommand=scroll.set)
#
# root.mainloop()


# from tkinter import *
# from tkinter import filedialog
# import random
#
# counter = 1
#
#
# def add_question():
#     global counter
#     result_true_answers = None
#     result_false_answers = None
#     question_data = None
#     text_question_clear = text_question.get(1.0, END).strip()
#     if text_question_clear:
#         question_data = f'{counter}.{text_question_clear}\n'
#
#     text_true_answer_clear = text_true_answer.get(1.0, END).strip()
#     if text_true_answer_clear:
#         true_answer_data = text_true_answer_clear.split('\n')
#         result_true_answers = []
#         for answer in true_answer_data:
#             result_true_answers.append(f'+{answer}')
#
#     text_false_answer_clear = text_false_answer.get(1.0, END).strip()
#     if text_false_answer_clear:
#         result_false_answers = text_false_answer_clear.split('\n')
#
#     result_answer_data = []
#     if result_true_answers and result_false_answers:
#         result_answer_data.extend(result_true_answers)
#         result_answer_data.extend(result_false_answers)
#         random.shuffle(result_answer_data)
#
#     if question_data and result_answer_data:
#         answer = '\n'.join(result_answer_data)
#         result_data = f'{question_data}{answer}\n'
#         text_result_document.insert(INSERT, result_data)
#         counter += 1
#         text_question.delete(1.0, END)
#         text_true_answer.delete(1.0, END)
#         text_false_answer.delete(1.0, END)
#
#
# def save_to_file():
#     document_save = filedialog.asksaveasfilename()
#     data = text_result_document.get(1.0, END)
#     file = open(document_save, 'w')
#     file.writelines(data)
#     file.close()
#
#
# root = Tk()
#
# frame_left = Frame()
# frame_left.pack(side=LEFT, fill=BOTH, expand=1)
#
# frame_question = LabelFrame(frame_left, text='Question:')
# frame_question.pack(fill=BOTH, expand=1)
# text_question = Text(frame_question, width=40, height=5)
# text_question.pack(fill=BOTH, expand=1)
#
# frame_true_answer = LabelFrame(frame_left, text='True answer:')
# frame_true_answer.pack(fill=BOTH, expand=1)
# text_true_answer = Text(frame_true_answer, width=40, height=5)
# text_true_answer.pack(fill=BOTH, expand=1)
#
# frame_false_answer = LabelFrame(frame_left, text='False answer:')
# frame_false_answer.pack(fill=BOTH, expand=1)
# text_false_answer = Text(frame_false_answer, width=40, height=10)
# text_false_answer.pack(side=LEFT, fill=BOTH, expand=1)
# scroll_false_answer = Scrollbar(frame_false_answer, command=text_false_answer.yview)
# scroll_false_answer.pack(side=LEFT)
# text_false_answer.config(yscrollcommand=scroll_false_answer.set)
#
# Button(frame_left, text='Add question ->', command=add_question).pack()
#
# frame_right = Frame()
# frame_right.pack(side=RIGHT, fill=BOTH, expand=1)
# frame_final_document = LabelFrame(frame_right, text='Final document with questions:')
# frame_final_document.pack(side=TOP, fill=BOTH, expand=1)
# text_result_document = Text(frame_final_document, width=40, height=25)
# text_result_document.pack(side=LEFT, fill=BOTH, expand=1)
# scroll_frame_right = Scrollbar(frame_final_document, command=text_result_document.yview)
# scroll_frame_right.pack(side=LEFT)
# text_result_document.config(yscrollcommand=scroll_frame_right.set)
#
# Button(frame_right, text='Save file', command=save_to_file).pack(side=BOTTOM)
#
# root.mainloop()

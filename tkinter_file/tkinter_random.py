# import random
#
# print(random.randint(0, 10))
# print(random.shuffle(0, 100))


# import random
#
# mylist = ["apple", "banana", "cherry", "1", "2"]
# random.shuffle(mylist)
# print(mylist)


# import random
#
# a = random.random()
# print(a)                # 0.8366142721623201
# print(round(a, 1))      # 0.84
# print(round(random.random(), 3))


# import random
# print(random.random() * 100)     # 2.510618091637596
# print(random.random() * 10)


# import random
# print(random.random() * (10 - 4) + 4)   # 9.517280589233597
# print(random.random() * (10 - 4) + 4)   # 6.4429124181215975
# print(random.random() * (10 - 4) + 4)


# print(random.random() * (1 + 1) - 1)    # -0.673382618351051
# print(random.random() * (1 + 1) - 1)    # 0.34121487148075924
# print(random.random() * (1 + 1) - 1)    # -0.988751324713907
# print(random.random() * (1 + 1) - 1)


# print(int(random.random() * 100))       # 61
# print(round(random.random() * 100 - 50))     # -33


# import random
# print(random.randrange(6, 13, 2))
# print(random.randrange(5, 100, 5))


# import random
# number_from = int(input("enter the number from:"))
# number_to = int(input("enter the number to:"))
# number_type = input("Enter number '1' - integer or 2 - float:")
# if number_type == 1:
#     print(random.randint(number_from, number_to))
# else:
#     print(round(random.randint(number_from, number_to - 1) + random.random(), 2))


# import random
# print(int(random.random() * 7))
# print(int(random.random() * 20 + 10))
# print(int(random.random() * 14 - 7))
# print(int(random.random() * 5) * 2)
# print(int(random.random() * 8) * 3)
# print(int(random.random() * 5) * 4 + 20)
# print(int(random.random() * 12) * 2 - 14)
# print(int(random.random() * 9) * 0.5)
# print(int(random.random() * 56) * 0.25 + 7)
# print(int(random.random() * 4) * 1.25 - 2.5)


from tkinter import *
from tkinter.ttk import *
import random


def generate_number():
    first = first_entry.get()
    second = second_entry.get()
    third = step_entry.get()
    # label.config(text=f'Result:{int(random.random() * second / third) * third + first}')
    # print(len(first_entry.get().split(".")))
    # print(len(first_entry.get().split(".")) == 2 and first_entry.get().split(".")[0].isdigit()
    #       and first_entry.get().split(".")[1].isdigit())
    int_positive_first = first.replace(" ", "").isdigit()
    int_negative_first = first.replace(" ", "").find("-") == 0 and first.count("-") == 1\
                   and first.replace("-", "").replace(" ", "").isdigit()
    float_positive_first = first.replace(" ", "").replace(",", ".").count(".") == 1\
                     and first.replace(",", ".").replace(".", "").replace(" ", "").isdigit()
    float_negative_first = first.replace(",", ".").count("-") == 1\
                           and first.replace(" ", "").replace(",", ".").count(".") == 1\
                           and first.replace(" ", "").replace(",", ".").replace(".", "").replace("-", "").isdigit()
    first_number = int_positive_first or int_negative_first or float_negative_first or float_positive_first

    int_positive_second = second.replace(" ", "").isdigit()
    int_negative_second = second.replace(" ", "").find("-") == 0 and second.count("-") == 1\
                   and second.replace("-", "").replace(" ", "").isdigit()
    float_positive_second = second.replace(" ", "").replace(",", ".").count(".") == 1\
                     and second.replace(",", ".").replace(".", "").replace(" ", "").isdigit()
    float_negative_second = second.replace(",", ".").count("-") == 1\
                            and second.replace(" ", "").replace(",", ".").count(".") == 1\
                            and second.replace(" ", "").replace(",", ".").replace(".", "").replace("-", "").isdigit()
    second_number = int_positive_second or int_negative_second or float_negative_second or float_positive_second

    int_positive_third = third.replace(" ", "").isdigit()

    float_positive_third = third.replace(" ", "").replace(",", ".").count(".") == 1\
                     and third.replace(",", ".").replace(".", "").replace(" ", "").isdigit()
    third_number = int_positive_third or float_positive_third

    if first_number and second_number and third_number and float(third) != 0:
        label.config(text=f'Result:{(int(random.random() * (float(second) - float(first)) / float(third) + 1)) * float(third) + float(first)}')
        # print(random.random() * (float(second) - float(first) + 1) + float(first))
    else:
        label.config(text="print another number")


root = Tk()
frame = LabelFrame(text="Number generator")
frame.pack(side=LEFT)
Label(frame, text="from:").pack(side=LEFT)
first_entry = Entry(frame)
first_entry.pack(side=LEFT)
Label(frame, text="to:").pack(side=LEFT)
second_entry = Entry(frame)
second_entry.pack(side=LEFT)
Label(frame, text="step:").pack(side=LEFT)
step_entry = Entry(frame)
step_entry.pack(side=LEFT)
Button(frame, text="Generate number", command=generate_number).pack(side=LEFT)
label = Label(frame, text="Result:")
label.pack(side=LEFT)

root.mainloop()

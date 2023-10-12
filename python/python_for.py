# array = [10, 40, 20, 30]
# for element in array:
#     print(element + 2)


# for char in 'any string':
#     print(char)


# line = 'any string'
# for char in line:
#     print(char)


# words = ['any', 'string', 8]
# for word in words:
#     print(word)


# line = 'В ключевого слова for используется переменная'
# # print(line)
# # print(line.split())
# for word in line.split('о'):
#     print(word)

# from tkinter import *
# # from tkinter.ttk import *
#
# root = Tk()
#
# line = 'В ключевого слова for используется переменная'
# for word in line.split():
#     # print(word)
#     label = Label(text=word, fg='black')
#     label.pack()
# root.mainloop()


# array = [10, 40, 20, 30]
# i = 0
# for element in array:
#     array[i] = element + 2
#     i += 1
#     print(i, element)
# print(array)


# i = 0
# while i < len(array):
#     array[i] = array[i] + 2     # или array += 2
#     i = i + 1                   # или i += 1
#
# print(array)


# print(range(5))
# print(list(range(10)))


# for i in range(8):
#     print('8')


# for i in range(len(array)):
#     array[i] += 2
# print(array)


# import random
# numbers = []
# for i in range(5):
#     numbers.insert(0, random.randrange(-20, 20, 3))
# print(numbers)


# for i in range(7):
#     print(i)

# numbers = range(15)
# print(list(numbers))
# print(numbers[0])
# print(numbers[1])
# print(numbers[2])
# print(numbers[3])
# for number in numbers:
#     print(number + 1)


# print(list(range(2)))
# print(list(range(2, 9)))
# print(list(range(-10, 1)))
# print(list(range(-10, 1, 5)))
# print(list(range(10, -10, -1)))


# print(list(range(0, 101, 17)))


# numbers = [8, 7, -9, 4, -5]
# i = 1
# for number in numbers:
#     if number < 0:
#         print("negative number:", number)
#         print("number:", i)
#         i += 1


# how many even and odd numbers
# numbers = [9, 6, 1, -9, -1]
# for number in numbers:
#     if number % 2 == 0:
#         print("Четное")
#     else:
#         print("Нечетное")
#         i += 1


# total = 100
# for a in range(5):
#     n = int(input())
#     total = total - n
#     print(total)
# print("Осталось", total)


# import random
# for i in range(10):
#     number = random.randint(-5, 5)
#     print(number, end=" ")


# for i in range(15):
#     if i >= 1:
#         n = 2 ** i
#         print(n, end=" ")


# import random
#
# numbers = []
#
# for i in range(1000):
#     number = random.randint(-2, 2)
#     if numbers.count(number) == 0:
#         numbers.append(number)
#         # print(i, numbers)
#     if len(numbers) == 5:
#         break
# print(*numbers)


# element_answers = ['yes', 'no', 'maybe', 'ok', 'what']
# for i in elements_answers:
#     print(i)
# print(element_answers)
# print(enumerate(element_answers))
# print(list(enumerate(element_answers)))
# new_array = [
#     (0, 'yes'),
#     (1, 'no'),
#     (2, 'maybe'),
#     (3, 'ok'),
#     (4, 'what')
# ]
# for i in new_array:
#     print(i[0], i[1])

# second_array = list(enumerate(element_answers))
# for i in second_array:
#     print(i[0], i[1])

# for i in enumerate(element_answers):
#     print(i[0], i[1])

# for pair in enumerate(element_answers):
#     print(pair, pair[0], pair[1])

# for index, text in enumerate(element_answers):
#     print(index, text)

button_texts = [
    ["MC", "MR", "MS", "M+", "M-"],
    ["<-", "CE", "C", '±', '√'],
    [7, 8, 9, "/", "%"],
    [4, 5, 6, "*", "1/x"],
    [1, 2, 3, "-", '='],
    [0, "", '.', "+", ""]
]
# for index, text in enumerate(button_texts):
#     print(index, text)

for index, (b1, b2, b3, b4, b5) in enumerate(button_texts):
    print(index, b1, b2, b3, b4, b5)


# a = True
# print(type(a))      # в консоли выведеться следующее: <class 'bool'>
# b = False
# print(type(b))      # в консоли выведеться следующее: <class 'bool'>


# a = "100"
# print(type(a))
# a = 100
# print(type(a))
# a = 100.5
# print(type(a))
# a = True
# print(type(a))


# print(int(True))    # 1
# print(int(False))   # 0
# print(True + False)


# print(bool(3.4))    # True
# print(bool(-150))   # True
# print(bool(0))      # False
# print(bool(' '))    # True
# print(bool(''))     # False


# a = 25
# b = 5
# print(a + b > 14)   # True
# print(a < 14 - b)   # False
# print(a <= b + 5)   # True
# print(a != b)       # True
# print(a == b)       # False
# c = a == b
# print(c)   # False
# print(a, b, c)      # 10, 5, False


# a = 25
# b = -18
# c = '25'
# print(a + b > 19)   # False
# print(a < 14 - b)   # True
# print(a <= b + 40)  # False
# print(a != b)       # True
# print(c == c)       # True
# c = a == b          # False
# print(c)


# user_name = input("What year did you born?: ")
# print(int(user_name) > 0)


# user_year = float(input("What year is it?: "))
# print(2020 == user_year)


# x = 9
# y =16
# print(y < 15 and x > 8)
# print(y < 15 or x > 8)
# print(not y < 15)


# x = 2
# y = 5
# print(y < 15 and x > 1)
# print(y < 16 and x > 9)
# print(y < 15 or x > 1)
# print(y < 4 or x > 9)


# name_1 = "Vasya"
# name_2 = "Petya"
# city_1 = "Saint-Petesburg"
# city_2 = "New York"
# print(name_1 < name_2)
# print(city_1 < city_2)
# print(name_1 < city_1)
# print(city_2 > name_1)
# print(city_2 == name_2)


# b = 0
# a = 50
# n = 980
# if n < 100:
#     b = n + a
# print(b)


# product_1 = 50
# product_2 = 49
# if product_1 + product_2 > 99 :
#     print("99 рублей не достаточно")
# else:
#     print("Чек оплачен")

# a = 0
# if a:
#     a = 1
# print(a)


# a = 5 > 0
# if a:
#     print(a)


# a = 1
# b = 2
# if a > 0 and a < b:
#     print(b - a)


# if 0 < a < b:
#     print(b - a)


# massage = input("Enter the your login: ")
# if massage:
#     print('OK')


# massage = float(input("Enter the your number: "))
# if massage > 0:
#     print(1)
# if massage < 0:
#     print(-1)


# massage = float(input("What time is it? "))
# if 11 >= massage >= 4:
#     print("Good morning!")
# if 16 >= massage >= 12:
#     print("Good afternoon!")
# if 23 >= massage >= 17:
#     print("Good everning!")
# if 23 <= massage <= 24:
#     print("Good night!")
# if 0 <= massage <= 3:
#     print("Good night!")
# if 25 < massage < 0:
#     print("Eror")


# number_1 = float(input("Enter the first number: "))
# number_2 = float(input("Enter the second number: "))
# print(number_1 > number_2)


# number_1 = float(input("What day of month is it? "))
# print(31 >= number_1 >= 1)


# number_1 = float(input("What month did you born? "))
# print(12 >= number_1 >= 1)


# massage = input("Какое сейчас время года? ")
# if "лето" == massage or "Лето" == massage or massage == "ЛЕТО":
#     print("Нужно надеть футболку с шортами ")
# elif "осень" == massage:
#     print("Нужно надеть ветровку")
# elif "зима" == massage:
#     print("Нужно надеть теплые вещи")
# elif "весна" == massage:
#     print("нужно надеть ветровку")


# massage = input("Какое сейчас время года? ")
# print(massage)
# print(massage.capitalize())
# print(massage.lower())
# print(massage.upper())
# if "лето" == massage or "Лето" == massage or massage == "ЛЕТО":
#     print("Нужно надеть футболку с шортами ")
# elif "Осень" == massage.capitalize():
#     print("Нужно надеть ветровку")
# elif "зима" == massage.lower():
#     print("Нужно надеть теплые вещи")
# elif "ВЕСНА" == massage.upper():
#     print("нужно надеть ветровку")


# print("ПК: - Купи шубу!")
# massage = input("ВЫ: - ")
# if not massage:
#     print("ПК: - Все молчат, а ты купи шубу!")
# else:
#     print(f'ПК: - Все говорят: "{massage}", а ты купи шубу!')
#
# massage = input("ВЫ: - ")
# if not massage:
#     print("ПК: - Все молчат, а ты купи шубу!")
# else:
#     print(f'ПК: - Все говорят: "{massage}", а ты купи шубу!')
#
# massage = input("ВЫ: - ")
# if not massage:
#     print("ПК: - Все молчат, а ты купи шубу!")
# else:
#     print(f'ПК: - Все говорят: "{massage}", а ты купи шубу!')
#
# massage = input("ВЫ: - ")
# if not massage:
#     print("ПК: - Все молчат, а ты купи шубу!")
# else:
#     print(f'ПК: - Все говорят: "{massage}", а ты купи шубу!')
#
# massage = input("ВЫ: - ")
# if not massage:
#     print("ПК: - Все молчат, а ты купи шубу!")
# else:
#     print(f'ПК: - Все говорят: "{massage}", а ты купи шубу!')


word_1 = "1"
# print(word_1 > "0")
# print(word_1 < "10")
# print(word_1 < "+9999999")
# print(word_1 < "c")
# print(word_1 < "8c")
# print(word_1 == "0" or word_1 == "1" or word_1 == "2" or word_1 == "3" or word_1 == "4" or word_1 == "5" or word_1 == "6" or word_1 == "7" or word_1 == "8" or word_1 == "9")
# print("0" <= word_1 <= "9")
# print("a" <= word_1 <= "z")
# print("а" <= word_1 <= "я" or "А" <= word_1 <= "Я")
print(word_1.isnumeric())
print(word_1.isalpha())
print(word_1.isspace())
print(word_1.isnumeric())



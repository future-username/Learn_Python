# import matplotlib.pyplot as plt
# import numpy as np
#
# fig, ax = plt.subplots()
# x = [1, 2, 3, 4, 5]
# y = [25, 32, 34, 20, 25]
# # ax.plot(x, y)
# # ax.scatter(x, y)
# # ax.bar(x, y)
# ax.pie(x, y)
# plt.xlabel('Ось х')  # Подпись для оси х
# plt.ylabel('Ось y')  # Подпись для оси y
# plt.title('Первый график')  # Название
# plt.show()


import matplotlib.pyplot as plt
#
# дни = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
# температура = [10, 12, 14, 13, 15, 17, 16]
#
# plt.plot(дни, температура)
# plt.xlabel('Дни недели')
# plt.ylabel('Температура (°C)')
# plt.title('Температура за неделю')
# plt.show()
#
# plt

fruits = ['Apples', 'Oranges', 'Bananas']
quantities = [10, 15, 7]

pie = plt.pie(quantities, labels=fruits, autopct='%1.1f%%', colors=['red', 'orange', 'yellow'], startangle=90, explode=[0, 0.1, 0])
print(pie[0][0])
plt.title('Percentage Distribution of Fruits in the Market')
plt.grid(True)
plt.show()
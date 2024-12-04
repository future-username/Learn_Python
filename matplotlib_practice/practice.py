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


# import matplotlib.pyplot as plt
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

# fruits = ['Apples', 'Oranges', 'Bananas']
# quantities = [10, 15, 7]
#
# pie = plt.pie(quantities, labels=fruits, autopct='%1.1f%%', colors=['red', 'orange', 'yellow'], startangle=90, explode=[0, 0.1, 0])
# print(pie[0][0])
# plt.title('Percentage Distribution of Fruits in the Market')
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt
# import random
#
# data = []
# numbers = [random.randint(0, 100) for _ in range(1000)]
# print(numbers)
# plt.hist(numbers, bins=5, color='blue', edgecolor='black')
# plt.title("Гистограмма")
# plt.xlabel("Значения")
# plt.ylabel("Частота")
# plt.show()


# import matplotlib.pyplot as plt
#
#
# x = [1, 2, 3, 4, 5]
# y1 = [1, 4, 9, 16, 25]
# y2 = [1, 8, 27, 64, 125]
#
# plt.subplot(2, 1, 1)  # Первый график (2 строки, 1 столбец, 1-й график)
# plt.plot(x, y1, 'r-')
# plt.title("График 1")
#
# # plt.subplot(2, 1, 2)  # Второй график
# plt.plot(x, y2, 'b-')
# plt.title("График 2")
#
# # plt.tight_layout()  # Устранение наложения
# plt.show()


# import tkinter as tk
# from matplotlib.figure import Figure
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# import numpy as np
#
# # Создаем окно Tkinter
# root = tk.Tk()
# root.title("Гистограмма в Tkinter")
#
# # Создаем фигуру и ось
# fig = Figure(figsize=(5, 4), dpi=100)
# ax = fig.add_subplot(111)
#
# # Генерируем данные для гистограммы
# data = np.random.randn(1000)
#
# # Строим гистограмму
# ax.hist(data, bins=30, density=True)
#
# # Создаем канву для отображения графика
# canvas = FigureCanvasTkAgg(fig, master=root)
# canvas.draw()
#
# # Размещаем канву в окне
# canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
#
#
# # Запускаем цикл событий Tkinter
# root.mainloop()

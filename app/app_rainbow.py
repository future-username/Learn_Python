# from tkinter import *
#
#
# def print_red():
#     color_name.config(text="red", fg="red")
#     color_code.delete(0, END)
#     color_code.insert(0, "#ff0000")
#     color_code.config(bg="red")
#
#
# def print_orange():
#     color_name.config(text="Orange", fg="orange")
#     color_code.delete(0, END)
#     color_code.insert(0, "#ff7d00")
#     color_code.config(bg="orange")
#
#
# def print_yellow():
#     color_name.config(text="yellow", fg="yellow")
#     color_code.delete(0, END)
#     color_code.insert(0, "#ffff00")
#     color_code.config(bg="yellow")
#
#
# def print_green():
#     color_name.config(text="green", fg="green")
#     color_code.delete(0, END)
#     color_code.insert(0, "#00ff00")
#     color_code.config(bg="green")
#
#
# def print_lightblue():
#     color_name.config(text="lightblue", fg="lightblue")
#     color_code.delete(0, END)
#     color_code.insert(0, "#007dff")
#     color_code.config(bg="lightblue")
#
#
# def print_blue():
#     color_name.config(text="blue", fg="blue")
#     color_code.delete(0, END)
#     color_code.insert(0, "#0000ff")
#     color_code.config(bg="blue")
#
#
# def print_purple():
#     color_name.config(text="purple", fg="purple")
#     color_code.delete(0, END)
#     color_code.insert(0, "#7d00ff")
#     color_code.config(bg="purple")
#
#
# root = Tk()
#
#
# root.title('Colors')
# color_name = Label(text="Color name")
# color_name.pack()
# color_code = Entry(justify=CENTER)
# color_code.insert(0, "Color code")
# color_code.pack()
# button_red = Button(root, text='1', bg="red", command=print_red)
# button_red.pack(fill=X)
# button_orange = Button(root, text='2', bg="orange", command=print_orange)
# button_orange.pack(fill=X)
# button_yellow = Button(root, text='3', bg="yellow", command=print_yellow)
# button_yellow.pack(fill=X)
# button_green = Button(root, text='4', bg="green", command=print_green)
# button_green.pack(fill=X)
# button_lightblue = Button(root, text='5', bg="lightblue", command=print_lightblue)
# button_lightblue.pack(fill=X)
# button_blue = Button(root, text='6', bg="blue", command=print_blue)
# button_blue.pack(fill=X)
# button_purple = Button(root, text='7', bg="purple", command=print_purple)
# button_purple.pack(fill=X)
# root.mainloop()


# from tkinter import *
#
# root = Tk()
#
#
# root.title('Colors')
# color_name = Label(text="Color name")
# color_name.pack()
# color_code = Entry(justify=CENTER)
# color_code.insert(0, "Color code")
# color_code.pack()
#
# button_colors = ["red", "orange", "yellow", "green", "lightblue", "blue", "purple"]
# n = 0
# while n < 7:
#     n += 1
#     button_red = Button(root, text=n, bg=button_colors[n-1])
#     button_red.pack(fill=X)
# root.mainloop()


# from tkinter import *
#
# root = Tk()
#
#
# root.title('Colors')
# color_name = Label(text="Color name")
# color_name.pack()
# color_code = Entry(justify=CENTER)
# color_code.insert(0, "Color code")
# color_code.pack()
#
# button_colors = ["red", "orange", "yellow", "green", "lightblue", "blue", "purple"]
# i = 1
# for color in button_colors:
#     button_red = Button(root, text=i, highlightbackground=color)
#     button_red.pack(fill=X)
#     i += 1
# root.mainloop()


# from tkinter import *
#
# root = Tk()
# root.title('Colors')
#
# color_name = Label(text="Color name")
# color_name.pack()
# color_code = Entry(justify=CENTER)
# color_code.insert(0, "Color code")
# color_code.pack()
#
# button_colors = ["red", "orange", "yellow", "green", "lightblue", "blue", "purple"]
#
# for index, color in enumerate(button_colors):
#     button_red = Button(root, text=index, highlightbackground=color)
#     button_red.pack(fill=X)
# root.mainloop()


# from tkinter import *
#
# colors = {
#     "red": "#ff0000",
#     "orange": "#ff7d00",
#     "yellow": "#ffff00",
#     "green": "#00ff00",
#     "lightblue": "#007dff",
#     "blue": "#0000ff",
#     "purple": "#7d00ff"
# }
#
#
# def print_color(color_name: str, color_code: str) -> None:
#     label_color.config(text=color_name, fg=color_name)
#     entry_color.delete(0, END)
#     entry_color.insert(0, color_code)
#     entry_color.config(bg=color_name)
#
#
# root = Tk()
#
# root.title('Colors')
# label_color = Label(text="Color name")
# label_color.pack()
# entry_color = Entry(justify=CENTER)
# entry_color.insert(0, "Color code")
# entry_color.pack()
#
# for index, color in enumerate(colors):
#     button = Button(root, text=index, bg=color,
#                     command=lambda value=color, code=colors[color]: print_color(value, code))
#     button.pack(fill=X)
#
# root.mainloop()


from tkinter import *

colors = {
    "red": "#ff0000",
    "orange": "#ff7d00",
    "yellow": "#ffff00",
    "green": "#00ff00",
    "lightblue": "#007dff",
    "blue": "#0000ff",
    "purple": "#7d00ff"
}


class Errors:
    """Класс для обработки ошибок типов данных."""
    @staticmethod
    def type_error(value, type_value):
        """Вызывает TypeError, если тип значения не соответствует ожидаемому.
    
        Args:
            value: Значение для проверки.
            type_value: Ожидаемый тип.
    
        Raises:
            TypeError: Если тип value не совпадает с type_value.
        """
        if not isinstance(value, type_value):
            raise TypeError(f'Значение {value} должно быть типа {type_value}')


class Model:
    """Модель данных приложения. Хранит словарь цветов."""
    def __init__(self, colors_data: dict):
        """Инициализирует модель.
    
        Args:
            colors_data (dict): Словарь с данными цветов (имя: код).
    
        Raises:
            TypeError: Если colors_data не является словарем.
        """
        Errors.type_error(colors_data, dict)
        self.__colors_data = colors_data

    @property
    def colors_data(self):
        """Возвращает словарь цветов."""
        return self.__colors_data


class ButtonColor(Button):
    """Класс кнопки, отображающей информацию о цвете."""
    def __init__(self, parent: Tk, label: Label, entry: Entry, color_code: str, color_name: str):
        """Инициализирует кнопку цвета.
    
        Args:
            parent (Tk): Родительский виджет.
            label (Label): Метка для отображения имени цвета.
            entry (Entry): Поле для отображения кода цвета.
            color_code (str): Код цвета.
            color_name (str): Имя цвета.
    
        Raises:
            TypeError: Если типы аргументов не соответствуют ожидаемым.
        """
        Errors.type_error(parent, Tk)
        Errors.type_error(label, Label)
        Errors.type_error(entry, Entry)
        Errors.type_error(color_code, str)
        Errors.type_error(color_name, str)

        super().__init__(parent, text=color_name, bg=color_code)
        self.__label = label
        self.__entry = entry
        self.__color_name = color_name
        self.color_code = color_code

    def show_color(self):
        """Отображает имя и код цвета в соответствующих виджетах."""
        self.__label.config(text=self.__color_name)
        self.__entry.delete(0, END)
        self.__entry.insert(0, self.color_code)
        self.__entry.config(bg=self.color_code)


class Controller:
    """Контроллер приложения. Связывает модель и представление."""
    def __init__(self, model: Model, view: View):
        """Инициализирует контроллер.
    
        Args:
            model (Model): Экземпляр модели.
            view (View): Экземпляр представления.
    
        Raises:
            TypeError: Если типы аргументов не соответствуют ожидаемым.
        """
        Errors.type_error(model, Model)
        Errors.type_error(view, View)
        self.__model = model
        self.__view = view
        self.__view.set_controller(self)
        self.__view.create_buttons(self.__model.colors_data)

    @staticmethod
    def print_color(button: ButtonColor):
        """Обрабатывает нажатие кнопки цвета.
    
        Args:
            button (ButtonColor): Нажатая кнопка.
    
        Raises:
            TypeError: Если button не является экземпляром ButtonColor.
        """
        Errors.type_error(button, ButtonColor)
        button.show_color()


class View:
    """Представление приложения. Отвечает за пользовательский интерфейс."""
    def __init__(self, parent: Tk, label_name: str):
        """Инициализирует представление.
    
        Args:
            parent (Tk): Родительский виджет (главное окно).
            label_name (str): Текст для метки имени цвета.
    
        Raises:
            TypeError: Если типы аргументов не соответствуют ожидаемым.
        """
        Errors.type_error(parent, Tk)
        Errors.type_error(label_name, str)
        self.__parent = parent
        self.__label_name = label_name
        self.__controller = None

        self.__label = Label(self.__parent, text=self.__label_name)
        self.__label.pack()
        self.__entry = Entry(self.__parent, justify=CENTER)
        self.__entry.insert(0, "Color code")
        self.__entry.pack()

    def create_buttons(self, dict_colors: dict):
        """Создает кнопки для каждого цвета.
    
        Args:
            dict_colors (dict): Словарь цветов (имя: код).
    
        Raises:
            TypeError: Если dict_colors не является словарем.
        """
        Errors.type_error(dict_colors, dict)
        for color_name, color_code in dict_colors.items():
            button = ButtonColor(self.__parent, self.__label, self.__entry, color_code, color_name)
            button.config(command=lambda b=button: self.__set_color(b))
            button.pack(fill=X)

    def set_controller(self, controller: Controller):
        """Устанавливает контроллер для представления.
    
        Args:
            controller (Controller): Экземпляр контроллера.
    
        Raises:
            TypeError: Если controller не является экземпляром Controller.
        """
        Errors.type_error(controller, Controller)
        self.__controller = controller

    def __set_color(self, button: ButtonColor):
        """Вызывает метод контроллера для обработки нажатия кнопки.
    
        Args:
            button (ButtonColor): Нажатая кнопка.
    
        Raises:
            TypeError: Если button не является экземпляром ButtonColor.
        """
        Errors.type_error(button, ButtonColor)
        if self.__controller:
            self.__controller.print_color(button)


class App:
    """Главный класс приложения."""
    def __init__(self, colors_data: dict):
        """Инициализирует приложение.
    
        Args:
            colors_data (dict): Словарь с данными цветов.
    
        Raises:
            TypeError: Если colors_data не является словарем.
        """
        Errors.type_error(colors_data, dict)
        self.__root = Tk()
        self.__root.title('Colors')
        self.__model = Model(colors_data)
        self.__view = View(self.__root, 'Color name')
        self.__controller = Controller(self.__model, self.__view)

    def run(self):
        """Запускает главный цикл приложения Tkinter."""
        self.__root.mainloop()


if __name__ == '__main__':
    App().mainloop()

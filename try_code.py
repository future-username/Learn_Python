# class Square:
#     def __init__(self, side):
#         self.side = side
#
#     def calculate_area(self):
#         return self.side * self.side
#
#
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_area(self):
#         return self.width * self.height
#
#
# class RectangleAdapter:
#     def __init__(self, rectangle):
#         self.rectangle = rectangle
#
#     def calculate_area(self):
#         return self.rectangle.get_area()
#
#
# # Пример использования
# square = Square(5)
# rectangle = Rectangle(4, 6)
#
# adapter = RectangleAdapter(rectangle)
# area = adapter.calculate_area()
#
# print("Area:", area)


# class SingletonClass(object):
#     instance = None
#
#     def __new__(cls):
#         if not cls.instance:
#             cls.instance = super(SingletonClass, cls).__new__(cls)
#         return cls.instance
#
#
# # Usage:
# s1 = SingletonClass()
# s2 = SingletonClass()
#
# print(s1 is s2)  # Output: True


class Button:
    def __init__(self, text):
        self.text = text

    def click(self):
        print(f"Button '{self.text}' was clicked")


class UIFactory:
    def create_button(self, button_type, text):
        if button_type == "Windows":
            return WindowsButton(text)
        elif button_type == "Linux":
            return LinuxButton(text)
        else:
            raise ValueError("Invalid button type")


class WindowsButton(Button):
    def __init__(self, text):
        super().__init__(text)
        # Дополнительная инициализация для кнопки Windows


class LinuxButton(Button):
    def __init__(self, text):
        super().__init__(text)
        # Дополнительная инициализация для кнопки Linux


factory = UIFactory()

windows_button = factory.create_button("Windows", "Click me")
windows_button.click()  # Выведется: Button 'Click me' was clicked

linux_button = factory.create_button("Linux", "Press here")
linux_button.click()  # Выведется: Button 'Press here' was clicked

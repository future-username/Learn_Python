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
    @staticmethod
    def type_error(value, type_value):
        raise TypeError(f'{value} this is not {type_value}')


class Model:
    def __init__(self, colors_data):
        self.colors_data = colors_data

    @property
    def colors_data(self):
        return self.__colors_data

    @colors_data.setter
    def colors_data(self, value):
        if isinstance(value, dict):
            self.__colors_data = value
        else:
            raise TypeError(f'{value} this is not dict')


class ButtonColor(Button):
    def __init__(self, parent: Tk, label: Label, entry: Entry, color_code: str, color_name: str, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.__label = label if isinstance(label, Label) else Errors.type_error(label, Label)
        self.__entry = entry if isinstance(entry, Entry) else Errors.type_error(entry, Entry)
        self.__color_name = color_name if isinstance(color_name, str) else Errors.type_error(color_name, str)

        if (isinstance(color_code, str) and color_code.startswith('#') and len(color_code) == 7
                and color_code[1:].isalnum()):
            self.color_code = color_code
        else:
            raise TypeError(f'{color_code} this is not {color_code}')

        self.config(text=self.__color_name, fg=self.__color_name)

    def show_color(self) -> None:
        self.__label.config(text=self.__color_name, fg=self.__color_name)
        self.__entry.delete(0, END)
        self.__entry.insert(0, self.color_code)
        self.__entry.config(bg=self.__color_name)


class Controller:
    def __init__(self, model, view):
        self.__model = model
        self.__view = view
        self.__view.create_buttons(self.__model.colors_data)

    @staticmethod
    def print_color(button: ButtonColor):
        """
        print_color
        :return:
        """
        try:
            button.show_color()
        except ValueError as error:
            print(error)


class View:
    def __init__(self, parent: Tk, label_name: str):
        self.__label_name = label_name if isinstance(label_name, str) else Errors.type_error(label_name, str)
        self.__parent = parent if isinstance(parent, Tk) else Errors.type_error(parent, Tk)
        self.__controller = None

    def create_buttons(self, dict_colors):
        label_color = Label(text=self.__label_name)
        label_color.pack()
        entry_color = Entry(justify=CENTER)
        entry_color.insert(0, "Color code")
        entry_color.pack()

        for color_name, color_code in dict_colors.items():
            button_color = ButtonColor(self.__parent, label_color, entry_color, color_code, color_name)
            button_color.config(command=lambda b=button_color: self.__set_color(b))
            button_color.pack(fill=X)

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.__controller = controller

    def __set_color(self, button: ButtonColor):
        """
        Handle button click event
        :return:
        """
        if self.__controller:
            self.__controller.print_color(button)


class App:
    def __init__(self):
        super().__init__()
        self.__root = Tk()
        self.__root.title('Colors')

        model = Model(colors)

        # create a view and place it on the root window
        view = View(self.__root, label_name='Colors')

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)

    def mainloop(self):
        self.__root.mainloop()


if __name__ == '__main__':
    App().mainloop()

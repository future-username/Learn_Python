import re
import tkinter as tk
from tkinter import ttk


class ModelEmail:
    def __init__(self):
        self.email = ''

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        """
        Validate the email
        :param value:
        :return:
        """
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern, value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')

    def save(self):
        """
        Save the email into a file
        :return:
        """
        with open('emails.txt', 'a') as f:
            f.write(self.email + '\n')


class ModelPhoneNumber:
    def __init__(self):
        self.__value = None
        self.name = 'phone number'

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, number: str):
        """
        Validate the number
        :param number:
        :return:
        """
        temp = number.strip().replace(' ', '')
        signs = ['(', ')', '-']
        for char in signs:
            temp = temp.replace(char, '')

        if temp.isdigit() and len(temp) == 9:
            self.__value = number
        else:
            raise ValueError(f'Invalid {self.name}: {number}')

    def save(self):
        """
        Save the number into a file
        :return:
        """
        with open('numbers.txt', 'a') as f:
            f.write(self.value + '\n')


class ModelLogin:
    def __init__(self):
        self.__value = None
        self.name = 'login'

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, number: str):
        """
        Validate the number
        :param number:
        :return:
        """
        temp = number.strip().replace(' ', '').replace('.', '').replace(',', '')

        if len(temp) >= 3:
            self.__value = number.title()
        else:
            raise ValueError(f'Invalid {self.name}: {number}')

    def save(self):
        """
        Save the number into a file
        :return:
        """
        with open('numbers.txt', 'a') as f:
            f.write(self.value + '\n')


class Model:
    def __init__(self, name, complete):
        self.__complete = complete
        self.__value = None
        self.name = name

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, number: str):
        """
        Validate the number
        :param number:
        :return:
        """
        # temp = number.strip().replace(' ', '').replace('.', '').replace(',', '')

        temp = self.__complete(number.strip())

        if temp:
            self.__value = number.title()
        else:
            raise ValueError(f'Invalid {self.name}: {number}')

    def save(self):
        """
        Save the number into a file
        :return:
        """
        with open('numbers.txt', 'a') as f:
            f.write(self.value + '\n')


class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create widgets
        # label
        self.label = ttk.Label(self, text='Email:')
        self.label.grid(row=1, column=0)

        # email entry
        self.email_var = tk.StringVar()
        self.email_entry = ttk.Entry(self, textvariable=self.email_var, width=30)
        self.email_entry.grid(row=1, column=1, sticky=tk.NSEW)

        # save button
        self.save_button = ttk.Button(self, text='Save', command=self.save_button_clicked)
        self.save_button.grid(row=1, column=3, padx=10)

        # message
        self.message_label = ttk.Label(self, text='', foreground='red')
        self.message_label.grid(row=2, column=1, sticky=tk.W)

        # set the controller
        self.controller = None

    def set_controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def save_button_clicked(self):
        """
        Handle button click event
        :return:
        """
        if self.controller:
            self.controller.save(self.email_var.get())

    def show_error(self, message):
        """
        Show an error message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'red'
        self.message_label.after(3000, self.hide_message)
        self.email_entry['foreground'] = 'red'

    def show_success(self, message):
        """
        Show a success message
        :param message:
        :return:
        """
        self.message_label['text'] = message
        self.message_label['foreground'] = 'green'
        self.message_label.after(3000, self.hide_message)

        # reset the form
        self.email_entry['foreground'] = 'black'
        self.email_var.set('')

    def hide_message(self):
        """
        Hide the message
        :return:
        """
        self.message_label['text'] = ''


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def save(self, email):
        """
        Save the email
        :param email:
        :return:
        """
        try:
            # save the model
            self.model.value = email
            self.model.save()

            # show a success message
            self.view.show_success(f'The {self.model.name} {email} saved!')

        except ValueError as error:
            # show an error message
            self.view.show_error(error)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter MVC Demo')

        # create a model
        # model = ModelEmail()
        # model = ModelPhoneNumber()
        # model = Model(lambda x: x.replace(' ', '').replace('.', '').replace(',', ''))
        # model = Model(lambda x: len(x.replace(' ', '').replace('.', '').replace(',', '')) >= 3)
        command = lambda x: re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', x)
        model = Model('email', command)

        # create a view and place it on the root window
        view = View(self)
        view.grid(row=0, column=0, padx=10, pady=10)

        # create a controller
        controller = Controller(model, view)

        # set the controller to view
        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()

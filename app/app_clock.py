from tkinter import *
from time import strftime as time

cities = {
    "Quebec": -5,
    "London": 0,
    "Moscow": +3,
    "Tokyo": +9
}


class Errors:
    @staticmethod
    def type_error(value, type_value):
        raise TypeError(f'{value} this is not {type_value}')


class Clock:
    def __init__(self, parent: Tk, city_name: str, time_zone: int, current_zone=3):
        """
        Clock constructor
        :param parent:
        :param city_name:
        :param time_zone:
        :param current_zone:
        """
        self.parent = parent
        self.city_name = city_name
        self.time_zone = time_zone
        self.current_zone = current_zone

        frame = LabelFrame(master=self.parent, text=city_name)
        frame.pack(side=LEFT)
        self.__label = Label(frame, font=('times', 20, 'bold'), bg='green')
        self.__label.pack(fill=BOTH, expand=1)

    @property
    def parent(self) -> Tk:
        return self.__parent

    @parent.setter
    def parent(self, value: Tk):
        self.__parent = value if isinstance(value, Tk) else Errors.type_error(value, Tk)

    @property
    def city_name(self) -> Tk:
        return self.__city_name

    @city_name.setter
    def city_name(self, value: str):
        self.__city_name = value if isinstance(value, str) else Errors.type_error(value, str)

    @property
    def time_zone(self) -> int:
        return self.__time_zone

    @time_zone.setter
    def time_zone(self, value: int):
        self.__time_zone = value if isinstance(value, int) else Errors.type_error(value, int)

    @property
    def current_zone(self) -> int:
        return self.__current_zone

    @current_zone.setter
    def current_zone(self, value: int):
        self.__current_zone = value if isinstance(value, int) else Errors.type_error(value, int)

    def tick(self):
        time_hour = time('%H')
        time_minute_second = time('%M:%S')

        result_time = (24 + int(time_hour) + self.time_zone - self.current_zone) % 24

        self.__label.config(text=f"{result_time}:{time_minute_second}")
        self.__label.after(200, self.tick)


class App:
    def __init__(self):
        """
        Constructor
        """
        self.__root = Tk()
        for city in cities:
            Clock(self.__root, city, cities[city]).tick()

    def run(self):
        self.__root.mainloop()


if __name__ == '__main__':
    App().run()

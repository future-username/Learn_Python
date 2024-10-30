from abc import ABC, abstractmethod


class _Vehicle(ABC):
    """
    class Vehicle ...
    """
    @abstractmethod
    def __init__(self, make: str, model: str, price: float, year: int = 2000):
        """
        constructor Vehicle
        :param make: str - min length 3 chars
        :param model: str - min length 2 chars
        :param price: float - more than 0
        :param year: int - more than 1800, default 2000
        """
        raise NotImplementedError()

    @property
    @abstractmethod
    def model(self) -> str:
        """
        current model
        :return: model of Vehicle
        """
        raise NotImplementedError()

    @model.setter
    @abstractmethod
    def model(self, value: str):
        """
        set value min length 2 chars max 100 chars
        :param value: min length 2 chars
        :return: name model of Vehicle
        """
        raise NotImplementedError()

    @property
    @abstractmethod
    def year(self) -> int:
        """
        :return: made year
        """
        raise NotImplementedError()

    @year.setter
    @abstractmethod
    def year(self, year: int):
        """
        set made year
        :param year: made date
        """
        raise NotImplementedError()

    @property
    @abstractmethod
    def price(self) -> float:
        """
        :return: price Vehicle in dollars
        """
        raise NotImplementedError()

    @price.setter
    @abstractmethod
    def price(self, price: float):
        """
        set Vehicle price
        :param price: in dollars
        """
        raise NotImplementedError()


class Vehicle(_Vehicle):
    def __init__(self, make, model, price, year = 2000):
        self.__model = model
        self.__price = price
        self.__year = year

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value




# vehicle = _Vehicle("1","2",3,5)
# print(vehicle)
vehicle = Vehicle("1","2",3,5)
vehicle.set_model(1)
vehicle.get_model()
# vehicle.get_price()
# print(vehicle.__dir__())
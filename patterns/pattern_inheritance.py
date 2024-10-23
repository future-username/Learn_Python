from abc import ABC, abstractmethod


class _Vehicle(ABC):
    """
    class Vehicle ...
    """
    # pass
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

    @abstractmethod
    def get_model(self) -> str:
        """
        current model
        :return: model of Vehicle
        """
        raise NotImplementedError()

    @abstractmethod
    def set_model(self, value: str):
        """
        set value min length 2 chars max 100 chars
        :param value: min length 2 chars
        :return: name model of Vehicle
        """
        raise NotImplementedError()

    @property
    @abstractmethod
    def year(self) -> int:
        raise NotImplementedError()

    @year.setter
    @abstractmethod
    def year(self, year: int):
        raise NotImplementedError()

    @abstractmethod
    def get_price(self) -> float:
        raise NotImplementedError()

    @abstractmethod
    def set_price(self, price: float):
        raise NotImplementedError()


class Vehicle(_Vehicle):
    # pass
    def __init__(self, make, model, price, year = 2000):
        print()


    def get_model(self):
        pass

    def set_model(self, value):
        pass


# vehicle = _Vehicle("1","2",3,5)
# print(vehicle)
vehicle = Vehicle("1","2",3,5)
vehicle.set_model(1)
vehicle.get_model()
# vehicle.get_price()
# print(vehicle.__dir__())
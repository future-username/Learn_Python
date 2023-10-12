# class Box:
#     material = 'card'
#     amount = 0
#
#     def __init__(self):
#         self.width = 1
#         self._length = 2
#         self.__height = 3
#
#     def get_height(self):
#         return self.__height
#
#     def set_height(self, value: int):
#         self.__height = value if isinstance(value, int) else print('Error type')
#
#
# Box.material = 'wood'
# box_1 = Box()
# box_1.width = '-5'
# print(box_1.width)
# # box_1.set_height('-5')
# print(box_1.get_height())
# # print(box_1._length)
# # print(box_1.__height)
# # print(box_1.__height)
# # print(box_1._Box__height)


class Box:
    def __init__(self, width: int, length: int, height: int):
        self.__width = width
        self.length = length
        self.__height = None
        self.set_height(height)

    def get_height(self) -> int:
        return self.__height

    def set_height(self, value: int):
        if isinstance(value, int):
            self.__height = value
        else:
            raise ValueError('Error type')

    @property
    def width(self) -> int:
        return self.__width

    @property
    def length(self) -> int:
        return self._length

    @length.setter
    def length(self, value: int):
        if isinstance(value, int):
            self._length = value
        else:
            raise ValueError('Error type')


box = Box('1', 3, 4)
print(box.width)
# box.width = 0
print(box.__dict__)
box.length = 5
print(box.length)
print(box.__dict__)

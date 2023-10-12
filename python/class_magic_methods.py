# class Box:
#     def __init__(self):
#         self.size = 'M'
#
#     def __repr__(self):
#         return 'Box Medium'
#
#     def __str__(self) -> str:
#         """
#         str size
#         :return: str
#         """
#         return self.size
#
#     def __len__(self) -> int:
#         """
#         len size box (mm)
#         :return: int
#         """
#         return 205
#
#
# box = Box()
# print([box], box.__len__())
# print(len(box))
# print(box.__dict__)

# class MyArray:
#     def __init__(self):
#         self.values = [1, '2', 3]
#
#     def __repr__(self):
#         return str(self.values)
#
#     def __str__(self):
#         return ', '.join(str(i) for i in self.values)
#
#     def __len__(self):
#         return len(self.values)


# ar = MyArray()
# print(ar.__len__())
# print(len(ar))
# print([ar])
# print(ar.__repr__())
# print(ar.__str__())
# print(str(ar))
# print(type(ar))
# print(ar.__dict__)

# numbers = list((1, 2, 3))
# print(numbers)
# print(numbers.__repr__())
# print(numbers.__str__())
#
# number = int('4567')
# print(number)
# print(number.__repr__())
# print(number.__str__())
#
# number = dict({'v': '4567'})
# print(number)
# print(number.__repr__())
# print(number.__str__())


number = 5
print(number.__add__(5))
print(number + 5)
print(number.__sub__(7))
print(number - 7)
print(number.__bool__())
print(number.__eq__(4))
print(number == 4)
print(number.__ne__(5))

# array = [1, 5] + [3, 7]
# print([1, 5].__add__([3, 7]))
# print(array)


# class MyNumber:
#     def __init__(self, value: int):
#         self.value = value
#
#     # def __add__(self, other: int) -> int:
#     #     return self.value + other
#
#
# number = MyNumber(6)
# # print(value.__add__(3))
# print(number.value + 3)

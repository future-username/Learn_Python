# colors = ['yellow', 'blue', 'black', 'white']
# colors = ['yellow', 'blue', 'black', 'white'] * 500
# print(colors.__sizeof__())
# iter_colors = iter(colors)
# print(iter_colors.__sizeof__())
# print(next(iter_colors))
# print(next(iter_colors))
# print(next(iter_colors))
# print(next(iter_colors))
# # print(next(iter_colors))
# iter_colors = (_ for _ in colors)
# print(iter_colors)
# print(iter_colors.__sizeof__())
# print(next(iter_colors))
# print(next(iter_colors))
# print(next(iter_colors))
# print(next(iter_colors))


# def iter_values(values: list):
#     return (i for i in values)
#
#
# iter_colors = iter_values(colors)
# print(iter_colors)
# print(iter_colors.__sizeof__())
# print(next(iter_colors))


# def iter_values(values: list):
#     for value in values:
#         yield value.upper()
#
#
# iter_colors = iter_values(colors)
# print(iter_colors)
# print(iter_colors.__sizeof__())
# print(next(iter_colors))
# print(next(iter_colors))
# print(next(iter_colors))


# line = '''Python существует в нескольких разных версиях, с разными вариантами конфигурации в каждой операционной
#  системе. Это приложение пригодится вам в том случае, если описание из главы 1 не сработало или вы захотите установить
#   другую версию Python вместо той, которая поставлялась с вашей системой.
# #'''
#
# width = 50
#
#
# # def edit_width(value: str, w: int):
# #     result = ''
# #     for i, v in enumerate(value.replace('\n', '')):
# #         result += v
# #         if i % w == 0 and i != 0:
# #             result += '\n'
# #     return result
# #
# #
# # print(edit_width(line, width))
# # edit_width(line, width)
#
# def edit_width(value: str, w: int):
#     result = ''
#     for i, v in enumerate(value.replace('\n', '')):
#         result += v
#         if i % w == 0 and i != 0:
#             yield result
#             result = ''
#
#
# v = edit_width(line, width)
# print(next(v))
# print(next(v))
# print(next(v))
# print(next(v))


button_texts = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0],
    ["+", "-", "*", "/", "="]
]


def get_item(values: iter):
    for list_value in values:
        for value in list_value:
            yield value


items = get_item(iter(button_texts))
for item in items:
    print(item)

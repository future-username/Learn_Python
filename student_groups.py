"""
todo реализовать таблицу студентов с 5-10 студентами
Вариант 53.
Дано:
данные поступают из файла txt
Информация о группе студентов из N человек, где запись о студенте содержит следующие данные:

1) Фамилия, имя, (отчество необязательно) студента;
2) Число, месяц, год рождения;
3) Год поступления в институт;
4) Факультет (институт)
5) кафедра
6) Группа.
7) Номер зачетной книжки.
8) Пол
9) Названия предметов и оценки по каждому предмету в каждой
сессии, максимально 9 сессий и 10 предметов в каждом
семестре, которые могут быть разные.
Все данные должны быть форматными: даты, числа и т.д.
предметы:  ...todo
спецпредметы: ...todo

Найти:
Разбить группу на две части, с поиском среди лиц определенного пола:
1) сдавших все спец. предметы только на 4 и 5 'и только на 5';
2) сдавших спец. предметы на 3,4,5 'если есть хотя бы одна тройка'.
3) сдавших спец. предметы на 1,2 или не сданы не выводятся.
4) Отсортировать каждую часть по алфавиту по фамилии.
"""
from pprint import pprint

group = [
    ['Vasya', 'M', [3, 3]],
    ['dasya', 'W', [3, 4]],
    ['fasya', 'M', [4, 5]],
    ['gasya', 'W', [3, 5]],
    ['pasya', 'M', [5, 5]],
]
group_man, group_woman = [], []
group_man_mark, group_woman_mark = [], []

for student in group:
    for parram in student:
        if parram == 'M':
            group_man.append(student)
        elif parram == 'W':
            group_woman.append(student)

marks = [int(mark) for mark in input('Which marks of subjects do you need? (3,4,5/4,5):\t').split(',')]


def sort_marks(list_student: list, values: list) -> list:
    sorted_student = []
    for student in list_student:
        if min(values) in student[2] and student not in sorted_student:
            sorted_student.append(student)
    return sorted_student


i = sort_marks(group, marks)
# print(sort_marks(group, [3, 4, 5]))
pprint(sorted(i), width=30)

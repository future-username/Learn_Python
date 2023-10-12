line = 'Monday, Tuesday, Wednesday, Thursday, Friday'
days = line.split(", ")
new_line = ''
for day in days:
    new_line = f'{new_line}{day}'
    if days[-1] != day:
        new_line = f"{new_line}, "
print(new_line)
#
# print(', '.join(days))


# numbers = ['192', '168', '1', '15']
# print('.'.join(numbers))


# numbers = [192, 168, 1, 15]
# new_numbers = []
# for number in numbers:
#     # print(number)
#     new_numbers.append(str(number))
# print('.'.join(new_numbers))

# import random
# new_numbers = []
# for number in range(4):
#     new_numbers.append(str(random.randint(0, 255)))
# print('.'.join(new_numbers))


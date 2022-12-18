# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

# num1 = int(input('Введите число 1: '))
# num2 = int(input('Введите число 2: '))
# num3 = int(input('Введите число 3: '))
# num4 = int(input('Введите число 4: '))
# num5 = int(input('Введите число 5: '))
# max = num1
# if num2 > max:
#     max = num2
# if num3 > max:
#     max = num3
# if num4 > max:
#     max = num4
# if num5 > max:
#     max = num5
# print(max)

# def get_numbers(num):
#     list = []
#     max = 0
#     for i in range(num):
#         num = int(input('Введите число: '))
#         list.append(num)
#         if num > max:
#             max = num
#     return list, max

# my_list, num_max = get_numbers(5)
# print(my_list)
# print(num_max)

# max = 0

for i in range(5):
    num = int(input(f'Введите число {i + 1}: '))
    if num > max:
        max = num
print(max)

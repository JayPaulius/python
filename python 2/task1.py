# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

# num = int(input('ввведите число: '))
# list_1 = []
# for _ in range(num):
#     list_1.append(random.randrange(-10, 10))
# print(*list_1)

import random

num = int(input('ввведите число: '))
for _ in range(num):
    print(random.randrange(-10, 10), end=' ')
# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ]

import math

n = int(input('введите число: '))
list1 = [math.factorial(i) for i in range(1, n+1)] 
print(list1)



# num = int(input('введите число: '))
# list = []
# for i in range(1, num + 1):
#     list.append(math.factorial(i))
# print(list)
# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1 = int(input('Введите x1: '))
y1 = int(input('Введите y1: '))
x2 = int(input('Введите x2: '))
y2 = int(input('Введите y2: '))
f = lambda x, y: (x - y) ** 2
distance = round(float((f(x1, x2) + f(y1, y2)) ** 0.5), 2)
print(distance)



# import math
# x1 = int(input('Введите x1: '))
# y1 = int(input('Введите y1: '))
# x2 = int(input('Введите x2: '))
# y2 = int(input('Введите y2: '))
# distance = round(float(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)), 2)
# print(distance)
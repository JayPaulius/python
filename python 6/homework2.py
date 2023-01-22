# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
list1 = [random.randrange(10) for i in range(10)]
print(list1)
list1 = [el for i, el in enumerate(list1) if i % 2]
print(sum(list1))



# import random
# list1 = []
# sum = 0
# for _ in range(10):
#     list1.append(random.randrange(10))
# print(list1)
# for i in range(1, len(list1), 2):
#     sum += list1[i]
# print(sum)
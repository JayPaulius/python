# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random
list1 = []
sum = 0
for _ in range(10):
    list1.append(random.randrange(10))
print(list1)
for i in range(1, len(list1), 2):
    sum += list1[i]
print(sum)
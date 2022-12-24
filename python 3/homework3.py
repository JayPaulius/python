# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random 
list1 = []
for _ in range(5):
    list1.append(round(random.uniform(0, 10), 2))
min = round(list1[0] % 1, 2)
max = round(list1[0] % 1, 2)
for i in range(len(list1)):
    if list1[i] % 1 < min:
        min = round(list1[i] % 1, 2)
for i in range(len(list1)):
    if list1[i] % 1 > max:
        max = round(list1[i] % 1, 2)
diff = round(max - min, 2)
print(list1)
print(f'{max} - {min} = {diff}')
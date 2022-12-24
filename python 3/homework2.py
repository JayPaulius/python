# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random
list1 = []
list2 = []
for _ in range(5):
    list1.append(random.randrange(1, 10))
for i in range(len(list1) // 2 + len(list1) % 2):
    list2.append(list1[i] * list1[len(list1)-i-1])
print(list1)
print(list2)
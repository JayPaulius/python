# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности

import random
list1 = []
list2 = []
for i in range(10):
    list1.append(random.randrange(1, 10))
for i in range(10):
    if list1.count(list1[i]) == 1:
        list2.append(list1[i])
print('исходная последовательность:', list1, sep='\n')
if len(list2) > 0:
    print('неповторяющиеся элементы:', list2, sep='\n')
else:
    print('нет неповторяющихся элементов')
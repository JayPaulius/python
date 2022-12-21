# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import random
num = int(input('введите n: '))
list_1 = []
list_2 = []
prod = 1
for _ in range(num):
    list_1.append(random.choice([i for i in range(-num, num) if i not in [0]]))
f = open('file.txt')
for line in f:
    list_2.append(int(line))
for i in range(len(list_2)):
    prod *= (list_1[list_2[i]-1])
print(f'произведение чисел списка {list_1} на позициях', end=' ')
print(*list_2, sep=', ', end=' = ')
for i in range(len(list_2)):
    print(list_1[list_2[i]-1], end=' ')
    if i < len(list_2) - 1:
        print('* ', end='')
print(f'= {prod}')
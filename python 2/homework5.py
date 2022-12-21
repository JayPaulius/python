# Реализуйте алгоритм перемешивания списка.

import random
list = []
num = int(input('введите длину списка: '))
for i in range(num):
    list.append(int(input(f'введите значение элемента {i+1}: ')))
print('исходный список:')
print(list)
random.shuffle(list)
print('перемешанный список:')
print(list)
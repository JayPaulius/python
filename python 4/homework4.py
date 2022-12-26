# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('введите число: '))
polynom = ''
coeffs = ''
n = 0
for i in range(k, -1, -1):
    n = random.randrange(0, 10)
    coeffs += f'{n}, '
    if n != 0 and i != 0:
        polynom += f'{n} * x^{i} + '
    elif n != 0 and i == 0:
        polynom += f'{n} = 0'
    elif n == 0 and i == 0:
        polynom = polynom[:-2]
        polynom += '= 0'

print('список коэффициентов:')
print(coeffs[:-2])
print(f'многочлен степени {k}:')
print(polynom)

with open('file.txt', 'a') as data:
    data.write(f'{polynom} \n')
# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141

from math import pi
d = float(input('введите вещественное число <= 0.1: '))
while d > 0.1: d = float(input('введите вещественное число <= 0.1: '))
count = 0
while d < 1:
    count += 1
    d *= 10
print(round(pi, count))
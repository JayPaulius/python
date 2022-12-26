#  Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

a = int(input('введите a: '))
b = int(input('введите b: '))
c = int(input('введите c: '))
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b - d ** 0.5) / (2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    print(f'd > 0, x1 = {x1}, x2 = {x2}')
elif d == 0:
    x1 = -(b / (2 * a))
    print(f'd = 0, x1 = {x1}')
else:
    print('корней нет')
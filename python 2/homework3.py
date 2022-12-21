# Задайте список из n чисел последовательности (1 + 1 / n) ^ n и выведите на экран их сумму.

num = int(input('введите n: '))
list = []
for i in range(1, num+1):
    list.append(round( ( (1 + 1 / i) ** i), 2) )
print(list)
print(f'Сумма: {sum(list)}')
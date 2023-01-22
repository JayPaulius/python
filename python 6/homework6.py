# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Задайте список из n чисел последовательности (1 + 1 / n) ^ n и выведите на экран их сумму.

num = int(input('введите n: '))
list1 = [round(((1 + 1 / i) ** i), 2) for i in range(1, num+1)]
print(list1)
print(f'Сумма: {sum(list1)}')



# num = int(input('введите n: '))
# list = []
# for i in range(1, num+1):
#     list.append(round( ( (1 + 1 / i) ** i), 2) )
# print(list)
# print(f'Сумма: {sum(list)}')
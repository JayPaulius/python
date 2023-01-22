# Задача: предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6,782 -> 23
# - 0,56 -> 11

num = input('введите вещественное число: ')
list1 = list(map(int,(filter(lambda x: x.isdigit(), list(num)))))
print(sum(list1))



# num_1 = int(input('введите вещественное число: ').replace('.', ''))
# sum_1 = 0
# while num_1 > 0:
#     sum_1 += num_1 % 10
#     num_1 //= 10
# print(sum_1)
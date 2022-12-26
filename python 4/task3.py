#  Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

def null():
    num = int(input('Нельзя вводить 0. Введите любое натуральное число: '))
    return num

num1 = int(input('введите число 1: '))
while num1 == 0: num1 = null()
num2 = int(input('введите число 2: '))
while num2 == 0: num2 = null()
nok = 0

maxnum = max(num1, num2)
minnum = min(num1, num2)
for i in range(maxnum, num1 * num2 + 1, maxnum):
    if i % minnum == 0:
        nok = i
        break
print(nok)


# for i in range(1, num1 * num2 + 1):
#     if num1 * i % num2 == 0:
#         nok = num1 * i
#         break
#     elif num2 * i % num1 == 0:
#         nok = num2 * i
#         break
# print(nok)

# i = 1
# while nok == 0:
#     if num1 * i % num2 == 0:
#         nok = num1 * i
#     elif num2 * i % num1 == 0:
#         nok = num2 * i
#     i += 1
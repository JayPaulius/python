# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

str_1 = input('строка 1: ')
str_2 = input('строка 2: ')
if len(str_1) > len(str_2):
    print(str_1.count(str_2))
else:
    print(str_2.count(str_1))
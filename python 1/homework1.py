# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input('Введите цифру дня недели от 1 до 7: '))
while day < 1 or day > 7:
    day = int(input('Введите цифру дня недели от 1 до 7: '))
if day == 6 or day == 7:
    print('да')
else:
    print('нет')
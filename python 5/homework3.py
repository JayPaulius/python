# Создайте программу для игры в ""Крестики-нолики"".

import os

clear = lambda: os.system('cls')

def print_field(dict1):
    for i in range(1, 10, 3):
        print(dict1[i], dict1[i+1], dict1[i+2])

def player(playernum, dict1, char):
    cellnum = int(input(f'игрок {playernum} - {char}, введите номер ячейки: '))
    while dict1[cellnum] != str(cellnum):
        cellnum = int(input('ячейка занята, введите номер другой ячейки: '))
    dict1[cellnum] = char

def check(dict1, char):
    if (
        dict1[1] == dict1[2] == dict1[3] == char or 
        dict1[4] == dict1[5] == dict1[6] == char or
        dict1[7] == dict1[8] == dict1[9] == char or
        dict1[1] == dict1[4] == dict1[7] == char or
        dict1[2] == dict1[5] == dict1[8] == char or
        dict1[3] == dict1[6] == dict1[9] == char or
        dict1[1] == dict1[5] == dict1[9] == char or
        dict1[3] == dict1[5] == dict1[7] == char
        ):
        return True

def main():
    dict1 = {1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'}
    clear()
    print_field(dict1)
    for i in range(1, 10):
        if i % 2:
            player(1, dict1, 'x')
        else:
            player(2, dict1, 'o')
        clear()
        print_field(dict1)
        if check(dict1, 'x'):
            print('игрок 1 победил')
            break
        if check(dict1, 'o'):
            print('игрок 2 победил')
            break
        if i == 9:
            print('ничья')
main()
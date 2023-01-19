# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

def player(candies, max):
    while candies > 0:
        candy = int(input('игрок 1: '))
        while candy > max or candy < 0:
            print(f'за один ход можно забрать от 0 до {max} конфет')
            candy = int(input())
        candies -= candy
        if candies == 0:
            print('игрок 1 победил')
            break
        print(f'конфет осталось: {candies}')
        candy = int(input('игрок 2: '))
        while candy > max or candy < 0:
            print(f'за один ход можно забрать от 0 до {max} конфет')
            candy = int(input())
        candies -= candy
        if candies == 0:
            print('игрок 2 победил')
            break
        print(f'конфет осталось: {candies}')

def computer(candies, max):
    check_player = True
    player_candy = int(input('игрок: '))
    while player_candy > max or player_candy < 0:
        print(f'за один ход можно забрать от 0 до {max} конфет')
        player_candy = int(input())
    if player_candy == candies % (max + 1):
        candies -= player_candy
        print(f'конфет осталось: {candies}')
        bot_candy = random.randrange(1, max+1)
        print(f'бот: {bot_candy}')
        candies -= bot_candy
        print(f'конфет осталось: {candies}')
        while candies > 0:
            player_candy = int(input('игрок: '))
            while player_candy > max or player_candy < 0:
                print(f'за один ход можно забрать от 0 до {max} конфет')
                player_candy = int(input())
            if player_candy != candies % (max + 1) or candies < max and player_candy != candies:
                check_player = False
                break
            candies -= player_candy
            if candies == 0:
                print('игрок победил')
                break
            print(f'конфет осталось: {candies}')
            bot_candy = random.randrange(1, max+1)
            print(f'бот: {bot_candy}')
            candies -= bot_candy
            print(f'конфет осталось: {candies}')
    else:
        candies -= player_candy
        print(f'конфет осталось: {candies}')
        bot_candy = candies % (max + 1)
        print(f'бот: {bot_candy}')
        candies -= bot_candy
        print(f'конфет осталось: {candies}')
        while candies > 0:
            player_candy = int(input('игрок: '))
            while player_candy > max or player_candy < 0:
                print(f'за один ход можно забрать от 0 до {max} конфет')
                player_candy = int(input())
            candies -= player_candy
            print(f'конфет осталось: {candies}')
            bot_candy = candies % (max + 1)
            print(f'бот: {bot_candy}')
            candies -= bot_candy
            if candies == 0:
                print('бот победил')
                break
            print(f'конфет осталось: {candies}')
    if check_player == False:
        candies -= player_candy
        print(f'конфет осталось: {candies}')
        bot_candy = candies % (max + 1)
        print(f'бот: {bot_candy}')
        candies -= bot_candy
        if candies == 0:
            print('бот победил')
        else:
            print(f'конфет осталось: {candies}')
            while candies > 0:
                player_candy = int(input('игрок: '))
                while player_candy > max or player_candy < 0:
                    print(f'за один ход можно забрать от 0 до {max} конфет')
                    player_candy = int(input())
                candies -= player_candy
                print(f'конфет осталось: {candies}')
                bot_candy = candies % (max + 1)
                print(f'бот: {bot_candy}')
                candies -= bot_candy
                if candies == 0:
                    print('бот победил')
                    break
                print(f'конфет осталось: {candies}')

def main():
    mode = int(input('выберите режим игры: против человека - 1, против компьютера - 2: '))
    while mode > 2 or mode < 1:
        mode = int(input('выберите режим игры: против человека - 1, против компьютера - 2: '))
    candies = int(input('Введите общее количество конфет: '))
    max = int(input('Введите максимальное количество конфет за ход: '))
    if mode == 1:
        player(candies, max)
    else:
        computer(candies, max)

main()
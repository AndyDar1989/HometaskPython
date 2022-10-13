# 4. ** Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"
from random import randint


def candy_game(num: int, player_1, player_2):

    player = randint(1, 3)
    if player == 1:
        player = player_1
    else:
        player = player_2
    max_count = 28
    while True:
        count = int(input(f"{player}, enter count of candies: "))
        if 0 < count <= max_count and count <= num:
            num -= count
            if num == 0:
                print(f'Win {player}')
            else:
                print(f"candy's balance is {num}")
                if player == player_1:
                    player = player_2
                else:
                    player = player_1
        else:
            print('incorrect number')


#candy_game(121, 'aaa', 'bbb')


def bot_strategy(a, n, c):
    if n <= 28:
        bot_count = n
    elif n == a and n > 56:
        bot_count = 28
    elif 29 < n <= 56:
        bot_count = n-29
    elif n != a:
        bot_count = 29-c
    return bot_count


def candy_bot_game(amount: int, human, bot):
    num = amount
    count = 0
    player = randint(1, 3)
    if player == 1:
        player = human
    else:
        player = bot
    while True:
        if player == human:
            h_count = int(input(f"{human}, enter count of candies: "))
            count = h_count
        else:
            b_count = bot_strategy(amount, num, count)
            count = b_count
        if 0 < count <= 28 and count <= num:
            num -= count
            if num == 0:
                break
            elif num > 0:
                print(f"candy's balance is {num}")
                if player == human:
                    player = bot
                else:
                    player = human
        else:
            print('incorrect number')
    print(f'{player} Win!{chr(129395)}')


candy_bot_game(121, 'Person', 'Bot')

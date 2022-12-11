'''
2 Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем 28 конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Сколько конфет нужно взять первому игроку, чтобы забрать все
конфеты у своего конкурента?

a) Добавьте игру против бота
b) Подумайте как наделить бота "интеллектом"

'''
from random import randint
from random import choice
'''
Игра с другом
def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

def win():
    player1 = input("Введите имя первого игрока: ")
    player2 = input("Введите имя второго игрока: ")
    value = int(input("Введите количество конфет на столе: "))
    who_go = randint(0, 2)
    if who_go:
        print(f"Первый ходит {player1}")
    else:
        print(f"Первый ходит {player2}")
    counter1 = 0
    counter2 = 0
    while value > 28:
        if who_go:
            k = input_dat(player1)
            counter1 += k
            value -= k
            who_go = False
            print(f'{value} осталось конфет ')
        else:
            k = input_dat(player2)
            counter2 += k
            value -= k
            who_go = True
            print(f'{value} осталось конфет ')

    if who_go:
        print(f"Выиграл {player1}")
    else:
        print(f"Выиграл {player2}")
'''




# Игра с умным ботом
value = int(input("Enter count candies: "))

def ai(value):
    if value > 30:
        return randint(1, 28)
    elif value > 1  or value < 39:
        return randint(1 , 5)

    else:
        return 1

def game(value):
    player = input("Enter your name:  ")
    hm = [False , True]
    human = choice(hm)
    if human:
        print(f"The first {player} goes")
    else:
        print(f"The first bot goes")
    while value:
        if human:
            count = int(input(f"{player} enter count candies you want to take: "))
            if count > 28 or count < 1:
                count = int(input(f'Please enter a valid number(1 to 28): '))
            value -= count
            print('                                        ')
            print(f"{value} - candies it left")
            human = not human
            if value == 0:
                print(f"{player} Win")
                break
            else:
                continue
        else:
            vl_bot = ai(value)
            print(f"Bot goes now and choose {vl_bot} candies")
            value -= vl_bot
            print('                                        ')
            print(f"{value} - candies it left")
            human = not human
            if value == 0:
                print("Bot Win")
                break
            else:
                continue




game(value)







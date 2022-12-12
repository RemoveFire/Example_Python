import random
from random import randint, choice
from sympy import symbols
from math import prod


def RandomNaturalCoefficient(RandMin, RandMax):
    random_number = randint(RandMin, RandMax)
    return random_number


def KoeffForming(RandMin, RandMax, userNumber):
    koeff = [RandomNaturalCoefficient(RandMin, RandMax) for i in range(userNumber)] + [
        RandomNaturalCoefficient(RandMin, RandMax)]
    x = symbols('x')
    y = sum(map(prod, zip(koeff, [x ** i for i in range(userNumber + 1)])))
    return y


def input_check(enter):
    login = None
    check = True
    while check:
        try:
            login = float(input(f"{enter}"))
            check = False
        except ValueError:
            print("Неверный ввод!")
    return login


def U5Task1():
    print("Решение задачи №1: \n")

    with open('database\singular.txt', 'r', encoding='utf8') as file:
        text = file.readline().split()

    print(f'Исходный текст в файле: {text}')
    find = input("Введите что ищем в файле: ")
    new_text = ' '.join(word for word in text if word.find(find) == -1)
    print(f'Записываем в файл следующее содержимое: {new_text}')
    with open('database\singular_result.txt', 'w') as datafile:
        datafile.writelines(new_text)


def U5Task2():
    print("Решение задачи №2: \n")



    messages = ['Ваш ход брать конфеты', 'Возьмите конфеты',
                'сколько конфет берем?', 'берите еще', 'Ваш ход']
    max_number_move = 0

    def introduce_players():
        player1 = input('Первый игрок, представьтесь\n')
        player2 = 'BOT-ом'
        print(f'Очень приятно, сегодня Вы играете с искусственным интеллектом v 1.0  {player2}')
        return [player1, player2]

    def sweets_game(players):
        global max_number_move
        total_sweets = int(input('Введите cколько всего у нас конфет:\n'))
        max_number_move = int(input('Введите количество конфет, которое можно забрать за один ход:\n'))
        first = int(input(f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
        if first != 1:
            first = 0
        return [total_sweets, max_number_move, int(first)]

    # max_move = max_number_move
    # def check_player(num):  # проверка ввода игроком
    #     while True:
    #         try:
    #             num = int(num)
    #         except ValueError:
    #             num = input('Введите цифру. Попробуйте еще раз: ')
    #         else:
    #             if num > max_move or num < 1:
    #                 num = input(f'Ты хочешь взять {num}, столько брать нельзя, максимум {max_move}.'
    #                             'Попробуй ввести значения еще раз: ')
    #             else:
    #                 break
    #     return num
    def game_player_vs_smart_bot(sweets, players, messages):
        global max_number_move
        count = sweets[2]

        while sweets[0] > 0:
            if sweets[0] == (max_number_move and sweets[0] < max_number_move and sweets[0] > 1):
                move = sweets[0] - 1
                print(f'Я забираю {move}')

            elif not count % 2:
                move = random.randint(1, sweets[1])
                print(f'Я забираю {move}')
            else:
                print(f'{players[0]}, {choice(messages)}')
                move = int(input())
                if move > sweets[0] or move > sweets[1]:
                    print(
                        f'Можно взять не более {sweets[1]} конфет, у нас всего {sweets[0]} конфет')
                    chance = 2
                    while chance > 0:
                        if sweets[0] >= move <= sweets[1]:
                            break
                        print(f'Попробуйте ещё раз, у Вас {chance} попытки')
                        move = int(input())
                        chance -= 1
                    else:
                        return print(f'Попыток не осталось. Game over!')
            sweets[0] = sweets[0] - move
            if sweets[0] > 0:
                print(f'Осталось {sweets[0]} конфет')
            else:
                print('Все конфеты разобраны.')
            count += 1
        return players[not count % 2]

    players = introduce_players()
    sweets = sweets_game(players)

    winer = game_player_vs_smart_bot(sweets, players, messages)
    if not winer:
        print('У нас нет победителя.')
    else:
        print(f'Поздравляю! В этот раз победил {winer}! '
              f'Ему достаются все конфеты!')

def U5Task3():
    print("Решение задачи №3: \n")


def U5Task4():
    print("Решение задачи №4: \n")


def U5Task5():
    print("Решение задачи №5: \n")

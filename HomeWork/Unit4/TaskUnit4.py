from random import randint
from sympy import symbols
from math import prod
from datetime import datetime
import time


def RandomNaturalCoefficient(RandMin, RandMax):
    random_number = randint(RandMin, RandMax)
    # if abs(RandMax) > abs(RandMin):
    #     check = RandMin - 1
    #     max_abs = RandMax + 1
    # else:
    #     check = RandMax + 1
    #     max_abs = RandMin - 1
    # random_number = check
    # while random_number < RandMin or random_number > RandMax:
    #     temp_number = (float(time.time()) * float(datetime.now().time().microsecond)) / 1000000
    #     sign = -1
    #     if int(temp_number) % 2 != 0:
    #         sign = 1
    #     temp_number = temp_number - int(temp_number)
    #     random_number = abs(max_abs) * temp_number * sign
    #     random_number = int(random_number)
    #     time.sleep(0.000001)
    return random_number


def KoeffForming(RandMin, RandMax, userNumber):
    koeff = [RandomNaturalCoefficient(RandMin, RandMax) for i in range(userNumber)] + [RandomNaturalCoefficient(RandMin, RandMax)]
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


def U4Task1():
    print("Решение задачи №1: \n")
    import math
    x = math.pi
    n = input('Введите число d чтобы задать точность вывода числа π: ')
    count = 0

    n = n.replace('0.', '')

    for i in n:
        count += 1

    print(f'Число {x:.{count}f}')


def U4Task2():
    print("Решение задачи №2: \n")
    n = int(input('Введите число N: '))
    list = []
    a = n
    if n > 1:
        restart = True
        while restart:
            restart = False
            for i in range(2, n + 1):
                if n % i == 0:
                    list.append(i)
                    n = int(n / i)
                    restart = True
                    break

        print(f'Простые множители числа {a} - {list}')
    elif n == 1:
        print(f'Простые множители числа {a} - [{n}]')
    else:
        print(f'Вы ввели не правильное число')


def U4Task3():
    print("Решение задачи №3: \n")
    n = input('Введите последовательность чисел: ')
    list = (n)

    list_count = []
    for i in list:
        count = 0
        for k in list:
            if k == i:
                count += 1
        list_count.append(count)
    print("Промежуточный результат с выводом количества повторений: ", list_count)

    result = []
    for i in range(len(list_count)):
        if list_count[i] == 1:
            result.append(list[i])
    print("Вывод списка неповторяющихся элементов исходной последовательности: ", result)


def U4Task4():
    print("Решение задачи №4: \n")
    k = int(input('Задайте натуральную степень многочлена k: '))
    RangeMin, RangeMax = int(input('Введите диапазон рандомного числа ОТ, которого: ')), int(input('ДО, которого: '))

    with open('database\Data_Unit4Task4.txt', 'w') as data:
        data.write(f'Список коэффициентов многочлена в степени {k}:\n')
        for i in range(10):
            data.write(f'{KoeffForming(RangeMin, RangeMax, k):} = 0\n')
            print(KoeffForming(RangeMin, RangeMax, k), "= 0")


def U4Task5():
    print("Решение задачи №5: \n")
    k = int(input(f'Задайте натуральную степень многочлена для \033[33m{"первого файла k"}\033[0m: '))
    k2 = int(input(f'Задайте натуральную степень многочлена для \033[33m{"второго файла k"}\033[0m: '))
    RangeMin, RangeMax = int(input(f'Введите диапазон рандомного числа:\n'
                                   f'\033[33m{"ОТ, которого"}\033[0m: ')),\
                         int(input(f'\033[33m{"ДО, которого"}\033[0m: '))

    def Creat_file_name_first(k):
        with open('database\Data_Unit4_Task5_1.txt', 'w') as data:
            #data.write(f'Список коэффициентов многочлена в степени {k}:\n')
            for i in range(1):
                data.write(f'{KoeffForming(RangeMin, RangeMax, k):} = 0')
                #data.write('\n')
                #print('\nСоздан файл в директории \database\Data_Unit4Task5_1.txt,\n'
                #      f'который содержит: {KoeffForming(RangeMin, RangeMax, k)} = 0')

    def Creat_file_name_second(k2):
        with open('database\Data_Unit4_Task5_2.txt', 'w') as data:
            #data.write(f'Список коэффициентов многочлена в степени {k}:\n')
            for i in range(1):
                data.write(f'{KoeffForming(RangeMin, RangeMax, k2):} = 0')
                #data.write('\n')
                #print('\nСоздан файл в директории \database\Data_Unit4Task5_2.txt,\n'
                #      f'который содержит: {KoeffForming(RangeMin, RangeMax, k)} = 0')

    def String_to_list(str):
        str = str.replace('- ', '-')
        str = str.replace('+ ', '+')
        str = str.replace('+', '')
        str = str.replace(' = 0', '')
        #str = str.replace('\n', '')
        list = str.split(' ')
        return list

    def List_to_dict(list):
        new_dict = {}
        for i in list:
            if i.find('*x**') != -1:
                i = i.replace('*x**', ' ')
                temp_list = i.split(' ')
                new_dict[temp_list[1]] = int(temp_list[0])
            elif i.find('*x') != -1:
                i = i.replace('*x', ' ')
                temp_list = i.split(' ')
                new_dict['1'] = int(temp_list[0])
            else:
                new_dict['0'] = int(i)
        return new_dict

    Creat_file_name_first(k)
    Creat_file_name_second(k2)

    with open('database\Data_Unit4_Task5_1.txt', 'r') as file:
        text_first = file.read()

    with open('database\Data_Unit4_Task5_2.txt', 'r') as file:
        text_second = file.read()

    list_first = String_to_list(text_first)
    list_second = String_to_list(text_second)

    dict_first = List_to_dict(list_first)
    dict_second = List_to_dict(list_second)

    result_dict = {}
    for i in range(k and k2, -1, -1):
        if dict_first.get(str(i)) != None and dict_second.get(str(i)) != None:
            result_dict[str(i)] = dict_first[str(i)] + dict_second[str(i)]
        elif dict_first.get(str(i)) != None:
            result_dict[str(i)] = dict_first[str(i)]
        elif dict_second.get(str(i)) != None:
            result_dict[str(i)] = dict_second[str(i)]

    result_string = ''
    for i in result_dict:
        if i == '1':
            if result_dict[i] > 0:
                result_string += f'+ {result_dict[i]}x '
            elif result_dict[i] == 0:
                result_string += ''
            else:
                result_string += f'- {-(result_dict[i])}x '
        elif i != "0":
            if result_dict[i] > 0:
                result_string += f'+ {result_dict[i]}x**{i} '
            elif result_dict[i] == 0:
                result_string += ''
            else:
                result_string += f'- {-(result_dict[i])}x**{i} '
        else:
            if result_dict[i] > 0:
                result_string += f'+ {result_dict[i]} '
            elif result_dict[i] == 0:
                result_string += ''
            else:
                result_string += f'- {-(result_dict[i])} '

    result_string += '= 0'

    if result_string.find('+', 0, 1) != -1:
        result_string = result_string.replace('+', '', 1)

    with open('database/Result_Unit4_Task5.txt', 'w') as file:
        file.write(result_string)

    with open('database\Data_Unit4_Task5_1.txt') as file:
        print(f'\nСоздан файл в директории '
              f'\database\Data_Unit4_Task5_1.txt, \n'
              f'который содержит: {file.read()}')
    with open('database\Data_Unit4_Task5_2.txt') as file:
        print(f'\nСоздан файл в директории '
              f'\database\Data_Unit4_Task5_2.txt,\n'
              f'который содержит: {file.read()}')

    with open('database/Result_Unit4_Task5.txt') as file:
        print(f'\nФайл "Result_Unit4_Task5.txt" содержит результирующий многочлен:\n{file.read()}')

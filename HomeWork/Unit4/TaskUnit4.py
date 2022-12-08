from random import randint
from sympy import symbols
from math import prod


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
    print("Вывод список неповторяющихся элементов исходной последовательности: ", result)


def U4Task4():
    print("Решение задачи №4: \n")

    def RandomNaturalCoefficient():
        numb = randint(-100, 100)
        return numb

    userNumber = int(input('Задайте натуральную степень многочлена k: '))

    def KoeffForming(userNumber):
        koeff = [RandomNaturalCoefficient() for i in range(userNumber)] + [RandomNaturalCoefficient()]
        x = symbols('x')
        y = sum(map(prod, zip(koeff, [x ** i for i in range(userNumber + 1)])))
        return y

    with open('database\Data_Unit4Task4.txt', 'w') as data:
        data.write(f'Список коэффициентов многочлена в степени {userNumber}:\n')
        for i in range(10):
            data.write(f'{KoeffForming(userNumber)} = 0\n')
            print(KoeffForming(userNumber), "= 0")


def U4Task5():
    print("Решение задачи №5: \n")





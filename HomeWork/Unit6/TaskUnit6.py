from math import factorial
from math import prod
from random import randint
from sympy import symbols


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


def U6Task1():
    def task_1_1():
        print("Решение задачи №1.1: \n")
        print('''
                Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
    
                *Пример:*
                - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
                ''')
        n = int(input_check("Введите число: "))
        f = lambda x: ((x == 1) and 1) or x * factorial(x - 1)
        lst2 = list(f(i) for i in range(1, n + 1))
        print(f"\nНабор произведений чисел от 1 до {n}:  {lst2}")

    def task_1_2():
        print("Решение задачи №1.2: \n")
        print('''
                Задайте список из вещественных чисел. 
                Напишите программу, которая найдёт разницу между 
                максимальным и минимальным значением дробной части элементов.
                *Пример:*
                - [1.1, 1.2, 3.1, 5.1, 10.01] => 0.19
                ''')
        lst = list(map(float, input("Введите числа через пробел: ").split()))
        new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
        print(f"Разница между максимальным ({max(new_lst)}) и минимальным ({min(new_lst)})"
              f" значением дробной части элементов = ", max(new_lst) - min(new_lst))

    def task_1_3():
        print("Решение задачи №1.3: \n")

        def random_natural_coefficient(rand_min, rand_max):
            random_number = randint(rand_min, rand_max)
            return random_number

        def coefficient_forming(rand_min, rand_max, user_number):
            coefficient = [random_natural_coefficient(rand_min, rand_max) for i in range(user_number)] + [
            random_natural_coefficient(rand_min, rand_max)]
            x = symbols('x')
            y = sum(map(prod, zip(coefficient, [x ** i for i in range(user_number + 1)])))
            return y

        def Creat_file(k):
            with open('database/Unit6/Data_Unit6_Task_1_3.txt', 'w') as data:
                data.write(f'Список коэффициентов многочлена в степени {k}:\n')
                for i in range(10):
                    data.write(f'{coefficient_forming(min_range, max_range, k):} = 0')
                    data.write('\n')
                    print('\nСоздан файл в директории database/Unit6/Data_Unit6_Task_1_3.txt,\n'
                          f'который содержит: {coefficient_forming(min_range, max_range, k)} = 0')
        
        print('''
        Задана натуральная степень k. 
        Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
        многочлена и записать в файл многочлен степени k(до 6 степени).*

        *Пример:* 
        - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
        ''')
        coefficient_k = int(input('Задайте натуральную степень многочлена k: '))
        min_range, max_range = int(input('Введите диапазон рандомного числа ОТ, которого: ')), int(input('ДО, которого: '))
        Creat_file(coefficient_k)

    task_1_1()
    task_1_2()
    task_1_3()


def U6Task2():
    print("Решение задачи №2: \n")
    import re

    actions = {
        "^": lambda x, y: str(float(x) ** float(y)),
        "*": lambda x, y: str(float(x) * float(y)),
        "/": lambda x, y: str(float(x) / float(y)),
        "+": lambda x, y: str(float(x) + float(y)),
        "-": lambda x, y: str(float(x) - float(y))
    }

    priority_reg_exp = r"\((.+?)\)"
    action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"

    def my_eval(expresion: str) -> str:

        while (match := re.search(priority_reg_exp, expresion)):
            expresion: str = expresion.replace(match.group(0), my_eval(match.group(1)))

        for symbol, action in actions.items():
            while (match := re.search(action_reg_exp.format(symbol), expresion)):
                expresion: str = expresion.replace(match.group(0), action(*match.groups()))

        return expresion

    exp = input('Введите уравнение, к примеру такое - "(1 + 4) * (5 * (10 - 2)) / 5": ')
    print(f"Ответ: {my_eval(exp)} \nОтвет в другом формате: {eval(exp)}")

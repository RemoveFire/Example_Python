import sys
import Unit1


def Continuation():
    while True:
        yes = {'yes', 'ye', 'y', '', 'н', 'не', 'неы', 'да'}
        no = {'no', 'n', 'т', 'тщ', 'нет'}
        phrase = input("\n\tЕсли хотите продолжить введите 'yes' или введите 'no' чтобы выйти и завершить программу: "
                  "\n\tВведите выбранный вами вариант(y/n): ")
        if phrase in yes:
            print(f'\nВы выбрали: "{phrase}", поэтому работа программы Продолжится \n')
            NumberTask()
        elif phrase in no:
            print(f'\nВы выбрали: "{phrase}", поэтому работа программы Завершается\n')
            sys.exit()
        else:
            sys.stdout.write("\n\t\t!!!Пожалуйста введите 'yes' или 'no'!!!"
                             "\n\t\t\t\t(или 'y' или 'n') \n")
            Continuation()

#Вывод названия числа,для выбора задания
# Все это можно сделать иначе и правильней, но будет реализовано позже.
# Статьи где можно посмотреть как лучше сделать: https://code.activestate.com/recipes/410692/
# И еще: https://ru.stackoverflow.com/a/460208/530287
def NumberTask():
    while True:
        number = int(input('\nВыберите номер задания от 1 до 5 и напишите выбранный номер: '))
        if number == 1:
            print('''
            Выбрано задание №1
            Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

            Пример:
            - 6 -> да
            - 7 -> да
            - 1 -> нет''')
            Unit1.Task.Task1_func()
        elif number == 2:
            print('''
            Выбрано задание № 2
            Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
            ''')
            Unit1.Task.Task2_func()
        elif number == 3:
            print('''
            Выбрано задание № 3
            Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

            Пример:
            - x=34; y=-30 -> 4
            - x=2; y=4-> 1
            - x=-34; y=-30 -> 3
            ''')
            Unit1.Task.Task3_func()
        elif number == 4:
            print('''
            Выбрано задание № 4
            Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
            ''')
            Unit1.Task.Task4_func()
        elif number == 5:
            print('''
            Выбрано задание № 5
            Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

            Пример:
            - A (3,6); B (2,1) -> 5,09
            - A (7,-5); B (1,-1) -> 7,21
            ''')
            Unit1.Task.Task5_func()
            break
        else:
            sys.stdout.write('Выберите номер из предложенного списка')
    Continuation()

import os
import time
from math import factorial
import random


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


def WriteFile(number, roster):
    dir = 'database'
    if not os.path.exists(dir):
        os.mkdir(dir)
        print(os.getcwd())
        print("Directory ", dir, "is Created ")
        os.chdir(dir)
        print(os.getcwd())
    else:
        print("Directory ", dir, " already exists")
        print(os.getcwd())
        os.chdir(dir)
        print(os.getcwd())


    # os.path.exists(os.path.join(os.getcwd(), 'database', '.env'))

    #
    # if not os.path.isdir("database"):
    #     try:
    #         os.mkdir("database")
    #     except ValueError:
    #         os.chdir('database')
    #         print(os.getcwd())
    #         os.path.exists('.env')
    #     print(os.getcwd())
    for elem in range(-number, number):
        roster.append(str(elem))
    with open(r".env", "w") as file:
        for num in range(0, number):
            file.write(random.choice(roster))
            file.write("\n")


def U2Task1():
    print("Решение задачи №1: \n")
    total = 0
    for i in str(input_check("Введите число: ")):
        if i != i.isdigit():
            total += int(i)
    print(f"Сумма цифр = {total}")


def U2Task2():
    print("Решение задачи №2: \n")
    n = int(input_check("Введите число: "))
    f = lambda x: ((x == 1) and 1) or x * factorial(x - 1)
    list2 = list(f(i) for i in range(1, n + 1))
    print(f"\nНабор произведений чисел от 1 до {n}:  {list2}")


def U2Task3():
    print("Решение задачи №3: \n")
    n = int(input_check("Введите число: "))
    lst = {round((1 + 1 / i) ** i, 3) for i in range(1, n + 1)}
    dict = {i: round((1 + 1 / i) ** i, 3) for i in range(1, n + 1)}
    print(f'Последовательность: {lst}.\nТоже самое, но с представлением значения числа i: {dict}\nСумма: {round(sum(lst), 3)}')


def U2Task4():
    global num_line_start, num_line_end
    print("Решение задачи №4: \n")
    n = int(input_check("Задайте диапазон элементов N: "))
    l = []
    WriteFile(n, l)

    check = True
    while check:
        num_line_start = int(input_check("Введите позицию начала (номер строки) от 1 до N: "))
        num_line_end = int(input_check("Введите позицию конца (номер строки) от 1 до N: "))
        if 1 <= num_line_start < n and num_line_start < num_line_end <= n or n == 0:
            check = False
        else:
            print("\nНеверный ввод!")

    with open(r".env", "r") as file:
        mult_list = []
        for line in file:
            mult_list.append(int(line))
    mult_list = mult_list[ num_line_start - 1 : num_line_end : 1 ]

    print(f"Диапазон элементов с {num_line_start} по {num_line_end} строку: {mult_list}")
    mult = 1
    for num in mult_list:
        mult = mult * num
    print(f"Произведение элементов: {mult}")
    os.chdir('..')

def U2Task5():
    print("Решение задачи №5: \n")
    print("Случайное число от 0 до 9 на основе таймера: ", int(round(time.time() * 1000) % 10))

import time


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


def U2Task1():
    print("Решение задачи №1: \n")
    total = 0
    for i in str(input_check("Введите число: ")):
        if i != i.isdigit():
            total += int(i)
    print(f"Сумма цифр = {total}")


def U2Task2():
    print("Решение задачи №2: \n")
    from math import factorial

    N = int(input_check("Введите число: "))
    fun = lambda x: ((x == 1) and 1) or x * factorial(x - 1)
    list2 = list(fun(i) for i in range(1, N + 1))
    print(f"\nНабор произведений чисел от 1 до {N}:  {list2}")


def U2Task3():
    print("Решение задачи №3: \n")



def U2Task4():
    print("Решение задачи №4: \n")



def U2Task5():
    print("Решение задачи №5: \n")
    print("Случайное число от 0 до 9 на основе таймера: ", int(round(time.time() * 1000) % 10))

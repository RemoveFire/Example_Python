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


def U3Task1():
    print("Решение задачи №1: \n")
    lst = list(map(int, input("Введите числа через пробел(без запятых): ").split(",")))
    new = len(lst) // 2 + 1 if len(lst) % 2 != 0 else len(lst) // 2
    new_lst = [lst[i] * lst[len(lst) - i - 1] for i in range(new)]
    print(new_lst)


def U3Task2():
    print("Решение задачи №2: \n")
    lst = list(map(float, input("Введите числа через пробел: ").split()))
    new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
    print(f"Разница между максимальным ({max(new_lst)}) и минимальным ({min(new_lst)})"
          f" значением дробной части элементов = ", max(new_lst) - min(new_lst))


def U3Task3():
    print("Решение задачи №3: \n")
    num = n = int(input_check('Введите число для преобразования десятичного числа в двоичное: '))
    BinNum = []
    while num > 0:
        BinNum.append(str(num % 2))
        num //= 2
    print(f'Число {n} в двоичной форме выглядит так: ', ("".join(BinNum)[::-1]))


def U3Task4():

    print("Решение задачи №4: \n")
    num = int(input_check('Введите, сколько чисел нужно в ряду  Нефигабоначчи: '))

    LstNum = []
    LstFib = []
    num1, num2 = 0, 1
    fib1, fib2 = 0, 1
    for i in range(num):
        num1, num2 = num2, num1 + num2
        LstNum.append(num1)
        fib1, fib2 = fib2, fib1 - fib2
        LstFib.append(fib1)
    LstFib.reverse()
    print(f'Негафиббоначи: {[*LstFib, 0, *LstNum]}')

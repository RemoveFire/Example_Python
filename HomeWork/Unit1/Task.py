def Task1_func():
    print("\nРешение задачи №1: \n")
    day = int(input("Введите день недели от 1 до 7: "))
    if day <= 0 or day > 7:
        print(f"Вы ввели число {day}.\nВведите значение от 1 до 7!")
    elif day >= 1 and day <= 5:
        print(f"Вы ввели число: {day} и оно является - \tРабочим днем")
    elif day == 6:
        print(f"Вы ввели число: {day} и оно является -\tСубботой")
    elif day == 7:
        print(f"Вы ввели число: {day} и оно является -\tВоскресеньем")

def Task2_func():
    print("\nРешение задачи №2: \n")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if not (x or y or z) == (not x and not y and not z):
                    print(f'Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z истинно при X = {x}, Y = {y}, Z = {z}. ')

def Task3_func():
    print("\nРешение задачи №3: \n")
    x = int(input('Введите число X: '))
    y = int(input('Введите число Y: '))

    if x == 0 and y == 0:
        print('Ведите значения, которые не будут равны 0')
    elif x > 0 and y > 0:
        print(f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 1 ')
    elif x < 0 and y > 0:
        print(f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 2 ')
    elif x < 0 and y < 0:
        print(f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 3 ')
    elif x > 0 and y < 0:
        print(f'При координатах x = {x} и y = {y} ваша точка находится в плоскости 4 ')

def Task4_func():
    print("\nРешение задачи №4: \n")
    n = int(input('Введите номер четверти: '))
    if n < 1 or n > 4:
        print('Пожалуйста, повторите ввод')
    elif n == 1:
        print('x > 0 и y > 0')
    elif n == 2:
        print('x < 0 и y > 0')
    elif n == 3:
        print('x < 0 и y < 0')
    elif n == 4:
        print('x > 0 и y < 0')

def Task5_func():
    from math import sqrt
    print("\nРешение задачи №5: \n")
    print('Введите координату точки А:')
    x_A = float(input('X: '))
    y_A = float(input('Y: '))
    print("Введите координату точки B:")
    x_B = float(input('X: '))
    y_B = float(input('Y: '))

    # Решение по теореме Пифагора
    print('Расстояние  между A и B в 2D пространстве: ', round(sqrt((x_A - x_B) ** 2 + (y_A - y_B) ** 2), 2))

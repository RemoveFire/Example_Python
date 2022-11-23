def Task1_func():
    day = int(-1)
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

    print("\nЗдесь будет вторая задача ")

def Task3_func():

    print("\nЗдесь будет задание под номером 3")

def Task4_func():

    print("\nЗдесь будет задание под номером 4")

def Task5_func():

    print("\nЗдесь будет задание под номером 5")

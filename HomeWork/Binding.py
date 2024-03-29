# Файл в котором будут собираться в кучу все функции из разных юнитов
import sys
import Task

# Все это можно сделать иначе и правильней, но будет реализовано позже.
# Статьи где можно посмотреть как лучше сделать: https://code.activestate.com/recipes/410692/
# И еще: https://ru.stackoverflow.com/a/460208/530287


def Continuation():
    while True:
        yes = {'yes', 'ye', 'y', '', 'н', 'не', 'неы', 'да'}
        no = {'no', 'n', 'т', 'тщ', 'нет'}
        phrase = input("\n\tЕсли хотите продолжить введите 'yes' или введите 'no' чтобы выйти и завершить программу: "
                  "\n\tВведите выбранный вами вариант(y/n): ")
        if phrase in yes:
            print(f'\nВы выбрали: "{phrase}", поэтому работа программы Продолжится \n')
            UnitNumberTask()
        elif phrase in no:
            print(f'\nВы выбрали: "{phrase}", поэтому работа программы Завершается\n')
            sys.exit()
        else:
            sys.stdout.write("\n\t\t!!!Пожалуйста введите 'yes' или 'no'!!!"
                             "\n\t\t\t\t(или 'y' или 'n') \n")
            Continuation()


#Вывод названия числа,для выбора юнита и в дальнейшем задания
def UnitNumberTask():
    while True:
        try:
            NumberUnit = int(input('\nВыберите номер СЕМИНАРА от 1 до 6 или 11, 12 и напишите выбранный номер. '
                                   'Для раздела OOP введите - "13"! \n Ввод:  '))
        except ValueError:
            print('Неправильный ввод. Выберите UNIT из предложенного списка от 1 до 6! ')
            break
        if NumberUnit == 1:
            print('\nВы выбрали семинар №1')
            try:
                number = int(input('\nВыберите номер задания от 1 до 5 и напишите выбранный номер: '))
            except ValueError:
                print('Неправильный ввод. Выберите номер из предложенного списка от 1 до 5! ')
                continue
            Task.Unit_1_Task(number)
            Continuation()
        elif NumberUnit == 2:
            print('\nВы выбрали семинар №2')
            try:
                number = int(input('\nВыберите номер задания от 1 до 5 и напишите выбранный номер: '))
            except ValueError:
                print('Неправильный ввод. Выберите номер из предложенного списка от 1 до 5! ')
                break
            Task.Unit_2_Task(number)
            Continuation()
        elif NumberUnit == 3:
            print('\nВы выбрали семинар №3')
            try:
                number = int(input('\nВыберите номер задания от 1 до 4 и напишите выбранный номер: '))
            except ValueError:
                print('Неправильный ввод. Выберите номер из предложенного списка от 1 до 4! ')
                break
            Task.Unit_3_Task(number)
            Continuation()
        elif NumberUnit == 4:
            print('\nВы выбрали семинар №4')
            try:
                number = int(input('\nВыберите номер задания от 1 до 5 и напишите выбранный номер: '))
            except ValueError:
                print('Неправильный ввод. Выберите номер из предложенного списка от 1 до 5! ')
                break
            Task.Unit_4_Task(number)
            Continuation()
        elif NumberUnit == 5:
            print('\nВы выбрали семинар №5')
            try:
                number = int(input('\nВыберите номер задания от 1 до 4 и напишите выбранный номер: '))
            except ValueError:
                print('Неправильный ввод. Выберите номер из предложенного списка от 1 до 4! ')
                break
            Task.Unit_5_Task(number)
            Continuation()
        elif NumberUnit == 6:
            print('\nВы выбрали семинар №6')
            try:
                number = int(input('\nВыберите номер задания от 1 до 2 и напишите выбранный номер: '))
            except ValueError:
                print('Неправильный ввод. Выберите номер из предложенного списка от 1 до 2! ')
                break
            Task.Unit_6_Task(number)
            Continuation()
        elif NumberUnit == 11:
            print('\nВы выбрали семинар №11')
            try:
                number = int(input('\nВыберите номер задания от 1 до 1 и напишите выбранный номер: '))
            except ValueError:
                print('Неправильный ввод. Выберите номер из предложенного списка от 1 до 1! ')
                break
            Task.Unit_11_Task(number)
            Continuation()
        elif NumberUnit == 12:
            print('\nВы выбрали семинар №12')
            try:
                number = int(input('\nВыберите номер задания от 1 до 1 и напишите выбранный номер: '))
            except ValueError:
                print('Неправильный ввод. Выберите номер из предложенного списка от 1 до 1! ')
                break
            Task.Unit_12_Task(number)
            Continuation()
        elif NumberUnit == 13:
            print('\nВы выбрали семинар OOP №1')
            try:
                number = int(input('\nВыберите номер задания от 1 до 1 и напишите выбранный номер: '))
            except ValueError:
                print('Неправильный ввод. Выберите номер из предложенного списка от 1 до 1! ')
                break
            Task.oop_Unit_1_Task(number)
            Continuation()
        else:
            sys.stdout.write('Выберите UNIT из предложенного списка от 1 до 6 или 11, 12. Для раздела OOP введите - 13!'
                             '\n Ввод:  ')
    Continuation()


# Функция для записи текстового файла
def writing_file(user_string: str, user_file: str):
    with open(user_file, 'w', encoding='utf-8') as flow:
        flow.writelines(user_string)


# Функция для чтения файла
def read_file(user_file):
    with open(user_file, 'r', encoding='utf-8') as flow:
        result = flow.read()
        return result

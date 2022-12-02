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
            NumberUnit = int(input('\nВыберите номер СЕМИНАРА от 1 до 3 и напишите выбранный номер: '))
        except ValueError:
            print('Неправильный ввод. Выберите UNIT из предложенного списка от 1 до 3! ')
            break
        if NumberUnit == 1:
            print('\nВы выбрали семинар №1')
            try:
                number = int(input('\nВыберите номер задания от 1 до 5 и напишите выбранный номер: '))
            except ValueError:
                print('Неправильный ввод. Выберите номер из предложенного списка от 1 до 5! ')
                continue
            Task.Unit_1_Task(number)
        elif NumberUnit == 2:
            print('\nВы выбрали семинар №2')
            try:
                number = int(input('\nВыберите номер задания от 1 до 5 и напишите выбранный номер: '))
            except ValueError:
                print('Неправильный ввод. Выберите номер из предложенного списка от 1 до 5! ')
                break
            Task.Unit_2_Task(number)
        elif NumberUnit == 3:
            print('\nВы выбрали семинар №3')
            try:
                number = int(input('\nВыберите номер задания от 1 до 5 и напишите выбранный номер: '))
            except ValueError:
                print('Неправильный ввод. Выберите номер из предложенного списка от 1 до 5! ')
                break
            Task.Unit_3_Task(number)
        else:
            sys.stdout.write('Выберите UNIT из предложенного списка от 1 до 3! ')
    Continuation()

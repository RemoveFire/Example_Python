from multiprocessing.resource_sharer import stop
from unittest import result
import log
import mod
import view


def input_integer(enter):
    while True:
        try:
            a = int(input(enter))
            return a
        except:
            view.error_value()


def input_list(enter):
    a = input(enter)
    if '/0' in a:
        view.error_value_zerro()
    else:
        mod.result_list(a)


def input_ask(enter):
    while True:
        a = input(enter)
        if a in ['y', 'Y', 'да', 'Да', 'Yes', 'yes']:
            return a
        else:
            mod.init_first()


def input_operation(enter):
    while True:
        a = input(enter)
        if a in ['+', '-', '*', '/', '=']:
            return a
        else:
            view.error_value()


def operation():
    match (mod.ops):
        case '+':
            mod.total = mod.first + mod.second
        case '-':
            mod.total = mod.first - mod.second
        case '*':
            mod.total = mod.first * mod.second
        case '/':
            while mod.second == 0:
                print('На ноль делить нельзя!')
                mod.init_second()
            mod.total = int(mod.first / mod.second)

        case _:
            view.error_value()
            log.logger(f'{mod.first} {mod.ops} {mod.second} = {mod.total}')


def deleteElement(list, i):
    list.pop(i + 1)
    list.pop(i)


def operation2(list, i, oper):
    if list[i] == oper:
        list[i - 1] = mod.opSelect.get(oper)(int(list[i - 1]), int(list[i + 1]))
        deleteElement(list, i)
        return True


def totalOperation(list):
    list1 = list
    list = list.replace(' ', '').strip()
    list = list.replace('+', ' + ') \
        .replace('-', ' - ') \
        .replace('*', ' * ') \
        .replace('/', ' / ')
    list = list.split()

    while len(list) > 1:
        if '*' in list or '/' in list:
            for i in range(len(list)):
                if operation2(list, i, '*'): break
                if operation2(list, i, '/'): break

        elif '+' in list or '-' in list:
            for i in range(len(list)):
                if operation2(list, i, '+'): break
                if operation2(list, i, '-'): break

    view.print_total2(list)
    log.logger(f'{list1} = {list}')

    mod.stop = True

    return stop

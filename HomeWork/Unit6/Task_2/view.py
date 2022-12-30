import log
import mod


def error_value():
    log.logger('Ошибка ввода данных')
    return print('Ошибка ввода данных')

def error_value_zerro():
    log.logger('Ошибка ввода данных')
    return print('На ноль делить нельзя! Ошибка ввода данных')

def print_total():
    return print(f'Результат: {mod.total}')

def print_total2(list):
    return print(f'Результат: {list}')
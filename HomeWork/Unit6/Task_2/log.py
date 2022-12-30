import datetime

path = 'database/Unit6/log_unit6_task2.txt'
string = ''


def logger(info: str):
    global string
    datetime.datetime.now()
    string = str(datetime.datetime.now())[:-7] + ' | ' + info
    with open(path, 'a', encoding='UTF-8') as data:
        data.write(f'{string}\n')

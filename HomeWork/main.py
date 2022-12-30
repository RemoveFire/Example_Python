import Binding
import logging.config
import logging

from log.logger import logger_config

logging.config.dictConfig(logger_config)

logger_debug = logging.getLogger("main_debug_logger")
logger_info = logging.getLogger("info_logger")


def main():
    # Выполняем команду выполнения задач из урока 1

    print('''
    Знакомство с языком Python (семинары)\n
        Урок 1. Знакомство с Python:
            - включает в себя 5 задач
        Урок 2. Знакомство с Python. Продолжение:
            - включает в себя 5 задач (последняя задача под №5 является дополнительной)
        Урок 3. Данные, функции и модули в Python
            - включает в себя 4 задачи
        Урок 4. Данные, функции и модули в Python. Продолжение
            - включает в себя 5 задач(5-ая задача с дополнениями)
        Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension
            - включает в себя 4 задачи
        Урок 6. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension. Продолжение 
            - включает в себя 2 задачи''')
    logger_info.info("Запускаем Binding.UnitNumberTask()")

    Binding.UnitNumberTask()


# Запускаем главную функцию
logger_debug.debug("Start Program")
main()

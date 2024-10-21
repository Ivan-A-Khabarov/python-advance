# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

import logging

# Создаем объект журналирования
logger = logging.getLogger('example_app')

# Создаем поток журналирования для записи в файл
file_handler = logging.FileHandler('error_log.txt')
file_handler.setLevel(logging.ERROR)

# Форматируем сообщение об ошибке
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавляем поток к объекту журналирования
logger.addHandler(file_handler)

def divide_by_zero():
    try:
        result = 1 / 0
    except ZeroDivisionError as e:
        logger.exception("Ошибка деления на ноль")
        print("Ошибка деления на ноль!")
    else:
        return result

if __name__ == '__main__':
    divide_by_zero()
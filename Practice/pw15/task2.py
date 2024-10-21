# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.

import functools
import logging


class LoggingDecorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        arguments = {'args': args, 'kwargs': kwargs}
        result = self.func(*args, **kwargs)
        log_record = f'Аргументы: {arguments}, Результат: {result}'
        with open('log.txt', 'a',encoding='utf-8') as file:
            file.write(log_record + '\n')

        return result

def decorate(func):
    return LoggingDecorator(func)

@decorate
def my_function(arg1, arg2, keyword=None):
    print(f"Выполняется функция с аргументами: {arg1}, {arg2}, {keyword}")
    return f"Результат функции: {arg1} {arg2}"

my_function(1, 2, keyword='test')
# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.



import functools
import logging
from datetime import datetime


class LoggingDecorator:
    def __init__(self, level, func):
        self.level = level
        self.func = func

    def __call__(self, *args, **kwargs):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_record = f"{now}: {self.level}: {self.func.__name__}(*{args}, **{kwargs}) -> {self.func(*args, **kwargs)}"
        with open('log.txt', 'a') as file:
            file.write(log_record + '\n')
        return self.func(*args, **kwargs)


def decorate(level, func):
    return LoggingDecorator(level, func)


@decorate('INFO', print)
def my_function(arg1, arg2, keyword=None):
    print(f"Выполняется функция с аргументами: {arg1}, {arg2}, {keyword}")
    return f"Результат функции: {arg1} {arg2}"


my_function(1, 2, keyword='test')
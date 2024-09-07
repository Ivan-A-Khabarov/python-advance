# Если описание функции подразумевает больше подробностей, после первой строки
# документации оставляют одну пустую. Далее в несколько строк даётся всё
# необходимое описание. Закрывающие кавычки ставятся на отдельной строке, без
# текста.

def max_before_hundred(*args):
    """Return the maximum number not exceeding 100.
    :param args: tuple of int or float numbers
    :return: int or float number from the tuple args
    """
    m = float('-inf')
    for item in args:
        if m < item < 100:
            m = item
    return m
print(max_before_hundred(-42, 73, 256, 0))

help(max_before_hundred)

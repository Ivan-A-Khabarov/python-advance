# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

data = ['строка', 'число', True, False]

for i in range(1, len(data) + 1):
    print(f'{i}.')
    print(f'\tЗначение: {data[i - 1]}')
    print(f'\tАдрес в памяти: {id(data[i - 1])}')
    print(f'\tРазмер в памяти: {sys.getsizeof(data[i - 1])} bytes')
    print(f'\tХэш объекта: {hash(data[i - 1])}')

    if isinstance(data[i - 1], int):
        print(f'\tЦелое число: {data[i - 1]}')

    elif isinstance(data[i - 1], str):
        print(f'\tСтрока: {data[i - 1]}')

# Добавим повторяющиеся элементы
data.append('строка')
data.append(True)

for i in range(1, len(data) + 1):
    print(f'{i}.')
    print(f'\tЗначение: {data[i - 1]}')
    print(f'\tАдрес в памяти: {id(data[i - 1])}')
    print(f'\tРазмер в памяти: {sys.getsizeof(data[i - 1])} bytes')
    print(f'\tХэш объекта: {hash(data[i - 1])}')

    if isinstance(data[i - 1], int):
        print(f'\tЦелое число: {data[i - 1]}')

    elif isinstance(data[i - 1], str):
        print(f'\tСтрока: {data[i - 1]}')
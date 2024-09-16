# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.


import random
import string
import os


def create_random_files(extension, min_name_length=6, max_name_length=30,
                        min_bytes=256, max_bytes=4096, file_count=42):
    for _ in range(file_count):
        # Генерация случайного имени файла
        name_length = random.randint(min_name_length, max_name_length)
        random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_length))
        filename = f"{random_name}.{extension}"

        # Генерация случайного количества байт для записи в файл
        file_size = random.randint(min_bytes, max_bytes)
        random_data = os.urandom(file_size)  # Генерируем случайные байты

        # Запись данных в файл
        with open(filename, 'wb') as f:  # Открываем файл в бинарном режиме
            f.write(random_data)


# Пример использования:
create_random_files('txt', min_name_length=6, max_name_length=15, min_bytes=256, max_bytes=1024, file_count=10)


# Генерация случайного имени файла:
#
# Используем random.randint() для выбора случайной длины имени в диапазоне от min_name_length до max_name_length.
# random.choices(string.ascii_letters + string.digits, k=name_length) — генерирует строку случайной длины из букв (заглавных и строчных) и цифр.
# Генерация случайного размера файла:
#
# С помощью os.urandom() создаём случайную последовательность байтов нужного размера (от min_bytes до max_bytes).
# Запись данных в файл:
#
# Открываем файл на запись в бинарном режиме (wb), чтобы можно было записывать байты, и записываем в него сгенерированные данные.
# Количество файлов:
#
# Функция создаст столько файлов, сколько указано в параметре file_count (по умолчанию 42).
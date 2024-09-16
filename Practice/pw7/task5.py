# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.


import random
import string
import os


# Функция из предыдущей задачи, создающая файлы с заданным расширением
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


# Новая функция для создания файлов с разными расширениями
def create_files_with_different_extensions(file_specs, min_name_length=6, max_name_length=30,
                                           min_bytes=256, max_bytes=4096):
    """
    Параметры:
    - file_specs: словарь, где ключ - расширение, значение - количество файлов для этого расширения
    - min_name_length: минимальная длина имени файла (по умолчанию 6)
    - max_name_length: максимальная длина имени файла (по умолчанию 30)
    - min_bytes: минимальное количество случайных байт (по умолчанию 256)
    - max_bytes: максимальное количество случайных байт (по умолчанию 4096)
    """
    for extension, file_count in file_specs.items():
        create_random_files(extension, min_name_length, max_name_length, min_bytes, max_bytes, file_count)


# Пример использования:
file_specs = {
    'txt': 5,  # Создаём 5 текстовых файлов
    'bin': 3,  # Создаём 3 бинарных файла
    'csv': 2  # Создаём 2 файла формата CSV
}

create_files_with_different_extensions(file_specs, min_name_length=8, max_name_length=12, min_bytes=512, max_bytes=2048)

# Функция create_random_files():
# Это та же функция, что и в предыдущей задаче, которая создаёт файлы с заданным расширением, именами и случайными байтами.
# Функция create_files_with_different_extensions():
# Эта новая функция принимает словарь file_specs, где ключами являются расширения файлов (например, 'txt', 'bin'), а значениями — количество файлов, которое нужно сгенерировать для каждого расширения.
# Для каждого расширения вызывается функция create_random_files(), создающая нужное количество файлов с указанными параметрами (длина имени, размер файла).
# Пример использования:
# В примере мы создаём 5 файлов с расширением .txt, 3 файла с расширением .bin и 2 файла с расширением .csv. Размер имени файлов варьируется от 8 до 12 символов, а количество случайных байт в каждом файле — от 512 до 2048.

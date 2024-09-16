# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.


import random
import string
import os


# Функция для создания файлов с указанным расширением в указанную директорию
def create_random_files(directory, extension, min_name_length=6, max_name_length=30,
                        min_bytes=256, max_bytes=4096, file_count=42):
    # Проверка и создание директории, если она не существует
    if not os.path.exists(directory):
        os.makedirs(directory)

    for _ in range(file_count):
        while True:  # Цикл для генерации уникального имени
            name_length = random.randint(min_name_length, max_name_length)
            random_name = ''.join(random.choices(string.ascii_letters + string.digits, k=name_length))
            filename = f"{random_name}.{extension}"
            filepath = os.path.join(directory, filename)

            if not os.path.exists(filepath):  # Проверяем, существует ли файл с таким именем
                break  # Если не существует, выходим из цикла

        # Генерация случайного количества байт для записи в файл
        file_size = random.randint(min_bytes, max_bytes)
        random_data = os.urandom(file_size)  # Генерируем случайные байты

        # Запись данных в файл
        with open(filepath, 'wb') as f:  # Открываем файл в бинарном режиме
            f.write(random_data)


# Функция для создания файлов с разными расширениями в указанную директорию
def create_files_with_different_extensions(directory, file_specs, min_name_length=6, max_name_length=30,
                                           min_bytes=256, max_bytes=4096):
    """
    Параметры:
    - directory: директория, куда сохранять файлы
    - file_specs: словарь, где ключ - расширение, значение - количество файлов для этого расширения
    - min_name_length: минимальная длина имени файла (по умолчанию 6)
    - max_name_length: максимальная длина имени файла (по умолчанию 30)
    - min_bytes: минимальное количество случайных байт (по умолчанию 256)
    - max_bytes: максимальное количество случайных байт (по умолчанию 4096)
    """
    for extension, file_count in file_specs.items():
        create_random_files(directory, extension, min_name_length, max_name_length, min_bytes, max_bytes, file_count)


# Пример использования:
file_specs = {
    'txt': 5,  # Создаём 5 текстовых файлов
    'bin': 3,  # Создаём 3 бинарных файла
    'csv': 2  # Создаём 2 файла формата CSV
}

output_directory = "generated_files"  # Директория для сохранения файлов
create_files_with_different_extensions(output_directory, file_specs, min_name_length=8, max_name_length=12,
                                       min_bytes=512, max_bytes=2048)


# Проверка и создание директории:
#
# Функция проверяет наличие указанной директории с помощью os.path.exists(). Если директория не существует, она создаётся с помощью os.makedirs().
# Генерация уникальных имён:
#
# В цикле while генерируется случайное имя файла. Мы используем os.path.exists(filepath) для проверки, существует ли файл с таким именем в указанной директории. Если файл с таким именем уже существует, генерируется новое имя, и так продолжается, пока не будет найдено уникальное имя.
# Создание файлов с разными расширениями:
#
# Функция create_files_with_different_extensions() создаёт файлы с различными расширениями в заданной директории. Для каждого расширения она вызывает функцию create_random_files(), которая обрабатывает генерацию файлов и данных.
# Пример использования:
#
# Мы создаём директорию generated_files (если она не существует) и сохраняем в неё 5 файлов с расширением .txt, 3 файла с расширением .bin, и 2 файла с расширением .csv. Имена файлов варьируются от 8 до 12 символов, а размер данных — от 512 до 2048 байт.
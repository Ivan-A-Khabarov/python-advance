# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.


import os
import shutil

# Словарь с категориями и соответствующими расширениями
FILE_CATEGORIES = {
    'video': ['mp4', 'mkv', 'avi', 'mov'],
    'images': ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
    'documents': ['txt', 'doc', 'docx', 'pdf'],
    'audio': ['mp3', 'wav', 'flac', 'aac'],
    'archives': ['zip', 'rar', '7z', 'tar'],
}

def sort_files_by_category(source_directory):
    # Создаём директории для категорий, если их нет
    for category in FILE_CATEGORIES:
        category_dir = os.path.join(source_directory, category)
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)

    # Перебираем все файлы в исходной директории
    for filename in os.listdir(source_directory):
        filepath = os.path.join(source_directory, filename)

        # Пропускаем директории, обрабатываем только файлы
        if os.path.isfile(filepath):
            # Извлекаем расширение файла
            file_extension = filename.split('.')[-1].lower()

            # Проверяем, попадает ли расширение в одну из категорий
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    category_dir = os.path.join(source_directory, category)
                    shutil.move(filepath, os.path.join(category_dir, filename))  # Перемещаем файл в нужную категорию
                    moved = True
                    break  # Выходим из цикла, если файл уже перемещён

            # Если файл не подходит ни под одну категорию, он остаётся на месте
            if not moved:
                print(f"Файл '{filename}' не был отсортирован.")

# Пример использования:
source_directory = "source_folder"  # Папка, в которой нужно отсортировать файлы
sort_files_by_category(source_directory)


# Словарь FILE_CATEGORIES:
#
# Этот словарь определяет категории файлов и соответствующие им расширения. Можно добавлять или изменять категории по необходимости.
# Создание директорий для категорий:
#
# Для каждой категории создаётся папка в исходной директории, если она ещё не существует. Это делается через функцию os.makedirs().
# Обработка файлов:
#
# Мы используем os.listdir() для получения списка всех файлов в исходной директории.
# Проверяем, что объект является файлом с помощью os.path.isfile() (чтобы не пытаться перемещать директории).
# Извлекаем расширение файла и проверяем, попадает ли оно в одну из категорий. Если да, перемещаем файл в соответствующую папку с помощью shutil.move().
# Неотсортированные файлы:
#
# Если файл не подходит под ни одну категорию (его расширение не указано в словаре), он остаётся на месте.
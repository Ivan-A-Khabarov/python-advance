import os
from pathlib import Path


def rename_files(directory, extension, base_name, new_extension, start=None, end=None, final_suffix="", digits=2):
    # Получаем все файлы в указанном каталоге
    files = list(Path(directory).glob('*.' + extension))

    if not files:
        print("Нет файлов с расширением '{}' в директории '{}'".format(extension, directory))
        return

    # Проверяем наличие целевого каталога
    target_dir = Path(os.path.join(directory, 'result'))
    if not target_dir.exists():
        target_dir.mkdir(parents=True)

    counter = 0
    for file in files:
        # Извлекаем оригинальное имя файла без расширения
        original_base_name = file.stem

        # Формируем новое имя файла
        new_file_name = '{}{}{}.{}'.format(original_base_name[start:end], final_suffix,
                                           f"{{:0{digits}d}}".format(counter), new_extension)
        full_new_file_name = os.path.join(target_dir, new_file_name)

        # Проверяем, что новый файл не существует
        if os.path.exists(full_new_file_name):
            print("Файл '{}' уже существует. Переименование пропущено.".format(full_new_file_name))
            continue

        # Переименовываем файл
        os.rename(str(file), full_new_file_name)
        counter += 1

    print("Переименовано {} файлов.".format(counter))


# Пример использования
directory = '/tmp/input_files/'
extension = '.txt'
base_name = ''
new_extension = '.png'
final_suffix = '_renamed'
start = None
end = None
digits = 2

rename_files(directory, extension, base_name, new_extension, start, end, final_suffix, digits)

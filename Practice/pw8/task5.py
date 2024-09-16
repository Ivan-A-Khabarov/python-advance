import os
import json
import pickle


def save_json_to_pickle(directory, file_extension='.json'):
    """Считывает JSON файлы в директории и сохраняет их в виде одноименных pickle файлов."""

    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(file_extension):
                # Получаем полное имя файла
                full_filename = os.path.join(dirpath, filename)

                # Открываем JSON файл для чтения
                with open(full_filename, 'rb') as f:
                    data = json.load(f)

                # Создаем новый pickle файл с тем же именем
                new_filename = full_filename.replace(file_extension, '.pickle')
                with open(new_filename, 'wb') as w:
                    pickle.dump(data, w)


# Вызов функции
save_json_to_pickle('путь/к/папке')
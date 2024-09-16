# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка
# csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы
# функции

import json
import hashlib

def process_csv_to_json(csv_filename, json_filename):
    """Функция для чтения CSV, обработки данных и сохранения в JSON"""
    data = []

    # Открываем CSV-файл для чтения
    with open(csv_filename, 'r', encoding='utf-8') as csv_file:
        # Пропускаем первую строку с заголовками
        next(csv_file)

        # Чтение остальных строк
        for line in csv_file:
            # Убираем лишние пробелы и переносы строк
            line = line.strip()

            # Разбиваем строку на ID, Имя и Уровень доступа
            user_id, name, access_level = line.split(',')

            # Приведение идентификатора к 10 символам с ведущими нулями
            user_id = user_id.zfill(10)

            # Преобразуем имя: первая буква заглавная, остальные — строчные
            name = name.capitalize()

            # Хеширование (используем идентификатор и имя)
            hash_value = hashlib.md5(f'{user_id}{name}'.encode()).hexdigest()

            # Формируем словарь для текущей записи
            record = {
                "ID": user_id,
                "Имя": name,
                "Уровень доступа": int(access_level),
                "Хеш": hash_value
            }

            # Добавляем запись в список данных
            data.append(record)

    # Записываем данные в JSON-файл
    with open(json_filename, 'w', encoding='utf-8') as json_file:
        for record in data:
            json.dump(record, json_file, ensure_ascii=False)
            json_file.write('\n')  # Разделяем записи новой строкой

# Пример вызова функции:
process_csv_to_json('users.csv', 'users.json')

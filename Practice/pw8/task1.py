# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json


def convert_txt_to_json(txt_filename, json_filename):
    data = {}

    # Открываем файл с псевдо именами и числами
    with open(txt_filename, 'r', encoding='utf-8') as file:
        for line in file:
            # Убираем лишние пробелы и символы новой строки
            line = line.strip()

            # Разбиваем строку на имя и значение
            if line:
                pseudoname, number = line.split()

                # Имя с большой буквы
                pseudoname = pseudoname.capitalize()

                # Преобразуем строковое число в целое (или вещественное)
                number = float(number) if '.' in number else int(number)

                # Добавляем в словарь
                data[pseudoname] = number

    # Записываем данные в формате JSON в новый файл
    with open(json_filename, 'w', encoding='utf-8') as json_file:
        # Выводим данные с отступами для лучшей читаемости
        json.dump(data, json_file, ensure_ascii=False, indent=4)


# Пример вызова функции:
if __name__ == '__main__':
    convert_txt_to_json('result.txt', 'pseudonames.json')

# import json
# from pathlib import Path
# from pprint import pprint
#
# def file_to_json(file: Path):
#     data = {}
#     with open(file, 'r', encoding="utf-8") as f_read:
#         for line in f_read:
#             name, number = line.split(' - ')
#             data[name.capitalize()] = number
#         pprint(data)
#     with open(file.stem + '.json', 'w', encoding='utf-8') as f_write:
#         json.dump(data, f_write, ensure_ascii=False, indent=2)
#
# if __name__=="__main__":
#     file_to_json(Path('file_new.txt'))
# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import pickle
import csv
from pathlib import Path

def csv_to_str_pickle(file_csv: Path):
    with open(file_csv, 'r', encoding='utf-8', newline='') as f_r:
        csv_file = csv.reader(f_r, dialect='excel-tab')
        header = next(csv_file)
        data = [{k: v for k, v in zip(header, row)} for row in csv_file]
        return pickle.dumps(data)

if __name__ == '__main__':
    result = csv_to_str_pickle(Path('u_users.csv'))
    print(result)
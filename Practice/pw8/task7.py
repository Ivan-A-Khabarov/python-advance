# Задание №7 Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.

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
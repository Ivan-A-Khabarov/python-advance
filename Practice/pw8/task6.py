# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи
# 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import pandas as pd
import pickle

def convert_pickle_to_csv(pickle_file):
    with open(pickle_file, 'rb') as file:  # Открываем файл для чтения
        data = pickle.load(file)  # Загружаем данные из файла

    df = pd.DataFrame(data)  # Создаем DataFrame из данных

    # Извлекаем ключи словаря для заголовков столбца
    headers = list(df[0].keys())  # Получаем ключи первого элемента списка словарей

    # Сохраняем DataFrame в CSV-файл
    df.to_csv('output.csv', index=False, header=headers)  # Записываем данные в файл output.csv

# Пример использования функции
convert_pickle_to_csv('путь/к/pickle-файлу')
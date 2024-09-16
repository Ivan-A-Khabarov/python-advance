import pandas as pd

def read_csv_as_pickle(file_path):
    df = pd.read_csv(file_path)  # Считываем данные из файла
    data = df.to_dict(orient='records')  # Преобразуем DataFrame в список словарей
    return pickle.dumps(data)  # Возвращаем данные в виде pickle-строки

# Пример использования функции
print(read_csv_as_pickle('путь/к/CSV-файлу'))

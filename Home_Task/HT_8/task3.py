import json
import csv


def convert_json_to_csv(json_file_path, csv_file_path):
    """Считывает данные из JSON файла и сохраняет их в CSV файл."""

    # Чтение данных из JSON файла
    with open(json_file_path, 'r') as json_file:
        product_data = json.load(json_file)

    # Создание DictWriter для записи в CSV файл
    fieldnames = ['product_name', 'price', 'quantity']
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for product in product_data:
            writer.writerow(product)


if __name__ == "__main__":
    json_file_path = "products.json"
    csv_file_path = "products.csv"

    try:
        convert_json_to_csv(json_file_path, csv_file_path)
        print(f"Данные успешно сохранены в {csv_file_path}.")
    except Exception as e:
        print(f"Ошибка при конвертации: {e}")
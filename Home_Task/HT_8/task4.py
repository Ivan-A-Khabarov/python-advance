import csv


def calculate_total_sales(input_csv_path, output_csv_path):
    """Читает данные из CSV файла, подсчитывает общую выручку для каждого продукта и сохраняет результат в новом CSV файле."""

    # Словарь для хранения общей выручки по каждому продукту
    total_sales = {}

    with open(input_csv_path, 'r') as input_csv, open(output_csv_path, 'w', newline='') as output_csv:
        reader = csv.DictReader(input_csv)
        fieldnames = ['product_name', 'quantity', 'unit_price']
        writer = csv.DictWriter(output_csv, fieldnames=['product_name', 'total_revenue'])

        writer.writeheader()
        for row in reader:
            product_name = row['product_name'].strip()
            quantity = int(row['quantity'].strip())
            unit_price = float(row['unit_price'].strip())

            revenue = quantity * unit_price
            total_sales[product_name] = total_sales.get(product_name, 0) + revenue

        for product, revenue in total_sales.items():
            writer.writerow({'product_name': product, 'total_revenue': round(revenue, 2)})


if __name__ == "__main__":
    input_csv_path = "sales.csv"
    output_csv_path = "total_sales.csv"

    try:
        calculate_total_sales(input_csv_path, output_csv_path)
        print(f"Данные успешно сохранены в {output_csv_path}.")
    except Exception as e:
        print(f"Ошибка при расчете общей выручки: {e}")
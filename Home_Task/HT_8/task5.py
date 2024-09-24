import csv
import json


def convert_csv_to_grouped_json(csv_file_path, json_file_path):
    """Читает данные из CSV файла и сохраняет их в JSON файл с другой структурой."""

    author_books = {}

    with open(csv_file_path, 'r') as csv_file, open(json_file_path, 'w') as json_file:
        reader = csv.DictReader(csv_file)
        fieldnames = ['title', 'author', 'year']

        for row in reader:
            book = {
                'title': row['title'],
                'year': row['year']
            }
            author = row['author']

            if author not in author_books:
                author_books[author] = []

            author_books[author].append(book)

        json.dump(author_books, json_file, indent=4)


if __name__ == "__main__":
    csv_file_path = "books.csv"
    json_file_path = "books_by_author.json"

    try:
        convert_csv_to_grouped_json(csv_file_path, json_file_path)
        print(f"Данные успешно сохранены в {json_file_path}.")
    except Exception as e:
        print(f"Ошибка при преобразовании: {e}")
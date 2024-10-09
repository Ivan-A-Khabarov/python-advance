# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл

import json
from contextlib import AbstractContextManager

# Класс ContextManager реализует абстрактный контекстный менеджер
class ContextManager(AbstractContextManager):
    # Конструктор принимает имя файла для сохранения данных
    def __init__(self, filename):
        self.filename = filename
        self.data = {}

    # Метод __enter__ используется для входа в блок с управлением контекстом
    def __enter__(self):
        return self

    # Метод __exit__ используется для выхода из блока с управлением контекстом
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Открывает файл в режиме записи
        with open(self.filename, 'w') as file:
            # Записывает данные в файл в формате JSON
            json.dump(self.data, file)

    # Метод set устанавливает значение ключа
    def set(self, key, value):
        self.data[key] = value

    # Метод get получает значение по ключу
    def get(self, key, default=None):
        return self.data.get(key, default)

# Пример использования
with ContextManager('context.json') as ctx:
    ctx.set('ключ1', 'значение1')
    ctx.set('ключ2', 'значение2')

print(ctx.get('ключ1'))  # Вывод: значение1
print(ctx.get('ключ2'))  # Вывод: значение2

# Данные будут сохранены при выходе из блока with
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.

import json
import os


def load_data(json_filename):
    """Функция для загрузки данных из файла JSON"""
    if os.path.exists(json_filename):
        with open(json_filename, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {}
    return {}


def save_data(json_filename, data):
    """Функция для сохранения данных в файл JSON"""
    with open(json_filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def add_user(json_filename):
    """Функция для добавления пользователей в файл"""
    # Загружаем текущие данные
    data = load_data(json_filename)

    while True:
        # Запрашиваем у пользователя имя, идентификатор и уровень доступа
        name = input("Введите имя пользователя: ").strip()
        user_id = input("Введите уникальный идентификатор (число): ").strip()
        access_level = input("Введите уровень доступа (1-7): ").strip()

        # Проверяем, что уровень доступа является числом в пределах от 1 до 7
        if not access_level.isdigit() or not (1 <= int(access_level) <= 7):
            print("Ошибка: уровень доступа должен быть числом от 1 до 7.")
            continue

        access_level = int(access_level)

        # Проверка уникальности идентификатора
        if any(user_id in level_data for level_data in data.values()):
            print(f"Ошибка: идентификатор {user_id} уже существует.")
            continue

        # Добавляем нового пользователя
        if access_level not in data:
            data[access_level] = {}

        data[access_level][user_id] = name

        # Сохраняем обновлённые данные в JSON файл
        save_data(json_filename, data)

        print(f"Пользователь с именем {name} и идентификатором {user_id} успешно добавлен на уровень {access_level}.")
        break

# Пример вызова функции:
if __name__ == '__main__':
    add_user('users.json')

# 


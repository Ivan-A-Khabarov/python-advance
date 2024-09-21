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
from pathlib import Path


def set_users(file: Path) -> None:
    unique_id = set()

    if not file.is_file():
        data = {str(level): {} for level in range(1, 8)}
    else:
        with open(file, 'r', encoding='utf-8') as f_r:
            data = json.load(f_r)

    for dict_id in data.values():
        unique_id.update(dict_id)

    while True:
        user_name = input("Введите имя: ")
        if not user_name:
            break
        user_id = input("Введите id: ")
        user_level = input("Введите уровень: ")
        if user_id not in unique_id and int(user_level) in data:
            data[int(user_level)][user_id] = user_name
            unique_id.add(user_id)
        else:
            print("Неправильный ввод!")

    with open(file, 'w', encoding='utf-8') as f_w:
        json.dump(data, f_w, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    set_users(Path('users.json'))
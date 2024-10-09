# Задание №4.
# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.


import json

class User:
    def __init__(self, name, id, access_level):
        self.name = name
        self.id = id
        self.access_level = access_level

    def __repr__(self):
        return f"User({self.name}, {self.id}, {self.access_level})"

def load_users_from_file(filepath):
    users = []
    with open(filepath, 'r') as f:
        data = json.load(f)
        for user_data in data:
            users.append(User(user_data['name'], user_data['id'], user_data['access_level']))
    return users

# Пример использования
def main():
    # Добавляем пользователей вручную
    user1 = User('John Doe', 12345, 7)
    user2 = User('Jane Smith', 98765, 5)

    # Сохраняем пользователей в JSON файл
    with open('users.json', 'w') as f:
        json.dump([{'name': user1.name, 'id': user1.id, 'access_level': user1.access_level},
                   {'name': user2.name, 'id': user2.id, 'access_level': user2.access_level}], f)

    # Читаем пользователей из JSON файла обратно
    loaded_users = load_users_from_file('users.json')
    print(loaded_users)

if __name__ == '__main__':
    main()
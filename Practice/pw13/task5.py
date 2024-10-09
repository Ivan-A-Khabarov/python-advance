# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей. Добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.


import json

class User:
    def __init__(self, name, id, access_level):
        self.name = name
        self.id = id
        self.access_level = access_level

    def __eq__(self, other):
        return self.name == other.name and self.id == other.id

    def __repr__(self):
        return f"User({self.name}, {self.id}, {self.access_level})"

class Project:
    def __init__(self, filepath='users.json'):
        self.filepath = filepath
        self.users = self.load_users_from_file()

    def login(self, name, id):
        found_user = next((u for u in self.users if u.name == name and u.id == id), None)
        if found_user is None:
            raise AccessError(f"Пользователь с именем '{name}' и ID '{id}' не найден.")
        elif found_user.access_level < self.access_level:
            raise AccessError(f"Уровень доступа пользователя слишком низкий.")
        else:
            return found_user

    def add_user(self, name, id, access_level):
        if access_level < self.access_level:
            raise AccessError(f"Нельзя добавлять пользователей с уровнем доступа ниже вашего.")
        else:
            self.users.append(User(name, id, access_level))
            self.save_users_to_file()

    def save_users_to_file(self):
        with open(self.filepath, 'w') as f:
            json.dump([user.__dict__ for user in self.users], f)

    def load_users_from_file(self):
        users = []
        with open(self.filepath, 'r') as f:
            data = json.load(f)
            for user_data in data:
                users.append(User(**user_data))
        return users

class AccessError(Exception):
    def __init__(self, message):
        self.message = message

# Пример использования
def main():
    project = Project()

    # Добавляем пользователей вручную
    user1 = User('John Doe', 12345, 7)
    user2 = User('Jane Smith', 98765, 5)

    # Сохраняем пользователей в JSON файл
    with open('users.json', 'w') as f:
        json.dump([user1.__dict__, user2.__dict__], f)

    # Читаем пользователей из JSON файла обратно
    loaded_users = project.load_users_from_file()
    print(loaded_users)

    # Войти в систему
    logged_in_user = project.login('Jane Smith', 98765)
    print(logged_in_user)

    # Попробовать войти с неправильным именем
    try:
        project.login('Wrong Name', 98765)
    except AccessError as e:
        print(e.message)

    # Попробовать войти с правильным именем, но с неправильным ID
    try:
        project.login('Jane Smith', 12345)
    except AccessError as e:
        print(e.message)

    # Попробовать добавить пользователя с высоким уровнем доступа
    project.add_user('New User', 54321, 8)

    # Попробовать добавить пользователя с низким уровнем доступа
    try:
        project.add_user('Low Access User', 67890, 1)
    except AccessError as e:
        print(e.message)

if __name__ == '__main__':
    main()
import json
from pathlib import Path


class ProjectException(Exception):
    pass


class LevelError(ProjectException):
    def __init__(self, logged_in_user, level_new_user):
        self.logged_in_user = logged_in_user
        self.level_new_user = level_new_user

    def __str__(self):
        return (f'Нельзя добавить пользователя с уровнем - {self.level_new_user}\n'
                f'Вы вошли как {self.logged_in_user.name} и ограничены уровнями {self.logged_in_user.access_level}')


class AccessError(ProjectException):
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return (f'Нет такого пользователя в базе данных: \n'
                f'Имя - {self.name}\n'
                f'User_id - {self.id}')


class User:

    def __init__(self, name, user_id, access_level):
        self.name = name
        self.user_id = user_id
        self.access_level = access_level

    def __eq__(self, other):
        return self.name == other.name and self.user_id == other.user_id

    def __hash__(self):
        return hash((self.name, self.user_id))

    def __repr__(self):
        return f'User(name={self.name}, user_id={self.user_id}, access_level={self.access_level})'

    def __str__(self):
        return (f'Экземпляр класса пользователя:\n'
                f'Имя - {self.name}\n'
                f'User_id - {self.user_id}\n'
                f'Access_level - {self.access_level}\n')


class Project:
    def __init__(self):
        self.user = None
        self.users = set()

    def json_read(self, file: Path):
        with open(file, 'r', encoding='utf-8') as js_f_r:
            data = json.load(js_f_r)

        for access_level, id_name in data.items():
            for user_id, user_name in id_name.items():
                self.users.add(User(user_name, user_id, access_level))
        return self.users

    def system_enter(self, name, id):
        log_user = User(name, id, 0)
        # if log_user not in self.users:
        #     raise AccessError

        for user in self.users:
            if user == log_user:
                self.user = user
                return self.user
            else:
                raise AccessError(name, id)

    def add_user(self, name, id, level):
        if int(level) < int(self.user.access_level):
            raise LevelError(self.user, level)
        new_user = User(name, id, level)
        self.users.add(new_user)
        return new_user


if __name__ == '__main__':
    project = Project()
    project.json_read(Path('users.json'))
    project.system_enter('Алекс', '7g41')
    project.add_user('Саня', '2314', 1)
    print(project.users)
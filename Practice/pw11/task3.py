# **Задача 1:**

import time

class MyString:
    """Класс, который хранит строку, имя автора и время создания.

    Доступны все возможности str, а также методы get_author() и get_creation_time().
    """

    def __init__(self, string, author, creation_time):
        self.string = string
        self.author = author
        self.creation_time = creation_time

    # Переопределяем метод __str__, чтобы при выводе объекта класса выводилось значение поля string
    def __str__(self):
        return self.string

    def get_author(self):
        """Возвращает имя автора строки."""
        return self.author

    def get_creation_time(self):
        """Возвращает время создания строки."""
        return self.creation_time
# **Задача 2:**


class Archive:
    """Класс для хранения пар свойств (число и строка).

    Старые данные из ранее созданных экземпляров сохраняются в список архивов,
    который является свойством экземпляра.
    """

    def __init__(self):
        self.archives = []  # список архивов

    # метод для добавления нового элемента в список архивов
    def add_element(self, num, string):
        archive = [num, string]
        self.archives.append(archive)

    # методы для получения элементов списка архивов по индексу
    def get_num_by_index(self, index):
        """Возвращает число из элемента списка архивов с указанным индексом."""
        return self.archives[index][0]

    def get_string_by_index(self, index):
        """Возвращает строку из элемента списка архивов с указанным индексом."""
        return self.archives[index][1]

    # метод для вывода всех элементов списка архивов
    def print_archives(self):
        for archive in self.archives:
            print(f"{archive[0]} - {archive[1]}")

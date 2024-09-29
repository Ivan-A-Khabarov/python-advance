# Задание №1 Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)
import time
from time import localtime


class MyString:
    def __init__(self, string, author, creation_time):
        self.string = string
        self.author = author
        self.creation_time = time.localtime()

    # Переопределяем метод __str__, чтобы при выводе объекта класса выводилось значение поля string
    def __str__(self):
        return self.string

    def get_author(self):
        return self.author

    def get_creation_time(self):
        return self.creation_time

my_string = MyString("Привет, мир!", "Вася", time.time())
print(my_string)  # Привет, мир!
print(my_string.get_author())  # Вася
print(my_string.get_creation_time())  # Текущее время создания строки
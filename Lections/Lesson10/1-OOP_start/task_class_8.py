# Конструктор экземпляра
# При создании класса обычно используют функцию конструктор __init__.

class Person:
    max_up = 3

    def __init__(self):
        self.level = 1
        self.health = 100

p1 = Person()
p2 = Person()
print(f'{p1.max_up = }, {p1.level = }, {p1.health = }')
print(f'{p2.max_up = }, {p2.level = }, {p2.health = }')
# print(f'{Person.max_up = }, {Person.level = }, {Person.health = }') # AttributeError: type object 'Person' has no attribute 'level'

Person.level = 100
print(f'{Person.level = }, {p1.level = }, {p2.level = }')


# Внутри класса создаём функцию __init__. Два символа подчёркивания до и после
# имени говорят о том, что это “магическое имя”. Подобные имена нужны для
# добавления новых возможностей в работе класса и его экземпляров.
# Внутри функции заданы две переменные level и health. Это атрибуты экземпляров.
# Любой экземпляр получает заранее присвоенные значения. При этом сам класс не
# имеет доступа к заданным атрибутам
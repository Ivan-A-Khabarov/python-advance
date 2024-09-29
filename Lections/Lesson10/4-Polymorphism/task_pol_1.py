# class Person:
#
#     def change_health(self, other, quantity):
#         self.health += quantity
#         other.health -= quantity
#
# class Hero(Person):
#     def __init__(self, power, *args, **kwargs):
#         self.power = power
#         super().__init__(*args, **kwargs)
#     def change_health(self, other, quantity):
#         self.health += quantity * 2
#         other.health -= quantity * 2
#         ...
# p1 = Hero('archery', 'Сильвана', 'Эльф', 120)
# p2 = Person('Маг', 'Тролль')print(f'{p1.health = }, {p2.health =}')
# p1.change_health(p2, 10)
# print(f'{p1.health = }, {p2.health = }')
# p2.change_health(p1, 10)
# print(f'{p1.health = }, {p2.health = }')
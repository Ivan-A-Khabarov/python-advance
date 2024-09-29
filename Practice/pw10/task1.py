# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_circumference(self):
        return 2 * 3.14 * self.radius

    def get_area(self):
        return 3.14 * (self.radius ** 2)

my_circle = Circle(5)  # Создаём окружность с радиусом 5
print("Длина окружности:", my_circle.get_circumference())
print("Площадь окружности:", my_circle.get_area())
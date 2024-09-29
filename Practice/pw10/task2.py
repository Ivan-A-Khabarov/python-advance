# Задание №2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def get_perimeter(self):
        if self.length == 0 or self.width == 0:
            raise ValueError("Длина и ширина должны быть заданы.")
        return (self.length + self.width) * 2

    def get_area(self):
        if self.length == 0 or self.width == 0:
            raise ValueError("Длина и ширина должны быть заданы.")
        return self.length * self.width


my_rectangle = Rectangle(5, 3)  # Создаём прямоугольник с длиной 5 и шириной 3
print("Периметр прямоугольника:", my_rectangle.get_perimeter())
print("Площадь прямоугольника:", my_rectangle.get_area())
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # метод для вычисления периметра прямоугольника
    def get_perimeter(self):
        return (self.length + self.width) * 2

    def add(self, other):
        new_rectangle = Rectangle(0, 0)
        new_rectangle.length = (self.get_perimeter() + other.get_perimeter()) / 2
        new_rectangle.width = new_rectangle.length
        return new_rectangle

    def subtract(self, other):
        if self.get_perimeter() < other.get_perimeter():
            raise ValueError("Невозможно вычесть")
        else:
            new_rectangle = Rectangle(0, 0)
            new_rectangle.length = (self.get_perimeter() - other.get_perimeter()) / 2
            new_rectangle.width = new_rectangle.length
            return new_rectangle

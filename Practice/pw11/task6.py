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
        if self.get_perimeter() < other.get_perimiter():
            raise ValueError("Невозможно вычесть")
        else:
            new_rectangle = Rectangle(0, 0)
            new_rectangle.length = (self.get_perimeter() - other.get_perimeter()) / 2
            new_rectangle.width = new_rectangle.length
            return new_rectangle

    # Метод для вычисления площади прямоугольника
    def get_area(self):
        return self.length * self.width

    # Сравнение прямоугольников по площади
    def compare_areas(self, other):
        result = self.get_area() > other.get_area()
        return result

    def greater_than(self, other):
        return self.compare_areas(other)

    def less_than(self, other):
        return not self.greater_than(other)

    def equal_to(self, other):
        return not (self.greater_than(other) or self.less_than(other))

    def not_equal_to(self, other):
        return not self.equal_to(other)

# Задание №4
# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width):
        if new_width >= 0:
            self._width = new_width
        else:
            raise ValueError("Ширина должна быть положительной.")

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height):
        if new_height >= 0:
            self._height = new_height
        else:
            raise ValueError("Высота должна быть положительной.")

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)

# Пример использования
rect = Rectangle(3, 4)
print(rect.area())  # Output: 12
print(rect.perimeter())  # Output: 18

try:
    rect.width = -1
except ValueError as e:
    print(e)  # Output: Width must be positive.

rect.width = 5
print(rect.width)  # Output: 5
# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря dict.

class Descriptor:
    """Базовый класс для всех дескрипторов."""

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class DimensionDescriptor(Descriptor):
    """Дескриптор для ширины и высоты."""

    def __init__(self, name):
        super().__init__()
        self.name = name

    def __set__(self, instance, value):
        if value > 0:
            super().__set__(instance, value)
        else:
            raise ValueError(f"{self.name} must be positive.")


class RectangleFactory:
    """Класс-фабрика для создания экземпляров прямоугольника."""

    def create_rectangle(self, width, height):
        rectangle = object.__new__(Rectangle)
        rectangle._width = width
        rectangle._height = height
        return rectangle


class Rectangle:
    """Класс прямоугольника."""

    width = DimensionDescriptor("width")
    height = DimensionDescriptor("height")

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Пример использования
rect = RectangleFactory().create_rectangle(3, 4)
print(rect.area())  # Output: 12
print(rect.perimeter())  # Output: 18

try:
    rect.width = -1
except ValueError as e:
    print(e)  # Output: width must be positive.

rect.width = 5
print(rect.width)  # Output: 5
# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.

class ValidatedAttribute:
    """Базовый класс дескриптора для атрибутов с валидацией."""

    def __init__(self, validator):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if self.validator(value):
            instance.__dict__[self.name] = value
        else:
            raise ValueError(f"Invalid value for '{self.name}'")


class PositiveValidator:
    """Валет для проверки положительного значения."""

    def __call__(self, value):
        return value > 0


class Rectangle:
    """Класс прямоугольника."""

    width = ValidatedAttribute(PositiveValidator())
    height = ValidatedAttribute(PositiveValidator())

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Пример использования
rect = Rectangle(3, 4)
print(rect.area())  # Output: 12
print(rect.perimeter())  # Output: 18

try:
    rect.width = -1
except ValueError as e:
    print(e)  # Output: Invalid value for 'width'

rect.width = 5
print(rect.width)  # Output: 5
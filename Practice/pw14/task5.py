from functools import total_ordering

class Range:
    def __set_name__(self, owner, name):
        self.parametr_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.parametr_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.parametr_name, value)
    def validate(self, value):
        if value <= 0:
            raise ValueError('Значение value должно быть больше 0')


@total_ordering
class Rectangle:
    length = Range()
    width = Range()
    def __init__(self, _length, _width=None):
        if _width is None:
            self._width = _length
        else:
            self._width = _width
            self._length = _length

def get_length(self):
    return self._length

def get_width(self):
    return self._width

def perimeter(self):
    return self._length * 2 + self._width * 2

def area(self):
    return self._length * self._width

def __add__(self, other):
    new__length = self._length + other._length
    new_perimeter = self.perimeter() + other.perimeter()
    new__width = new_perimeter / 2 - new__length
    return Rectangle(new__length, new__width)

def __sub__(self, other):
    new_perimeter = abs(self.perimeter() - other.perimeter())
    new__length = abs(self._length - other._length)
    new_width = new_perimeter / 2 - new__length
    return Rectangle(new__length, new_width)

def __eq__(self, other):
    return self.area() == other.area()

def __gt__(self, other):
    return self.area() > other.area()

def __ge__(self, other):
    return self.area() >= other.area()



if __name__ == '__main__':
    r1 = Rectangle(1, 2)
    print(r1.length)
    print(r1.width)
    r1.length = 12
    r1.width = 15
    print(r1.length)
    print(r1.width)
    r1.length = -12
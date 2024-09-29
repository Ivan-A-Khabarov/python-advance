class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age

    @property
    def age(self):
        return self._age

    def birthday(self):
        self._age += 1

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Employee(Person):
    def __init__(self, id_number, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.__id_number = id_number

    @property
    def id_number(self):
        return self.__id_number

    @id_number.setter
    def id_number(self, value):
        if not isinstance(value, int) or len(str(value)) != 6:
            raise ValueError("ID-номер должен быть шестизначным числом")
        self.__id_number = value

    @property
    def access_level(self):
        sum_of_digits = sum([int(digit) for digit in str(self.id_number)])
        access_level = sum_of_digits % 7
        return access_level

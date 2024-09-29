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


my_person = Person("Иван", "Иванов", 30)  # Создаём человека с именем Иван Иванов и возрастом 30 лет
print("Возраст:", my_person.age)
my_person.birthday()  # Увеличиваем возраст на 1 год
print("Новый возраст:", my_person.age)
print("Полное ФИО:", my_person.full_name())
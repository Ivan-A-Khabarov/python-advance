import re

class Person:
    def __setattr__(self, name, value):
        if name == 'name':
            if not value.istitle():
                raise ValueError("Имя должно начинаться с заглавной буквы и состоять из букв")
        elif name == 'age':
            if not isinstance(value, int) or value < 0 or value > 120:
                raise ValueError("Возраст должен быть целым числом от 0 до 120")
        elif name == 'email':
            if not re.match(r'[^@]+@[^@]+\.[^@]+', value):
                raise ValueError("Неверный формат электронной почты")
        super().__setattr__(name, value)

    def __str__(self):
        return f"Person(name={self.name}, age={self.age}, email={self.email})"

# Пример использования
try:
    p = Person()
    p.name = "John"
    p.age = 25
    p.email = "john@example.com"
    print(p)
except ValueError as e:
    print(e)
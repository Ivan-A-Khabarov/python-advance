class ValidationError(Exception):
    pass

class NameValidationError(ValidationError):
    def __init__(self):
        super().__init__("Имя должно состоять из хотя бы двух слов, каждое из которых начинается с заглавной буквы.")

class EmailValidationError(ValidationError):
    def __init__(self):
        super().__init__("Электронная почта должна содержать символ '@' и точку '.'.")

class AgeValidationError(ValidationError):
    def __init__(self):
        super().__init__("Возраст должен быть целым числом от 0 до 120.")

class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        words = value.split()
        if len(words) < 2 or any(not word[0].isupper() for word in words):
            raise NameValidationError()
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        parts = value.split("@")
        if "@@" not in value or not (parts[-1].count(".") > 0 and "." in parts[-1]):
            raise EmailValidationError()
        self._email = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not (isinstance(value, int) and 0 <= value <= 120):
            raise AgeValidationError()
        self._age = value

# Пример использования:
try:
    user = User(name="John Doe", email="john.doe@example.com", age=25)
    print(f"User created: {user.name}, {user.email}, {user.age}")
except ValidationError as e:
    print(e)
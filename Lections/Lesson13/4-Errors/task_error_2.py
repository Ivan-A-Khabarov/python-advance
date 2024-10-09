# Теперь внесём правки в код инициализации пользователя. Заодно избавимся от
# магических чисел для минимальной и максимальной длины имени.

from task_error_1 import UserAgeError, UserNameError


class User:
    MIN_LEN = 6
    MAX_LEN = 30

    def __init__(self, name, age):
        if self.MIN_LEN < len(name) < self.MAX_LEN:
            self.name = name
        else:
            raise UserNameError
        if not isinstance(age, (int, float)) or age < 0:
            raise UserAgeError
        else:
            self.age = age

user = User('Яков', '-12')

# Подобный код отлично справляется с поставленной задачей. Но стал менее
# информативен в случае возникновения ошибок.


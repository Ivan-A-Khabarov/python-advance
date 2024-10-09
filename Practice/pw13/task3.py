# Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

class BaseException(Exception):
    pass

class LevelError(BaseException):
    def __init__(self, level):
        self.level = level
        super().__init__(f"Уровень '{level}' не поддерживается")

class AccessError(BaseException):
    def __init__(self, username):
        self.username = username
        super().__init__(f"Недостаточно прав для пользователя '{username}'")

# Пример использования
try:
    raise LevelError('user')
except LevelError as e:
    print(f"Ошибка уровня: {e.level}")

try:
    raise AccessError('admin')
except AccessError as e:
    print(f"Ошибка доступа: {e.username}")
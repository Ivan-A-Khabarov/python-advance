# Задание №6
# Доработайте классы исключения так, чтобы они выдали
# подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода
# проекта.

class BaseException(Exception):
    pass

class LevelError(BaseException):
    def __init__(self, level, msg="Уровень '{level}' не поддерживается"):
        self.level = level
        self.msg = msg
        super().__init__(self.msg.format(level=level))

    def __str__(self):
        return f"{self.msg}\n\tУровень: {self.level}"

class AccessError(BaseException):
    def __init__(self, username, reason=""):
        self.username = username
        self.reason = reason
        super().__init__(f"Недостаточно прав для пользователя '{username}'. {self.reason}")

    def __str__(self):
        return f"{self.username} не имеет достаточного уровня доступа.\n\tПричина: {self.reason}"

# Пример использования
try:
    raise LevelError('user')
except LevelError as e:
    print(e)

try:
    raise AccessError('admin', 'Права заблокированы временно')
except AccessError as e:
    print(e)
# Внимание! В классе User надо исправит строку вызова ошибки имени,
# чтобы код сработал верно. Иначе исключение вернёт нам исключение
# TypeError: UserNameError.__init__() missing 2 required positional arguments:
# 'lower' and 'upper'
# ...
# def __init__(self, name, age):
#     if self.MIN_LEN < len(name) < self.MAX_LEN:
#         self.name = name
#     else:
#         raise UserNameError(name, self.MIN_LEN, self.MAX_LEN)
# ...

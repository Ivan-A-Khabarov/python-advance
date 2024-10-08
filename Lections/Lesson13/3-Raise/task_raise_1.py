# Отдельно рассмотрим команду raise для поднятия исключений. С ней мы уже
# сталкивались на прошлой лекции. Команда поднимает исключение, указанное
# после неё. Используется для случаев, когда вы явно хотите сообщить о
# неправильной работе вашего кода.
# Например у нас есть функция, которая запрещает изменять значение у
# существующих ключей.

def add_key(dct, key, value):
    if key in dct:
        raise KeyError (f'Перезаписывание существующего ключа запрещено. {dct[key] = }')
    dct[key] = value
    return dct

data = {'one': 1, 'two': 2}
print(add_key(data, 'three', 3))
print(add_key(data, 'three', 3))

# Первый раз мы смогли добавить пару ключ-значение в словарь. Но строкой ниже
# получили ошибку. Ключ уже добавлен в словарь и изменить его нельзя. Поднимаем
# исключение KeyError.

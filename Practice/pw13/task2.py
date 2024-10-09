# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

def get_default(dictionary, key, default_value):
    try:
        return dictionary[key]
    except KeyError:
        return default_value

# Пример использования
d = {'a': 1, 'b': 2}

# Тестовый случай с существующим ключом
print(get_default(d, 'a', 'default'))  # Output: 1

# Тестовый случай с несуществующим ключом
print(get_default(d, 'c', 'default'))  # Output: 'default'
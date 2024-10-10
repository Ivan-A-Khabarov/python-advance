# Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа



my_tuple = ('строка', 1, True, 3.14)

type_to_values = {}
for element in my_tuple:
    type_name = type(element).__name__
    if type_name not in type_to_values:
        type_to_values[type_name] = []
    type_to_values[type_name].append(element)

print(type_to_values)
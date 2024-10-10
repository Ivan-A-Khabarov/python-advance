def to_binary_octal(number):
    """Преобразует целое число в двоичную и восьмеричную системы счисления."""
    binary_str = f'{number:b}'
    octal_str = f'{number:o}'
    return binary_str, octal_str

# Чтение числа от пользователя
number = int(input("Введите целое число: "))

# Преобразование и отображение результатов
binary_result, octal_result = to_binary_octal(number)
print(f"Двоичное представление: {binary_result}")
print(f"Восьмеричное представление: {octal_result}")
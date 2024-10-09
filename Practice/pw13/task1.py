# Задание №1.
# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число. Обрабатывайте не числовые данные как исключения.

def get_number():
    while True:
        try:
            input_value = input("Введите целое или вещественное число: ")
            if input_value.strip() == '':
                continue
            return int(input_value) if input_value.isdigit() else float(input_value)
        except ValueError:
            print("Вы ввели не числовое значение. Пожалуйста, попробуйте снова.")

# Пример использования
while True:
    number = get_number()
    print(f"Вы ввели число {number}")
    choice = input("Хотите ввести еще одно число? (y/n) ").lower()
    if choice != 'y':
        break
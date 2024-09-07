#  Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
# Определяем переменные

apples = 10
oranges = 20
bananas = 30
apple = 100
orange = 200
s = 5  # Специальная переменная, которую трогать не нужно


def replace_s_variables():
    # Используем словарь глобальных переменных
    globals_dict = globals()

    # Проходим по всем переменным в глобальном пространстве
    for var_name in list(globals_dict.keys()):
        # Если переменная оканчивается на 's' и это не переменная 's'
        if var_name.endswith('s') and var_name != 's':
            # Создаём переменную без 's' на конце
            new_var_name = var_name[:-1]
            # Переносим значение в новую переменную
            globals_dict[new_var_name] = globals_dict[var_name]
            # Заменяем старую переменную на None
            globals_dict[var_name] = None


# Запуск функции
replace_s_variables()

# Проверка результата
print(f"apples: {apples}, apple: {apple}")
print(f"oranges: {oranges}, orange: {orange}")
print(f"bananas: {bananas}, banana: {'banana' in globals()}")  # проверим, создалась ли переменная banana
print(f"s: {s}")  # Переменная s не должна измениться

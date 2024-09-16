# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from random import  randint, choice
import string
from pathlib import  Path

VOWELS = "aeiou"
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'
MIN_LEN = 4
MAX_LEN = 7


def generate_name():
      # Гласные
    consonants = "".join(set(string.ascii_lowercase) - set(VOWELS))  # Согласные

    name_length = randint(4, 7)  # Длина имени от 4 до 7 символов
    name = [choice(consonants)]  # Начинаем с согласной

    # Гарантируем, что хотя бы одна гласная присутствует в имени
    for _ in range(name_length - 1):
        if len([ch for ch in name if ch in VOWELS]) == 0:
            name.append(choice(VOWELS))
        else:
            name.append(choice(string.ascii_lowercase))

    # Превращаем первую букву в заглавную
    name[0] = name[0].upper()

    return "".join(name)


def save_names_to_file(filename, num_names):
    with open(filename, 'w') as f:
        for _ in range(num_names):
            f.write(generate_name() + "\n")


# Пример использования:
filename = "pseudonames.txt"
num_names = 10  # Количество генерируемых имен
save_names_to_file(filename, num_names)


# Объяснение:
# Импортируем библиотеки:
#
# random — для случайного выбора элементов.
# string — для получения всех строчных букв английского алфавита с помощью string.ascii_lowercase.
# Функция generate_name():
#
# Создаем набор гласных и согласных букв.
# Генерируем длину имени в диапазоне от 4 до 7 символов.
# Начинаем имя с согласной и гарантируем, что хотя бы одна гласная присутствует.
# Превращаем первую букву имени в заглавную.
# Функция save_names_to_file(filename, num_names):
#
# Открываем файл для записи.
# Вызываем функцию generate_name() нужное количество раз и записываем результат в файл.
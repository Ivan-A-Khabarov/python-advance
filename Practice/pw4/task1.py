# Задание №1
# Погружение в Python | Функции
# ✔ Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

def print_sorted_words(text):
    words = text.split()
    sorted_words = sorted(words)
    max_len = len(max(sorted_words, key=len))
    for i, word in enumerate(sorted_words,start=1):
        print(f'{i}.{word.rjust(max_len)}')

text = input("Введите текст: ")
print_sorted_words(text)

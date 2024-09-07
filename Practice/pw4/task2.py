# Задание №2
# ✔ Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

def unique_unicode(text):
    unique = list(set(ord(char) for char in text))
    sorted_codes = sorted(unique, reverse=True)
    return sorted_codes

text = input('Введите текст: ')
unique_unicode = unique_unicode(text)
print(unique_unicode)

# Напишите генераторную функцию substrings(s), которая принимает строку
# s и возвращает генератор всех возможных подстрок этой строки.
# На вход подается строка abc
# На выходе будут выведены обозначения:
# a
# ab
# abc
# b
# bc
# c


def substring(s):
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            yield s[start:end]

s = input("Введите строку: ")
for substring in substring(s):
    print(substring)
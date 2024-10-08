# Задача 5. Нахождение анаграмм
# Напишите программу, которая принимает два слова и определяет, являются ли
# они анаграммами.
# Подсказка № 1
# Сначала проверьте, равна ли длина двух слов. Если они имеют разную длину, они не
# могут быть анаграммами.
# Подсказка № 2
# Создайте два пустых словаря для хранения частоты символов каждого слова. Один
# словарь для первого слова, другой для второго.
# Подсказка № 3
# Пройдитесь по каждому символу в первом слове и увеличьте счётчик в словаре.
# Повторите это для второго слова.
# Подсказка № 4
# После подсчета символов сравните оба словаря. Если они идентичны, слова являются
# анаграммами.

word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

if len(word1) == len(word2):
    print("Слова имеют одинаковую длину")
else:
    char_count1 = {}
    char_count2 = {}

    for i in word1:
        if i in char_count1:
            char_count1[i] += 1
        else:
            char_count1[i] = 1

    for i in word2:
        if i in char_count2:
            char_count2[i] += 1
        else:
            char_count2[i] = 1

    if char_count1 == char_count2:
        print("Слова являются анаграммами")
    else:
        print("Слова не являются анаграммами")
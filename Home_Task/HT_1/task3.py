# Напишите программу, которая считает количество простых чисел в заданной
# последовательности и выводит ответ на экран.
# Простое число делится только на себя и на единицу. Последовательность
# задаётся при помощи вызова ввода (input) на каждой итерации цикла. Одна
# итерация — одно число.

# Запрос количества чисел в последовательности
n = int(input("Введите количество чисел в последовательности: "))
# Инициализация счётчика
count = 0

for i in range(n):
    number = int(input("Введите число: "))

    # Проверка на простое число
    if number > 1:
        for j in range(2, number):
            if (number % j) == 0:
                break
        else:
            count += 1

print('Количество простых чисел в последовательности:', count)
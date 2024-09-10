# Задание 1. Квадраты чисел
# Пользователь вводит число N. Напишите программу, которая генерирует
# последовательность из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так
# далее). Реализацию напишите двумя способами: функция-генератор и
# генераторное выражение.

# способ 1

def square_generator(n):
    for i in range(1, n + 1):
        yield i ** 2
# Пример использования функции-генератора
N = int(input("Введите число N: "))
squares = square_generator(N)
for square in squares:
    print(square)

# способ 2

N = int(input("Введите число N: "))
squares = (i ** 2 for i in range(1, N + 1))
for square in squares:
    print(square)

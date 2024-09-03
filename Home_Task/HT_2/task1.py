# Задача 1. Нахождение наибольшего общего делителя (НОД) двух
# чисел
# Программа принимает два целых числа и находит их наибольший общий
# делитель (НОД).
# Подсказка № 1
# Для решения задания используйте принцип алгоритма Евклида: если у вас есть два
# числа, вы можете заменить большее число на остаток от деления большего числа на
# меньшее. Повторяйте этот процесс до тех пор, пока одно из чисел не станет нулем.
# Подсказка № 2
# Используйте цикл while, чтобы повторять шаги алгоритма Евклида до тех пор, пока
# одно из чисел не станет нулем. В каждом шаге обновляйте значения так, чтобы
# большее число становилось меньшим числом, а меньшее число становилось остатком
# от деления.
# Подсказка № 3
# Когда одно из чисел становится нулем, другое число является наибольшим общим
# делителем (НОД). Это и будет результатом выполнения программы.

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
while b:
    a, b = b, a % b
    print("НОД:",a)
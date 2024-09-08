# Задание 1. Апгрейд калькулятора
# Степан использует калькулятор для расчёта суммы и разности чисел, но на
# работе ему требуются не только обычные арифметические действия. Он ничего
# не хочет делать вручную, поэтому решил немного расширить функционал
# калькулятора.
# Напишите программу, запрашивающую у пользователя число и действие,
# которое нужно сделать с числом: вывести сумму его цифр, максимальную или
# минимальную цифру. Каждое действие оформите в виде отдельной функции, а
# основную программу зациклите.
# Запрошенные числа должны передаваться в функции суммы, максимума и
# минимума при помощи аргументов.

def digits_sum(number):
    sum = 0
    while number > 0:
        digit = number % 10 # получаем цифру из числа, округляем до целого, получаем её цифру, умножаем на 10, получаем её цифру
        sum += digit
        number //= 10
    print(sum) # выводим сумму цифр

def max_digit(number):
    max = 0
    while number > 0:
        digit = number % 10
        if digit > max:
            max = digit
        number //= 10
    print("Максимальная цифра: ", max)

def min_digit(number):
    min = 0
    while number > 0:
        digit = number % 10
        if digit < min:
            min = digit
        number //= 10
    print("Минимальная цифра: ", min)

while True:
    number = int(input("Введите число: "))
    action = input("Введите действие: ")
    if action == "сумма":
        digits_sum(number)
    elif action == "максимум":
        max_digit(number)
    elif action == "минимум":
        min_digit(number)
    else:
        print("Неверное действие")
# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

list = []
for item in range(1, 101):
    if item % 3 == 0 and item % 5 == 0:
        list.append("FizzBuzz")
    elif item % 3 == 0:
        list.append("Fizz")
    elif item % 5 == 0:
        list.append("Buzz")
    else:
        list.append(item)
print(list)

# тернарный вариант
list_2 = ('FizzBuzz' if item % 15 == 0 else 'Fizz' if item % 3 == 0 else 'Buzz' if item % 5 == 0 else item for item in range(1, 101))
print(tuple(list_2))
# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.

gen = (x for x in range(0, 101, 2) if x // 10 + x % 10 != 8) # решение математикой.
gen1 = (i for i in range(0, 101, 2) if sum(map(int, str(i))) != 8) # решение через map() и функцию sum().
gen2 = filter(lambda x: sum(map(int, str(x)))!= 8, range(0, 101, 2)) # решение через лямбда выражение.

print(*list(gen))
print(*list(gen1))
print(*list(gen2))

# Задание
# Перед вами несколько строк кода. Напишите что выведет каждая из строк, не
# запуская код. У вас 3 минуты.

data = {"один": 1, "два": 2, "три": 3}
x = iter(data.items())
print(x) # <dict_itemiterator object at 0x00000225F7555AD0>
y = next(x)
print(y) # ('один', 1)
z = next(iter(y))
print(z) # один

#
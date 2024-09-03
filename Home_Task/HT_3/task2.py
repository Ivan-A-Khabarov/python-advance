# Задача 2. Поиск наибольшего числа в списке
# Напишите программу, которая принимает список чисел через строку и
# возвращает наибольшее число в этом списке.
# Подсказка № 1
# После получения строки чисел, используйте метод split() для разделения строки на
# отдельные числа. Затем преобразуйте их в целые числа.
# Подсказка № 2
# Определите, как правильно инициализировать переменную, которая будет хранить
# наибольшее число. Обычно это первый элемент списка.
# Подсказка № 3
# Сделайте проход по каждому элементу списка и сравнить его с текущим наибольшим
# числом. Если найдете число больше текущего наибольшего, то его нужно сменить.

# принимаем строку ввода от пользователя и разбиваем ее на список чисел через пробел.

nums = [int(x) for x in input('В введите числа через пробел: ').split()]

max_num = nums[0] # создаем переменную, которая будет хранить наибольшее число.

for num in nums:
    if num > max_num:
        max_num = num # сравниваем текущее наибольшее число с текущим наибольшим. Если больше, то меняем его. Если меньше, то не меняем.
print("Самое наибольшее число в списке -",max_num) # выводим на экран наибольшее число.
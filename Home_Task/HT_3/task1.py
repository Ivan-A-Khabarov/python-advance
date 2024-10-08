# Задание 1. Удаление дубликатов из списка
# Дан список повторяющихся элементов. Вернуть список с дублирующимися
# элементами. В результирующем списке не должно быть дубликатов.
# Подсказка № 1
# Для решения задачи вам нужно найти элементы, которые повторяются в списке.
# Подумайте о том, как можно определить, что элемент повторяется.
# Подсказка № 2
# Метод count позволяет узнать, сколько раз элемент встречается в списке.
# Используйте его, чтобы определить, является ли элемент дублирующимся.

elements = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 88, 88, 91, 91] # список элементов, которые повторяются в списке

duplicates = [] # пустой список, в который будут записаны дубликаты элементов из списка elements.

for element in elements: # перебираем элементы списка elements.
    if elements.count(element) > 1 and element not in duplicates:
        duplicates.append(element) # если элемент встречается в списке более одного раза и не является дубликатом,
                                   # то добавляем его в список duplicates. Если элемент является дубликатом,
print(duplicates) # выводим список дубликатов.

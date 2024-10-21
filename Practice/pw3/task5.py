# Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

# Создание списка с повторяющимися целыми числами
repeating_numbers = [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Список с порядковыми номерами нечётных элементов
odd_indices = []

for i in range(len(repeating_numbers)):
    if repeating_numbers[i] % 2 != 0:
        odd_indices.append(i + 1)

print(odd_indices)
# [1, 3, 5, 7]
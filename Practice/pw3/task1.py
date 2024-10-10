# Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

# Вариант 1
original_list = [1, 4, 6, 7, 8, 9, 4]
unique_elements = list(set(original_list))
print("Unique elements:", unique_elements)

# Вариант 2
def remove_duplicates(lst):
    result = []
    
    for item in lst:
        if item not in result:
            result.append(item)
            
    return result

original_list = [1, 4, 6, 7, 8, 9, 4]
unique_elements = remove_duplicates(original_list)
print("Unique elements:", unique_elements)
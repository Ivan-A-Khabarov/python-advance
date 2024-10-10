

from itertools import cycle

# Создание списка с повторяющимися элементами
repeating_list = list(cycle(['a', 'b']))
print(repeating_list[:10])  # Остановимся на первых 10 элементах
# ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']

# Удаление всех элементов, которые встречаются дважды
cleaned_list = []
seen = set()
for element in repeating_list:
    if element not in seen:
        cleaned_list.append(element)
        seen.add(element)

print(cleaned_list)
# ['a', 'b']
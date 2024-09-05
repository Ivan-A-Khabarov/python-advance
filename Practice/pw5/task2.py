# Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку

text = 'dsgsdg 23846123874'

for_dict = {}
for key in set(text):
    for_dict[key] = ord(key)
print(for_dict)

for_dict = {key: ord(key) for key in set(text)}
print(for_dict)

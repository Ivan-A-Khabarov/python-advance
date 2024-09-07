def unicode_dict_from_range(text):
    num1, num2 = map(int, text.split())

    start = min(num1, num2)
    end = max(num1, num2)

    unicode_dict = {chr(i): i for i in range(start, end + 1)}
    return unicode_dict

text = input("Введите текст: ")
unicode_dict = unicode_dict_from_range(text)
print(unicode_dict)
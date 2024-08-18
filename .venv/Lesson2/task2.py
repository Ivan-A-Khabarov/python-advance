text = input('Введите текст: ')
if str.isnumeric(text):
    print(bin(int(text)))
    print(oct(int(text)))
    print(hex(int(text)))
else:
    if str.isascii(text):
        print('Текст написан в ASCII')
    else:
        print('Текст не написан в ASCII')
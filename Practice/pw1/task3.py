rows = int(input("Сколько рядов у ёлки? "))

for row in range(rows):
    spaces = rows - row - 1
    stars = 2 * row + 1

    # Печатаем пробелы перед звездочками
    print(' ' * spaces, end='')

    # Печатаем звездочки
    print('*' * stars)
# Задание №5
# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

# Решение:


def riddle(secret, answers, qty = 3):
    count_answers = 0
    print(f'Угадай загадку: {secret}')
    for tries in range(1, qty + 1):
        answer = input('Введите ответ: ').lower()
        if answer in answers:
            return tries
    return 0

def storage():
    puzzles = {"Зимой и летом одним цветом": ['ель', 'елка', ',бакс'],
              "Не лает ни кусает в дом не пускает": ['замок', 'домофон'],
              "Сидит дед во сто шуб одет": ['лук', 'луковица']}
    # print(puzzles.items())
    for key, value in puzzles.items():
        # print(key, value)
        result = riddle(key, value)
        print(f'Угадал с {result} попытки' if result > 0 else f'Не угадал!')
if __name__ == '__main__':
    storage()
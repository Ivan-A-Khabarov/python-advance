# Защищённый словарь для хранения результатов
_results = {}

def add_result(riddle_text, attempt):
    """Функция добавляет результат угадывания в защищённый словарь"""
    _results[riddle_text] = attempt

def show_results():
    """Функция выводит результаты угадывания в удобном виде"""
    for riddle, attempt in _results.items():
        result = (f'Угадана с {attempt} попытки' if attempt > 0 else 'Не угадана')
        print(f'Загадка: "{riddle}" - {result}')

def riddle(secret, answers, qty=3):
    """Функция задает загадку и возвращает номер попытки, с которой была угадана"""
    print(f'Угадай загадку: {secret}')
    for tries in range(1, qty + 1):
        answer = input('Введите ответ: ').lower()
        if answer in answers:
            return tries
    return 0

def storage():
    """Функция содержит загадки и вызывает функцию угадывания"""
    puzzles = {
        "Зимой и летом одним цветом": ['ель', 'елка'],
        "Не лает, не кусает, в дом не пускает": ['замок', 'домофон'],
        "Сидит дед, во сто шуб одет": ['лук', 'луковица']
    }

    for key, value in puzzles.items():
        result = riddle(key, value)
        add_result(key, result)
        print(f'Угадал с {result} попытки' if result > 0 else 'Не угадал!')

if __name__ == '__main__':
    storage()
    print("\nРезультаты угадывания:")
    show_results()
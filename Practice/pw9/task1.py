# Задание №1 Создайте функцию-замыкание, которая запрашивает два целых числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
import random


def generate_guessing_game(max_num=100, max_attempts=10):
    def guessing_game():
        secret_number = random.randint(1, max_num)
        attempts = 0
        while True:
            guess = int(input(f'Попытайтесь угадать число от 1 до {max_num}: '))
            attempts += 1
            if guess == secret_number:
                print(f'Вы угадали число за {attempts} попытку!')
                break
            elif guess > secret_number:
                print('Ваше число больше задуманного. Попробуйте снова.')
            else:
                print('Ваше число меньше задуманного. Попробуйте снова.')

            if attempts >= max_attempts:
                print(f'Вы превысили максимальное количество попыток ({max_attempts}). Игры окончена.')
                break

    return guessing_game

games = [generate_guessing_game(), generate_guessing_game(max_num=50)]
for game in games:
    game()

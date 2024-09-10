import random

LOWER_LIMIT = 1
UPPER_LIMIT = 10
TRY_LIMIT = 3

def guess_the_numb():
    user_number = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
    rand_numb = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    counter = 1
    while counter <= TRY_LIMIT:
        if user_number == rand_numb:
            return True
        elif user_number < rand_numb:
            user_number = int(input('Ваше число меньше загаданного, попробуйте ещё раз: '))
        else:
            user_number = int(input('Ваше число больше загаданного, попробуйте ещё раз: '))
        counter += 1
    return False

if __name__ == '__main__':
    print(guess_the_numb())
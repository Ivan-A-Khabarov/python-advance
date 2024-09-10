from random import randrange
from sys import argv

def guess_the_numb(low_limit: int = 0, upper_limit: int = 100, try_limit: int = 10):
    user_number = int(input(f'Введите число от {low_limit} до {upper_limit}: '))
    rand_numb = randrange(low_limit, upper_limit + 1)
    counter = 1
    while counter <= try_limit:
        if user_number == rand_numb:
            return True
        elif user_number < rand_numb:
            user_number = int(input('Ваше число меньше загаданного, попробуйте ещё раз: '))
        else:
            user_number = int(input('Ваше число больше загаданного, попробуйте ещё раз: '))
        counter += 1
    return False

if __name__ == '__main__':
    # print(guess_the_numb())
    _, *param = argv
    print(guess_the_numb(*(int(n) for n in param)))
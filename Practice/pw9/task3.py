import random
from typing import Callable


def validate_number(value: int, min_val: int, max_val: int) -> None:
    if value < min_val or value > max_val:
        raise ValueError(f"Number out of range: expected between {min_val} and {max_val}, got {value}.")


def validate_count(value: int, min_val: int, max_val: int) -> None:
    if value < min_val or value > max_val:
        raise ValueError(f"Count out of range: expected between {min_val} and {max_val}, got {value}.")


def number_control(func: Callable):
    def wrapper(*args, **kwargs):
        try:
            validate_number(args[0], 1, 100)
            validate_count(args[1], 1, 10)
        except ValueError as e:
            print(e)
            return func(random.randint(1, 100), random.randint(1, 10), *args, **kwargs)
        else:
            return func(*args, **kwargs)

    return wrapper


@number_control
def number_endeavors(num, count):
    for _ in range(count):
        user_input_num = int(input("Введите число от 1 до 100: "))
        print(f"Оставшееся количество попыток - {count - _}")
        if user_input_num == num:
            return f"Поздравляю число угадано - {num}, за сколько попыток {_}"
        elif user_input_num > num:
            print("Искомое число меньше!")
        elif user_input_num < num:
            print("Искомое число больше!")
    return "Закончились попытки"


if __name__ == '__main__':
    result = number_endeavors(500, 5)
    print(result)
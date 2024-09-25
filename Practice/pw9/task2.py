from random import randint

def num_riddles(num=randint(1, 100), count=10):
    def num_endeavors():
        for i in range(1, count + 1):
            user_input_num = int(input('Введите число от 1 до 100: '))
            print(f"Оставшееся количество попыток - {count - i}")
            if user_input_num == num:
                return f'Поздравляю число угаданно - {num}, за сколько попыток {i}'
            elif user_input_num > num:
                print('Искомое число меньше!')
            elif user_input_num < num:
                print('Искомое число больше!')
        return 'Закончились попытки'
    return num_endeavors

if __name__ == '__main__':
    func_num_game = num_riddles()
    print(func_num_game())
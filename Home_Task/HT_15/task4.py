# Задача 4. Опции и флаги
# Напишите скрипт, который принимает два аргумента командной строки: число и
# строку. Добавьте следующие опции:
# ● --verbose, если этот флаг установлен, скрипт должен выводить
# дополнительную информацию о процессе.
# ● --repeat, если этот параметр установлен, он должен указывать,
# сколько раз повторить строку в выводе.

import argparse

def main():

    parser = argparse.ArgumentParser("Программа для работы с числами и строками.")
    parser.add_argument('number', type=int, help='Число, которое нужно обработать')
    parser.add_argument('text', type=str, help='Строка, которую нужно вывести')
    parser.add_argument('--verbose', action='store_true', help='Выводит дополнительную информацию')
    parser.add_argument('--repeat', type=int, default=1, help='Сколько раз повторить строку')
    args = parser.parse_args()

    if args.verbose:
        print(f"Получено число: {args.number}")
        print(f"Получена строка: '{args.text}'")
        print(f"Повторять строку {args.repeat} раз")


    for _ in range(args.repeat):
        print(args.text)


if __name__ == "__main__":
    main()
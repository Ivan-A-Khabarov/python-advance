# ● Цикл while для обработки ошибок ввода
# Иногда необходимо получить данные повторно, если попытка не удалась. В случае с
# пользователем можем спрашивать его бесконечно, пока не добъёмся ввода целого
# числа.



def get(text: str = None) -> int:
    while True:
        try:
            num = int(input(text))
            break
        except ValueError as e:
            print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
                  f'Попробуйте снова')
    return num

if __name__ == '__main__':
    number = get('Введите целый делитель: ')
    print(f'100/{number} = {100 / number}')

# Бесконечный цикл while True можно прервать командой break. В случае
# преобразования ввода пользователя к целому без ошибок она завершит цикл и
# вернёт число из функции. При появлении ошибки дальнейшие строки не
# выполняются, сразу переходим в блок except. Обработав ошибку мы возвращаемся
# к началу цикла, следовательно повторяем запрос.
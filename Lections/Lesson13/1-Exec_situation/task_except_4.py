# Как вы уже догадались при вводе нуля в примерах на деление выше мы получим
# ошибку. Это ZeroDivisionError: division by zero.
# Вспомним высшую математику, а именно то, что при делении любого числа на ноль
# получаем бесконечность.


def hundred_div_num(text: str = None) -> tuple[int, float]:
    while True:
        try:
            num = int(input(text))
            div = 100 / num
            break
        except ValueError as e:
            print(f'Ваш ввод привёл к ошибке ValueError: {e}\n'
            f'Попробуйте снова')
        except ZeroDivisionError as e:
            div = float('inf')
            break
    return num, div

if __name__ == '__main__':
    n, d = hundred_div_num('Введите целый делитель: ')
    print(f'Результат операции: "100 / {n} = {d}"')


# В приведённом примере блок try обрабатывает сразу несколько строчек, которые
# способны вызвать разные ошибки. Не лучший вариант. Правильнее было бы
# разделить код на отдельные try блоки со своими возможными исключениями. Но
# зато мы познакомились с обработкой нескольких ошибок разом.
# Если не удалось получить целое число, обрабатываем ошибку значения и даём ещё
# один шанс. А если делим на ноль, вместо ошибки возвращаем бесконечность.

# Внимание! Язык Python поддерживает такие математические числа как
# бесконечность и минус бесконечность. Записываются они как особая форма
# вещественного числа:
# ● float(‘inf’) - бесконечность
# ● float(‘-inf’) - минус бесконечность
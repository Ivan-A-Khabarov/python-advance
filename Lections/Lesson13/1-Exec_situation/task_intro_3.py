# Команда try
# Что делать, если мы не хотим завершать программу в случае появления ошибки?
# Команда try позволяет обернуть блок кода с возможной ошибкой и отловить её.
# Поступим так с третьей строкой нашей программы.

# def get(text: str = None) -> int:
#     data = input(text)
#     try:
#         num = int(data)
#     return num
# if __name__ == '__main__':
#     number = get('Введите целый делитель: ')
#     print(f'100 / {number} = {100 / number}')

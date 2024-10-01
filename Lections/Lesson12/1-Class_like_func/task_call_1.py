# 1. Класс как функция
# При желании можно заставить класс, а точнее его экземпляры вести себя как
# функции. После имени экземпляра указываются круглые скобки с параметрами для
# вызова и экземпляр возвращает ответ. Разберём как это работает.

class Number:
    def __init__(self, num):
        self.num = num

n = Number(42)
print(f'{callable(Number) = }')
print(f'{callable(n) = }')

# Класс Number имеет метод инициализации для сохранения числа. Мы создали
# экземпляр класса n и воспользовались встроенной функцией callable. Для класса
# получили истину, для экземпляра ложь. Функция отвечает на вопрос вызываемый
# перед нами объект или нет. Вызов класса возможен. Он запускает инициализацию и
# возвращает экземпляр. Вызвать экземпляр нельзя.

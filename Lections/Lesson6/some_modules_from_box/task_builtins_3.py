# Все описанные функции представлены в листинге ниже.

import random as rnd

print(f'{rnd.random() = }')
rnd.seed(42) # Задаем начальное состояние рандома.
state = rnd.getstate() # Создаем объект состояния рандома.
print(f'{state = }') # Выводим состояние рандома.
print(f'{rnd.random() = }') # Выводим рандом.
print(f'{rnd.random() = }') # Выводим рандом.
rnd.setstate(state) # Восстанавливаем рандом.
print(f'{rnd.random() = }') # Выводим изначельный рандом.
print(f'{rnd.random() = }') # Выводим изначельный рандом.


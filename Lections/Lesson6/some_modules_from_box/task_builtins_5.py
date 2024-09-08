import random as rnd

START = -100
STOP = 1_000
STEP = 10
data = [2, 4, 6, 8, 42, 73]

print(f'{data = }')
rnd.shuffle(data)
print(f'{data = }')
print(f'{rnd.sample(data, 3) = }')
print(f'{rnd.sample(data, 3, counts=[1, 1, 1, 1, 1, 100]) = }')

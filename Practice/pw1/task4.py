# Таблица умножения от 2х2 до 9х10

for i in range(2, 10):
    for j in range(2, 11):
        print(f"{i} x {j} = {i * j}", end="\t")
    print()
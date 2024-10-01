class Fibonacci:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.first = 0
        self.second = 1
    def __iter__(self):
        return self

fib = Fibonacci(20, 100)
for num in fib: # TypeError: iter() returned non-iterator oftype 'Fibonacci'
    print(num)

# две строки метода вернули ссылку на самого себя. В результате получаем новую
# ошибку. Вернулся не итерируемый объект.

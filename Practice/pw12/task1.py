# Задание №1
# Создайте класс-функцию, который считает факториал числа при
# вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и
# их факториалов.



class FactorialTracker:
    def __init__(self,k=None):
        self._factorials = [] if k is None else [0] * k

    def _memoize(self,n):
        if n in self._factorials:
            return self._factorials[n]
        result = 1 if n == 0 or n == 1 else n * self._memoize(n - 1)
        self._factorials.append(result)
        return result

    def factorial(self,n):
        return self._memoize(n)

    def last_values(self):
        return [(i, f) for i,f in enumerate(self._factorials)]

def main():
    tracker = FactorialTracker()
    print("Факториал из 4:", tracker.factorial(4))
    print("Последнее значение:")
    for i,f in tracker.last_values():
        print(f'{i}: {f}')

if __name__ == '__main__':
    main()
    
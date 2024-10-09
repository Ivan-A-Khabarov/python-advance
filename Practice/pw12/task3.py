# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.




class FactorialGenerator:
    def __init__(self, start=1, stop=None, step=1):
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        if not self.stop:
            self.stop = self.start + self.step - 1

        return self

    def __next__(self):
        current = self.start
        while current <= self.stop:
            yield current, self._factorial(current)
            current += self.step

    def _factorial(self, n):
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


# Пример использования
for num, fact in FactorialGenerator(3, 6, 2):
    print(num, fact)

# Если передать только одно число, получим факториалы начиная с него до следующего целого кратного шагу
for num, fact in FactorialGenerator(7):
    print(num, fact)
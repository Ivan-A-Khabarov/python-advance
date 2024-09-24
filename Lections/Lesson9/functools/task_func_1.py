# Декоратор wraps
# Рассмотрим код из прошлой главы, но добавим строку документации в функцию
# factorial.

...
@count(10)
def factorial(n: int) -> int:
    """Returns the factorial of the number n."""
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

print(f'{factorial(1000) = }')
print(f'{factorial.__name__ = }')

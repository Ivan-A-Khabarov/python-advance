import cmath


def solve_quadratic(a, b, c):
    D = b ** 2 - 4 * a * c

    if D >= 0:
        root1 = (-b + cmath.sqrt(D)) / (2 * a)
        root2 = (-b - cmath.sqrt(D)) / (2 * a)
        roots = [root1, root2]
    else:
        root1 = (-b + cmath.sqrt(-D)) / (2 * a)
        root2 = (-b - cmath.sqrt(-D)) / (2 * a)
        roots = [root1, root2]

    return roots


# Пример использования функции
a = 1
b = 5
c = 6
roots = solve_quadratic(a, b, c)
print("Решения уравнения ax^2 + bx + c = 0:")
for root in roots:
    print(f"{root.real:.4f} + {root.imag:+.4f}j")
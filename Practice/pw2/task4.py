# Константа π с точностью до 42 знаков после запятой
PI = 3.14159265358979323846264338327950288419716939937510


def calculate_circle_properties(diameter):
    radius = diameter / 2
    area = PI * (radius ** 2)
    circumference = 2 * PI * radius

    return format(area, '.42f'), format(circumference, '.42f')


if __name__ == "__main__":
    while True:
        try:
            diameter = float(input("Введите диаметр круга: "))
            if diameter <= 0 or diameter > 1000:
                raise ValueError()

            break
        except ValueError as e:
            print("Диаметр должен быть положительным числом меньше 1000.")

    area, circumference = calculate_circle_properties(diameter)
    print(f"Площадь круга: {area}")
    print(f"Длина окружности: {circumference}")
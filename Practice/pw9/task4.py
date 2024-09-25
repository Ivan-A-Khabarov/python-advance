def repeat_decorator(n):
    def decorator(func):
        def wrapped(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapped
    return decorator

# Пример использования декоратора
@repeat_decorator(3)
def greet():
    print("Привет!")

greet()
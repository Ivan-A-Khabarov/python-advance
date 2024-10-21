# Общие моменты работы с pytest.
# Рассмотрим простой пример тестирования работы функции, которая складывает
# два числа.


import pytest

def sum_two_num(a, b):
    return a + b

def test_sum():
    assert sum_two_num(2, 3) == 5, 'Математика покинула чат'

if __name__ == '__main__':
    pytest.main()

# Импорт модуля нужен только для запуска тестов из файла. Для создания
# простейших тестов модуль pytest не нужен.
# Функция sum_two_num наш подопытный. Она принимает пару числе и возвращает
# их сумму.
# Для создания кейса просто определяем функцию, которая начинается со слова test.
# Внутри используем assert для проверки утверждения. В простейшем случае это
# сравнение вызова функции с ожидаемым результатом. Более сложные ассерты
# рассмотрим далее. Дополнительно можно указать сообщение, которое будет
# выведено в случае провала теста.
# Количество функций в файле может быть любым. pytest найдёт и запустит их все на
# основе сопоставления имён. При этом превращать функции в методы класса как в
# unittest не нужно. А если очень хочется объединить кейсы внутри класса, создайте
# класс начинающийся с Test.
# Чтобы запустить тест из файла, вызываем функцию main из модуля pytest.
# 🔥 Внимание! Команда для запуска тестов из командной строки выглядит
# аналогично запуску doctest и unittest. Ключ с одиночным или двойным v
# указывает на уровень детализации. Кроме того можно вызывать pytest
# напрямую.

import pytest

from string import ascii_letters


def check_str(text: str):
    alph = ascii_letters + ' '
    result = ''
    for let in text:
        if let in alph:
            result += let
    return result.lower()


def test_no_change():
    assert check_str('hello') == 'hello', 'Ошибка теста 1'


def test_lower():
    assert check_str('Hello') == 'hello', 'Ошибка теста 2'


def test_no_pucnuation():
    assert check_str('Hello, world!') == 'hello world', 'Ошибка теста 3'


def test_no_another_alphabet():
    assert check_str('Привет, world!') == ' world', 'Ошибка теста 4'


def test_all_cases():
    assert check_str('Привет, World!') == ' world', 'Ошибка теста 5'


if __name__ == '__main__':
    pytest.main()
    print(check_str('Привет hello'))
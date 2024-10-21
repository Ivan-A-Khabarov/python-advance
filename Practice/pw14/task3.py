# Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов
# (кроме п. 1)

from string import ascii_letters
import unittest


def check_str(text: str):
    alph = ascii_letters + ' '
    result = ''
    for let in text:
        if let in alph:
            result += let
    return result.lower()

class TestCheckStr(unittest.TestCase):

    def test_no_change(self):
        self.assertEqual(check_str('hello'), 'hello')

    def test_lower(self):
        self.assertEqual(check_str('Hello'), 'hello')

    def test_no_pucnuation(self):
        self.assertEqual(check_str('Hello, world!'), 'hello world')

    def test_no_another_alphabet(self):
        self.assertEqual(check_str('Привет, world!'), ' world')

    def test_all_cases(self):
        self.assertEqual(' world', check_str('Привет, World!'))


if __name__ == '__main__':
    unittest.main(verbosity=2)
    print(check_str('Привет hello'))
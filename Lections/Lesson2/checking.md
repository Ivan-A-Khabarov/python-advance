
**str.isalnum()** — возвращает True, если все символы в строке буквенно-цифровые. Символ является
буквенно-цифровым, если одно из следующих значений возвращает True: c.isalpha(), c.isdecimal(),
c.isdigit()или c.isnumeric().

**str.isalpha()** — возвращает True, если все символы в строке являются буквенными. Алфавитные
символы — это символы, определенные в базе данных символов Юникода как «буква».

**str.isdecimal()** — возвращает True, если все символы в строке являются десятичными символами

**str.isdigit()** — возвращает True, если все символы в строке являются цифрами. Цифры включают
десятичные символы и цифры, требующие специальной обработки, например цифры надстрочного
индекса совместимости.

**str.isnumeric()** — возвращает True, если все символы в строке являются числовыми символами.
Числовые символы включают цифровые символы и все символы, которые имеют свойство
числового значения Unicode.

**str.isascii()** — возвращает True, если строка пуста или все символы в строке ASCII.

**str.islower()** — возвращает True, если все символы в строке в нижнем регистре.

**str.istitle()** — возвращает True, если строка является строкой с заглавным регистром
и содержит хотя бы один символ.

**str.isupper()** — возвращает True, если все символы в строке в верхнем регистре.

**str.isprintable()** — возвращает True, если все символы в строке доступны для печати или строка пуста.
Непечатаемые символы — это символы, определенные в базе данных символов Unicode как «Другие»
или «Разделители», за исключением пробела ASCII (0x20), который считается печатаемым.

**str.isspace()** — возвращает True, если в строке есть только пробельные символы.
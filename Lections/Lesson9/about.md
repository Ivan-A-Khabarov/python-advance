Краткая выжимка, о чём говорилось
в предыдущей лекции
На прошлой лекции мы:
1. Разобрались в сериализации и десериализации данных
2. Изучили самый популярный формат сериализации — JSON
3. Узнали о чтении и записи таблиц в формате CSV
4. Разобрались с внутренним сериализатором Python — модулем pickle
Термины лекции
● Замыкание (англ. closure) в программировании — функция первого класса,
в теле которой присутствуют ссылки на переменные, объявленные вне тела
этой функции в окружающем коде и не являющиеся её параметрами.
● Декоратор — структурный шаблон проектирования, предназначенный для
динамического подключения дополнительного поведения к объекту.
Подробный текст лекции
1. Что такое замыкания
Прежде чем погрузиться в декораторы поговорим о замыканиях в
программировании вообще и в Python в частности. Плюс стоит вспомнить об
областях видимости в Python.
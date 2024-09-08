## Итераторы
С итераторами мы уже знакомы. Любая Python коллекция будь то список, словарь,
строка и т.п. предоставляют интерфейс итератора. Если коллекцию можно передать
в цикл for in для последовательного перебора элементов, значит коллекция
итерируемая, поддержи вает интерфейс итарации. При этом у каждой коллекции
может быть свой интерфейс. Списки, строки, кортежи возвращают элементы слева
направо, от нулевого индекса к последнему. Множества возвращают элементы в
случайном порядке.

💡 Секрет! На самом деле порядок вывода элементов множества не
случаен. Он зависит от результата работы встроенного хэша. Хэш функция
определяет в какое место множества будет помещён элемент и возвращает их
в порядке возрастания хеша.
Просто этот порядок может не совпадать со значением элементов.
Что касается словарей, они поддерживают сразу три интерфейса итерации: по
ключам, по значениям и по парам ключ-значение. Вспомните методы keys, values и
items.
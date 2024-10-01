# На прошлой лекции мы работали с классом треугольник и пометили его свойства
# защищёнными, добавив символ подчёркивания в начале имени. Но что если доступ
# к свойству нужен. Хотя бы на чтение. Для этого отлично подойдёт функция
# декоратор property(). Рассмотрим на более простом и коротком примере.

class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

user = User('Стивен')
print(f'{user.name = }')
user.name = 'Славик'  # AttributeError: can't set attribute 'name'

# Класс User получает имя пользователя и сохраняет его в защищённой переменной
# экземпляра _name.
# Далее создали метод name который возвращает значение из защищённого
# свойства _name. К методу применён декоратор property. Теперь Python
# воспринимает name не как имя вызываемого метода, а как название свойства.
# При обращении к свойству name получаем результат — имя пользователя. Если же
# сделать попытку на изменение свойства, получим ошибку
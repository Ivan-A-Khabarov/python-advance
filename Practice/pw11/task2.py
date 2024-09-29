# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

class Archive:
    def __init__(self):
        self.archives = []  # список архивов

    # метод для добавления нового элемента в список архивов
    def add_element(self, num, string):
        archive = [num, string]
        self.archives.append(archive)

    # методы для получения элементов списка архивов по индексу
    def get_num_by_index(self, index):
        return self.archives[index][0]

    def get_string_by_index(self, index):
        return self.archives[index][1]

    # метод для вывода всех элементов списка архивов
    def print_archives(self):
        for archive in self.archives:
            print(f"{archive[0]} - {archive[1]}")

archive = Archive()
archive.add_element(1, "Первая строка")
archive.add_element(2, "Вторая строка")

print(archive.get_num_by_index(0))  # 1
print(archive.get_string_by_index(1))  # Вторая строка
archive.print_archives()  # Первая строка - 1
                          # Вторая строка - 2

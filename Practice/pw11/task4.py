class Archive:
    """Класс для хранения пар свойств (число и строка).

    Старые данные из ранее созданных экземпляров сохраняются в список архивов,
    который является свойством экземпляра.
    """

    def __init__(self):
        self.archives = []  # список архивов

    # метод для добавления нового элемента в список архивов
    def add_element(self, num, string):
        archive = [num, string]
        self.archives.append(archive)

    # методы для получения элементов списка архивов по индексу
    def get_num_by_index(self, index):
        """Возвращает число из элемента списка архивов с указанным индексом."""
        return self.archives[index][0]

    def get_string_by_index(self, index):
        """Возвращает строку из элемента списка архивов с указанным индексом."""
        return self.archives[index][1]

    # метод для вывода всех элементов списка архивов
    def print_archives(self):
        for archive in self.archives:
            print(f"{archive[0]} - {archive[1]}")

    # Метод представления экземпляра для программиста
    def as_dict(self):
        return {"архивы": self.archives}

    # Метод представления экземпляра для пользователя
    def pretty_print(self):
        print("Число\tСтрока")
        for num, string in self.archives:
            print(num, "\t", string)

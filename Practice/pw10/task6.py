class Animal:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Name: {self.name}")


class Fish(Animal):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    def swim(self):
        print("Swimming gracefully in the water.")

    def eat(self):
        print(f"Eating plankton or small fish.")

    def show_info(self):
        super().show_info()
        print(f"Length: {self.length} cm")


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def fly(self):
        print("Soaring through the sky.")

    def sing(self):
        print("Making a beautiful song.")

    def show_info(self):
        super().show_info()
        print(f"Wingspan: {self.wingspan} cm")


class Reptile(Animal):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    def slither(self):
        print("Sliding silently on its belly.")

    def bask(self):
        print("Laying out to absorb some sunlight.")

    def show_info(self):
        super().show_info()
        print(f"Length: {self.length} cm")


# Создаем экземпляры животных
fish = Fish('Golden Trout', '30 cm')
bird = Bird('Hummingbird', '7 cm')
reptile = Reptile('Komodo Dragon', '3 m')

# Вызываем специфичные методы для каждого класса
fish.swim()
fish.eat()
fish.show_info()

bird.fly()
bird.sing()
bird.show_info()

reptile.slither()
reptile.bask()
reptile.show_info()
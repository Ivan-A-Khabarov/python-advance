class Fish:
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def swim(self):
        print("Swimming gracefully in the water.")

    def eat(self):
        print(f"Eating plankton or small fish.")


class Bird:
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan

    def fly(self):
        print("Soaring through the sky.")

    def sing(self):
        print("Making a beautiful song.")


class Reptile:
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def slither(self):
        print("Sliding silently on its belly.")

    def bask(self):
        print("Laying out to absorb some sunlight.")


# Создаем экземпляры животных
fish = Fish('Golden Trout', '30 cm')
bird = Bird('Hummingbird', '7 cm')
reptile = Reptile('Komodo Dragon', '3 m')

# Вызываем специфичные методы для каждого класса
fish.swim()
fish.eat()

bird.fly()
bird.sing()

reptile.slither()
reptile.bask()
class Animal:

    def __init__(self, name):
        self.name = name
        self.energy = 100

    @property
    def is_alive(self):
        return self.energy > 0

    def move(self, distance):
        self.energy -= 0.1 * distance
        if self.is_alive:
            return distance
        return self.is_alive

    def eat(self, calories):
        self.energy += 0.2 * calories

    def sound(self):
        print("Make noise:")

class Dog(Animal):

    def __init__(self, name, species):
        # super().__init__(name)
        # Animal.__init__(self, name)
        super(Dog, self).__init__(name)
        self.species = species

    def eat(self, calories):
        super().eat(calories)

        self.energy -= 10

    def bark(self):
        super().sound()
        print("How How")
        self.energy -= 0.01


a = Animal("Zenek")
azor = Dog("Azor", "owczarek niemiecki")

print(azor.move(100))
print(azor.bark())
print(azor.energy)
# print(a.bark())
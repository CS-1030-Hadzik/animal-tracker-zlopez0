from animal import Animal
# Inheritance - 

# child class or derived class
class bird(Animal):
    """
    Derived class representing a bird, which is a type of Animal.
    """
    def __init__(self, name, bird, eats):
        super().__init__(name, bird)
        self.eats = eats

    def speak(self):
        print(f"{self.name} chirps")

    def __str__(self):
        return super().__str__() + f"Eats: {self.eats}\n"
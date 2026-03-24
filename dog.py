from animal import Animal
# Inheritance - 

# child class or derived class
class Dog(Animal):
    """
    Derived class representing a dog, which is a type of Animal.
    """
    def __init__(self, name, species, size):
        super().__init__(name, species)
        self.size = size

    def speak(self):
        print(f"{self.name} woofs")

    def __str__(self):
        return super().__str__() + f"Size: {self.size}\n"

    # TODO: Initialize the Dog class and add the breed attribute.
    # The constructor should accept name, species, and breed as parameters.
    
    # TODO: Override the __str__ method to include the breed.
    # Example output:
    # Kingdom: 'kingdom attribute', Name: 'name attribute', Species: 'species attribute', Breed: 'breed attribute'
    
    # TODO: Add a method for the dog to make a specific sound. 
    # Call the method `speak` and make it output a specific message like 
    # "The dog barks.
class Animal:
    """
    Base class representing a generic animal. Parent Class. Highest Level
    """
    # Class-level attribute
    kingdom = "Animalia"
    # TODO create a class-level attribute that is a list of all the Animal objects
        # name = describe the animal
        # species = describe the species
    
    def __init__(self, name, species): 
        self.name = name
        self.species = species

    def speak(self):
        print("The animal makes a noise")
    
    def __str__(self):
        return f"Kingdom: {self.kingdom}\n Name: {self.name}\n Species: {self.species}\n"

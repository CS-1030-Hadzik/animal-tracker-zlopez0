class Animal:
    """
    Base class representing a generic animal. Parent Class. Highest Level
    """
    # Class-level attribute
    kingdom = "Animalia"
    
    # object specific attributes
    # Constructor -- initializer
    # dunder init magic method
    def __init__(self, name, species): 
        self.name = name
        self.species = species

    # class method
    def speak(self): # pass self error methods 0 arguments expected 1
        print("The animal makes a noise")
    
    # overiding the print function
    def __str__(self):
        return f"Kingdom: {self.kingdom}\n Name: {self.name}\n Species: {self.species}\n"

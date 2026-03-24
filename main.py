from animal import Animal
from dog import Dog
from bird import bird

if __name__ == "__main__":
    # TODO: Create an instance of the Animal class
    # instance of the animal class -- instatiation
    # the object
    animal1 = Animal("Gus", "Mouse") # object -- instance of the animal class -- instanciation
    dog2 = Dog("Nala", "canine", "medium")
    bird1 = bird("hummingbird", "bird", "nectar" )
    print(animal1)
    print(dog2)
    print(bird1)
    
    animal1.speak()
    dog2.speak()
    bird1.speak()



    # TODO: Create an instance of the Dog class
    # TODO: Print the Dog instance
    # TODO: Call the method to make the dog-specific sound

    # TODO print out all the animals

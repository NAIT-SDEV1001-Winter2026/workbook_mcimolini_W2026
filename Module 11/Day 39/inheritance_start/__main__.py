from animals import Animal, Dog, Cat

def main():
    # Create some animals
    dog = Dog("Trigger", "Brown", 4, "Labrador Retriever")
    cat = Cat("Scout", "Black", 4, "Tabby")
    bird = Animal("Tweety", "Yellow", 2)

    # Make a list
    animals = [dog, cat, bird]

    # Loop through our list
    for animal in animals:
        print("--------------------")
        print(animal) # calls __str__

        animal.make_a_noise()
        animal.move()
        animal.eat()
        #animal.chase_tail() # this won't work for our non-Dog Animals.

        # If I want to do things only some of the child classes know how to do, I need to be specific
        if isinstance(animal, Dog): # if my current instance of animal is actually a Dog
            animal.chase_tail()
        elif isinstance(animal, Cat):
            animal.anger_level = 20
            animal.be_a_jerk()
            animal.make_a_noise()
        print("--------------------")

if __name__ == "__main__":
    main()
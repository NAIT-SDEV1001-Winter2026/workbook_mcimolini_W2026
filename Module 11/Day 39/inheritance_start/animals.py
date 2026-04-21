# parent class
class Animal:
    def __init__(self, name, color, num_legs):
        self.name = name
        self.color = color
        self.num_legs = num_legs

    def __str__(self):
        return f"Name: {self.name} \nColor: {self.color} \nNumber of Legs: {self.num_legs}"
    
    def __repr__(self):
        return __str__()
    
    def eat(self):
        print(f"{self.name} starts eating.")
    
    def make_a_noise(self):
        print(f"{self.name} makes a noise.")

    def move(self):
        print(f"{self.name} runs around.")

# The classes in the brackets tell us what classes our child object inherits from. We can have multiple
class Dog(Animal):
    def __init__(self, name, color, num_legs, breed): # Added an extra parameter
        # let's call the parent constructor w/ super
        super().__init__(name, color, num_legs)
        self.breed = breed # specific to this child class

    # Can override any of our methods from the parent
    def __str__(self):
        return_string = super().__str__()

        return_string += f"\nBreed: {self.breed}"

        return return_string
    
    # Don't need to call super if we're not using anything from the parent
    def make_a_noise(self):
        print(f"{self.name} starts barking loudly!")

    # Children can have their own methods not present in the parent
    def chase_tail(self):
        print(f"{self.name} chases their tail.")

class Cat(Animal):
    def __init__(self, name, color, num_legs, pattern):
        super().__init__(name, color, num_legs)
        self.pattern = pattern
        self.anger_level = 5

    def __str__(self):
        return(super().__str__() + f"\nPattern: {self.pattern} \nAnger: {self.anger_level}")
    
    def make_a_noise(self):
        if(self.anger_level < 10):
            print(f"{self.name} purs.")
        elif(self.anger_level < 20):
            print(f"{self.name} meows.")
        else:
            print(f"{self.name} hisses!")
    
    def be_a_jerk(self):
        print(f"{self.name} knocks things off a ledge.")
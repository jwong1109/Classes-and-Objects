class Dog:
    def __init__(self, name, age, colour, danger):  # the self parameter
        # (e.g. dog1 or dog2) is automatically passed to the dog class
        # - so that we know which dog we're talking about

        self.name = name  # Creates a 'name' attribute for Dog
        self.age = age  # Creates a 'age' attribute for Dog
        self.colour = colour  # Creates a 'colour' attribute for Dog
        self.danger = danger

    def print_details(self):  # Creates a method of displaying information
        return f"{self.name} is a " \
               f"{self.danger} {self.colour} dog aged {self.age}"

    def change_age(self, age):
        self.age = age

    def change_colour(self, colour):
        self.colour = colour

    def age_days(self):
        return f"{self.name} is {self.age * 5.75} dog years old"


# These are two different Dog objects
dog1 = Dog("Spot", 7, "black", "savage")
dog2 = Dog("Jazz", 5, "white", "playful")
dog3 = Dog("Boss", 9, "ginger", "biting")

# Calling the printDetails method for each dog object
print(Dog.print_details(dog1))
print(Dog.print_details(dog2))
print(Dog.print_details(dog3))

# Changing the age of the dogs using a method from within the Dog class
dog1.change_age(17)
dog2.change_age(9)

# Calling the printDetails method for each dog object to confirm change
print()
print(Dog.print_details(dog1))
print(Dog.print_details(dog2))
print(Dog.print_details(dog3))

# Changing the colour of the dogs using a method from within the Dog class
dog1.change_colour("red")
dog2.change_colour("green")

# Calling the printDetails method for each dog object to confirm change
print()
print(Dog.print_details(dog1))
print(Dog.print_details(dog2))
print(Dog.print_details(dog3))

print()
print(Dog.age_days(dog1))
print(Dog.age_days(dog2))
print(Dog.age_days(dog3))

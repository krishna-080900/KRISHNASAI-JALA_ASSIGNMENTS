#10.1  Create a constructor and a method for each class

class Car:
    def __init__(self, make, model, year, color):
        # Constructor to initialize the car attributes
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        # Method to describe the car being driven
        return f"The {self.year} {self.color} {self.make} {self.model} is now driving."

# Create a car instance
my_car = Car("Audi", "Q7", 2024, "Black")
print(my_car.drive())  # Calling the method

class Person:
    def __init__(self, name, age, gender):
        # Constructor to initialize the person's attributes
        self.name = name
        self.age = age
        self.gender = gender

    def drive_car(self, car):
        # Method to describe the person driving the car
        return f"{self.name}, who is {self.age} years old, is driving the {car.year} {car.color} {car.make}."

# Create a person instance
person = Person("krishna", 24, "male")
print(person.drive_car(my_car))  # Calling the method to drive the car

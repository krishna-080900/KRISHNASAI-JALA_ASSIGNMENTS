#9.2 Create a sub class for an abstract class. Create an object in the child class for the abstract class and access the non-abstract methods

from abc import ABC, abstractmethod


class Animal(ABC):
    # Non-abstract method
    def speak(self):
        print("The animal makes a sound.")

    # Abstract method (to be implemented by subclass)
    @abstractmethod
    def move(self):
        pass

class Dog(Animal):
    # Implementing the abstract method from the Animal class
    def move(self):
        print("The dog runs.")

# Create an object of the Dog class
dog = Dog()

# Access the non-abstract method speak() from the parent class
dog.speak()  # Output: The animal makes a sound.

# Access the implemented abstract method move() from the child class
dog.move()  # Output: The dog runs.

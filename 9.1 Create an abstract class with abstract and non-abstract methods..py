#9.1 Create an abstract class with abstract and non-abstract methods.

from abc import ABC, abstractmethod


class Shape(ABC):

    # Abstract method (must be implemented by subclasses)
    @abstractmethod
    def area(self):
        pass

    # Non-abstract method (can have an implementation)
    def description(self):
        return "This is a shape."


# Example subclass that implements the abstract method
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)


# Example usage
circle = Circle(5)
print(circle.description())  # Calls the non-abstract method
print(f"Area of the circle: {circle.area()}")  # Calls the abstract method implementation

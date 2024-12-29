#9.4 Create an instance for the child class in child class and call non-abstract methods

from abc import ABC, abstractmethod


# Step 1: Define an abstract base class
class BaseClass(ABC):

    @abstractmethod
    def abstract_method(self):
        pass

    def non_abstract_method(self):
        print("This is a non-abstract method in the base class.")


# Step 2: Define a child class that inherits from the base class
class ChildClass(BaseClass):

    # Implement the abstract method
    def abstract_method(self):
        print("Implemented abstract method in the child class.")

    # A method inside the child class that creates an instance of itself
    def create_instance_and_call_methods(self):
        print("Creating an instance of the child class inside itself.")

        # Create an instance of the child class
        child_instance = ChildClass()

        # Call the non-abstract method from the base class
        child_instance.non_abstract_method()

        # Call the abstract method, which is implemented in the child class
        child_instance.abstract_method()


# Step 3: Create an instance of the child class and call the method
child = ChildClass()
child.create_instance_and_call_methods()

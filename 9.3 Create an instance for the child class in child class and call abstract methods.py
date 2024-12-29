#9.3 Create an instance for the child class in child class and call abstract methods

from abc import ABC, abstractmethod


# Step 1: Create an abstract class
class MyAbstractClass(ABC):

    @abstractmethod
    def abstract_method(self):
        pass


# Step 2: Create a child class that implements the abstract method
class MyChildClass(MyAbstractClass):

    def abstract_method(self):
        print("Abstract method implemented in MyChildClass!")

    def create_instance_and_call(self):
        # Creating an instance of the child class inside the child class
        instance = MyChildClass()

        # Calling the abstract method through the instance
        instance.abstract_method()


# Step 3: Instantiate the child class and call the method to see the result
child_instance = MyChildClass()
child_instance.create_instance_and_call()

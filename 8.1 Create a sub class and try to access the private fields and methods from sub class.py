#8.1 Create a class with PRIVATE fields, private method and a main method. Print the fields in main method. Call the private method in main method.
#Create a sub class and try to access the private fields and methods from sub class.

class Parent:
    # Private fields
    __private_field1 = "This is private field 1"
    __private_field2 = "This is private field 2"

    # Private method
    def __private_method(self):
        return "This is a private method"

    # Public method to access private fields and methods
    def public_method(self):
        return self.__private_method()

    # Main method
    @staticmethod
    def main():
        # Creating an instance of the Parent class
        parent = Parent()

        # Accessing private fields using getter method
        print(parent.__private_field1)  # This will cause an AttributeError
        print(parent.__private_field2)  # This will also cause an AttributeError

        # Calling the private method using the public method
        print(parent.public_method())  # This will print the output of the private method

# Creating a subclass
class SubClass(Parent):
    def try_to_access_private(self):
        # Attempting to access private fields from the parent class
        try:
            print(self.__private_field1)  # Will raise an AttributeError
        except AttributeError:
            print("Cannot access private_field1 from subclass")

        try:
            print(self.__private_field2)  # Will raise an AttributeError
        except AttributeError:
            print("Cannot access private_field2 from subclass")

        # Attempting to call private method from the subclass
        try:
            print(self.__private_method())  # Will raise an AttributeError
        except AttributeError:
            print("Cannot access __private_method from subclass")


# Run the main method
Parent.main()

# Creating an instance of SubClass and attempting to access private members
subclass_instance = SubClass()
subclass_instance.try_to_access_private()

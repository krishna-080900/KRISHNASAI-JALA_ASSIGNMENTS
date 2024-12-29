#12.1 Write a class with a default constructor, one argument constructor and two argument constructors. Instantiate the class to call all the constructors of that class from a main class

class MyClass:
    # Default constructor
    def __init__(self):
        self.name = "Default Name"
        self.age = 0
        print(f"Default Constructor called: Name = {self.name}, Age = {self.age}")

    # One-argument constructor
    def __init__(self, name):
        self.name = name
        self.age = 0
        print(f"One-Argument Constructor called: Name = {self.name}, Age = {self.age}")

    # Two-argument constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Two-Argument Constructor called: Name = {self.name}, Age = {self.age}")


# Main class
class MainClass:
    def __init__(self):
        # Calling all constructors from MyClass
        print("Calling Default Constructor:")
        obj1 = MyClass("Default",0)  # Default constructor

        print("\nCalling One-Argument Constructor:")
        obj2 = MyClass("krishna",24)  # One-argument constructor

        print("\nCalling Two-Argument Constructor:")
        obj3 = MyClass("apoo", 25)  # Two-argument constructor


# Instantiate MainClass to call all constructors
if __name__ == "__main__":
    main_obj = MainClass()





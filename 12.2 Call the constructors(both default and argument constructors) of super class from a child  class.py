#12.2 Call the constructors(both default and argument constructors) of super class from a child class

# Superclass
class Parent:
    # Default constructor
    def __init__(self):
        self.name = "Default Name"
        self.age = 0
        print(f"Parent Default Constructor called: Name = {self.name}, Age = {self.age}")

    # One-argument constructor
    def __init__(self, name):
        self.name = name
        self.age = 0
        print(f"Parent One-Argument Constructor called: Name = {self.name}, Age = {self.age}")

    # Two-argument constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Parent Two-Argument Constructor called: Name = {self.name}, Age = {self.age}")


# Child class
class Child(Parent):
    # Default constructor
    def __init__(self):
        # Call the parent class's default constructor
        super().__init__()
        print("Child Default Constructor called")

    # One-argument constructor
    def __init__(self, name):
        # Call the parent class's one-argument constructor
        super().__init__(name)
        print(f"Child One-Argument Constructor called with Name: {name}")

    # Two-argument constructor
    def __init__(self, name, age):
        # Call the parent class's two-argument constructor
        super().__init__(name, age)
        print(f"Child Two-Argument Constructor called with Name: {name} and Age: {age}")


# Main class to instantiate and call constructors
class MainClass:
    def __init__(self):
        # Calling all constructors from Child class
        print("Calling Default Constructor from Child:")
        child1 = Child("Default",0)  # Default constructor

        print("\nCalling One-Argument Constructor from Child:")
        child2 = Child("John",24)  # One-argument constructor

        print("\nCalling Two-Argument Constructor from Child:")
        child3 = Child("Krishna", 25)  # Two-argument constructor


# Instantiate MainClass to call constructors
if __name__ == "__main__":
    main_obj = MainClass()

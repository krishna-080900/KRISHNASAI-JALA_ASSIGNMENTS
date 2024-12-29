#12.3 Apply private, public, protected and default access modifiers to the constructor

# Superclass (Parent class)
class Parent:
    # Public constructor
    def __init__(self, name="Default Name", age=0):
        self.name = name  # Public member
        self.age = age  # Public member
        print(f"Parent Constructor called: Name = {self.name}, Age = {self.age}")

    # Protected constructor (for the sake of illustration)
    def _protected_constructor(self, name, age):
        self._name = name  # Protected member (single underscore)
        self._age = age  # Protected member (single underscore)
        print(f"Parent Protected Constructor called: Name = {self._name}, Age = {self._age}")

    # Private constructor (for the sake of illustration)
    def __private_constructor(self, name, age):
        self.__name = name  # Private member (double underscore)
        self.__age = age  # Private member (double underscore)
        print(f"Parent Private Constructor called: Name = {self.__name}, Age = {self.__age}")


# Child class
class Child(Parent):
    def __init__(self, name, age):
        # Calling public constructor from the Parent class
        super().__init__(name, age)
        print("Child Constructor called")

        # Calling protected constructor from the Parent class (demonstration)
        self._protected_constructor(name, age)
        print("Child Called Protected Constructor")

        # The following line will raise an error because private constructors cannot be accessed outside the class.
        # Uncommenting the line below will cause an AttributeError
        # self.__private_constructor(name, age)

    def display(self):
        # Demonstrating access to public, protected, and private members
        print(f"Public Name: {self.name}, Public Age: {self.age}")
        print(f"Protected Name: {self._name}, Protected Age: {self._age}")
        # Private members are not directly accessible, so the following line will cause an error if uncommented:
        # print(f"Private Name: {self.__name}, Private Age: {self.__age}")


# Main class
class MainClass:
    def __init__(self):
        # Calling constructors from Child class
        print("Calling Constructor from Child class:")
        child1 = Child("Krishna", 24)  # Call to the child constructor

        print("\nTrying to display data from Child class:")
        child1.display()


# Instantiate MainClass to call constructors
if __name__ == "__main__":
    main_obj = MainClass()

#5.7 Call static methods and instance methods in main method

class MyClass:
    # Static variable
    static_var = 10

    def __init__(self):
        # Instance variables
        self.instance_var1 = 20
        self.instance_var2 = "Hello"

    # Static method
    @staticmethod
    def static_method():
        print("This is a static method.")

    # Instance method
    def instance_method(self):
        print(f"This is an instance method. Instance variables: {self.instance_var1}, {self.instance_var2}")

    @staticmethod
    def print_variables():
        # Printing static variable
        print("Static variable:", MyClass.static_var)

        # Printing instance variables by creating an instance
        obj = MyClass()

        print("Instance variables:")
        for attribute, value in vars(obj).items():
            print(f"{attribute}: {value}")


# Main method
if __name__ == "__main__":
    # Calling static method using the class name
    MyClass.static_method()

    # Creating an instance to call instance method
    obj = MyClass()
    obj.instance_method()

    # Calling the print_variables method
    MyClass.print_variables()

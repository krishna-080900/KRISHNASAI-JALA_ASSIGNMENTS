#5.6 Print all the static, instance variables in main method

class MyClass:
    # Static variable
    static_var = 10

    def __init__(self):
        # Instance variables
        self.instance_var1 = 20
        self.instance_var2 = "Hello"

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
    MyClass.print_variables()

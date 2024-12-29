#5.5 Call static methods in instance methods

class MyClass:
    # Static variables
    static_var1 = 0
    static_var2 = "Hello, world!"

    # Instance variables
    def __init__(self, instance_var1, instance_var2):
        self.instance_var1 = instance_var1
        self.instance_var2 = instance_var2

    # Static methods
    @staticmethod
    def static_method1():
        print(f"Static Method 1: static_var1 = {MyClass.static_var1}")

    @staticmethod
    def static_method2():
        print(f"Static Method 2: static_var2 = {MyClass.static_var2}")

    # Instance methods
    def instance_method1(self):
        # Calling static methods from instance methods
        print("Instance Method 1: Calling static_method1()")
        MyClass.static_method1()  # Calling static method using the class name

    def instance_method2(self):
        # Calling static methods from instance methods
        print("Instance Method 2: Calling static_method2()")
        MyClass.static_method2()  # Calling static method using the class name

    # Main method
    @staticmethod
    def main():
        # Create an instance of MyClass
        obj = MyClass(10, "Python")

        # Call instance methods that invoke static methods
        obj.instance_method1()
        obj.instance_method2()

        # Modify static variables
        MyClass.static_var1 = 100
        MyClass.static_var2 = "Updated Hello!"

        # Call instance methods again to see the updated static variables
        obj.instance_method1()
        obj.instance_method2()


# Calling the main method to execute the program
if __name__ == "__main__":
    MyClass.main()

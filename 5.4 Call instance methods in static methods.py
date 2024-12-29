#5.4 Call instance methods in static methods

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
    def static_method1(obj):
        # Calling an instance method from a static method
        print(f"Static Method 1: Calling instance_method1()")
        obj.instance_method1()

    @staticmethod
    def static_method2(obj):
        # Calling an instance method from a static method
        print(f"Static Method 2: Calling instance_method2()")
        obj.instance_method2()

    # Instance methods
    def instance_method1(self):
        # Accessing static variables in instance method
        print(f"Instance Method 1: static_var1 = {MyClass.static_var1}, instance_var1 = {self.instance_var1}")

    def instance_method2(self):
        # Accessing static variables in instance method
        print(f"Instance Method 2: static_var2 = {MyClass.static_var2}, instance_var2 = {self.instance_var2}")

    # Main method
    @staticmethod
    def main():
        # Create an instance of MyClass
        obj = MyClass(10, "Python")

        # Call static methods that invoke instance methods
        MyClass.static_method1(obj)
        MyClass.static_method2(obj)

        # Modify static variables
        MyClass.static_var1 = 100
        MyClass.static_var2 = "Updated Hello!"

        # Call static methods again to see the updated static variables
        MyClass.static_method1(obj)
        MyClass.static_method2(obj)


# Calling the main method to execute the program
if __name__ == "__main__":
    MyClass.main()

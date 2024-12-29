#5.1 Write a class with 2 static variables, 2 Instance variables, 2 static methods, 2 instance  methods and a main method.

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
        print(f"Instance Method 1: instance_var1 = {self.instance_var1}")

    def instance_method2(self):
        print(f"Instance Method 2: instance_var2 = {self.instance_var2}")

    # Main method
    @staticmethod
    def main():
        # Access static methods
        MyClass.static_method1()
        MyClass.static_method2()

        # Create an instance of MyClass and access instance methods
        obj = MyClass(10, "Python")
        obj.instance_method1()
        obj.instance_method2()

        # Modify static variables
        MyClass.static_var1 = 100
        MyClass.static_var2 = "Updated Hello!"

        # Access modified static methods
        MyClass.static_method1()
        MyClass.static_method2()


# Calling the main method to execute the program
if __name__ == "__main__":
    MyClass.main()

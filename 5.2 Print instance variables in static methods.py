#5.2 Print instance variables in static methods

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
        # Accessing instance variables through the instance object
        print(f"Static Method 1: instance_var1 = {obj.instance_var1}")

    @staticmethod
    def static_method2(obj):
        # Accessing instance variables through the instance object
        print(f"Static Method 2: instance_var2 = {obj.instance_var2}")

    # Instance methods
    def instance_method1(self):
        print(f"Instance Method 1: instance_var1 = {self.instance_var1}")

    def instance_method2(self):
        print(f"Instance Method 2: instance_var2 = {self.instance_var2}")

    # Main method
    @staticmethod
    def main():
        # Access static methods (with instance passed)
        obj = MyClass(10, "Python")
        MyClass.static_method1(obj)
        MyClass.static_method2(obj)

        # Create another instance of MyClass and access instance methods
        obj2 = MyClass(20, "Java")
        obj2.instance_method1()
        obj2.instance_method2()


# Calling the main method to execute the program
if __name__ == "__main__":
    MyClass.main()

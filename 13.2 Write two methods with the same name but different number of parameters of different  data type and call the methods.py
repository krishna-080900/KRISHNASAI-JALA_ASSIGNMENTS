#13.2 Write two methods with the same name but different number of parameters of different data type and call the methods

class MethodOverloadingExample:

    # Method with one parameter
    def display(self, *args):
        if len(args) == 1 and isinstance(args[0], int):
            print(f"Integer value: {args[0]}")
        elif len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], float):
            print(f"String value: {args[0]}, Double value: {args[1]}")
        else:
            print("Invalid arguments")


# Create an instance of the class
obj = MethodOverloadingExample()

# Calling the first version of the method (with an integer parameter)
obj.display(10)

# Calling the second version of the method (with a string and a float parameter)
obj.display("Hi", 25.5)

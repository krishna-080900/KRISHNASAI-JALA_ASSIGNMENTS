#13.3 Write two methods with the same name and same number of parameters of same type

class Example:
    # Method with default arguments
    def print(self, a, b, reverse=False):
        if reverse:
            print(f"b: {b}, a: {a}")
        else:
            print(f"a: {a}, b: {b}")

# Create an object of Example
obj = Example()

# Calling the method without 'reverse'
obj.print(1, 2)  # Output: a: 1, b: 2

# Calling the method with 'reverse' argument
obj.print(1, 2, reverse=True)  # Output: b: 2, a: 1

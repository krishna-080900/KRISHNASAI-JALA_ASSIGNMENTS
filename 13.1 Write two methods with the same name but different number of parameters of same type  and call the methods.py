#13.1 Write two methods with the same name but different number of parameters of same type and call the methods

def display(*args):
    if len(args) == 1:
        print(f"Method with one parameter: {args[0]}")
    elif len(args) == 2:
        print(f"Method with two parameters: {args[0]}, {args[1]}")
    else:
        print("Invalid number of parameters")

# Calling the method with one parameter
display(5)

# Calling the method with two parameters
display(10, 20)

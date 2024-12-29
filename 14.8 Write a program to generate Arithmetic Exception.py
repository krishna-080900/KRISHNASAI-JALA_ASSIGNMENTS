#14.8 Write a program to generate Arithmetic Exception

# Function to generate an arithmetic exception
# Function to generate an arithmetic exception
def generate_arithmetic_exception():
    try:
        # Trying to divide by zero to generate an ArithmeticError
        result = 10 / 0  # This will raise a ZeroDivisionError
    except ZeroDivisionError as e:
        # Catching the specific exception
        print(f"Caught an exception: {e}")

# Example usage
generate_arithmetic_exception()

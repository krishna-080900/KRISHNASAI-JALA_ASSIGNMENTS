#14.7 Write a program with finally block

def divide_numbers(a, b):
    try:
        result = a / b  # Try to divide the numbers
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero!")
    else:
        print(f"Result: {result}")
    finally:
        print("This block will always execute, regardless of success or failure.")

# Example usage
divide_numbers(10, 2)  # This will not raise an exception
print("---")
divide_numbers(10, 0)  # This will raise a ZeroDivisionError

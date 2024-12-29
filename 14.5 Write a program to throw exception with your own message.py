#14.5 Write a program to throw exception with your own message

# Define a function that raises an exception with a custom message
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or older. Provided age: {}".format(age))
    else:
        print("Age is valid.")

# Example usage
try:
    check_age(15)  # This will raise an exception
except ValueError as e:
    print("Error:", e)

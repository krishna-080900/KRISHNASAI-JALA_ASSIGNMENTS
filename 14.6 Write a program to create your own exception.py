#14.6 Write a program to create your own exception

# Define a custom exception class
class AgeRestrictionError(Exception):
    def __init__(self, message):
        # Initialize the exception with a custom message
        super().__init__(message)

# Function that checks if the user is old enough
def check_age(age):
    if age < 18:
        # Raise custom exception if age is below 18
        raise AgeRestrictionError(f"Age must be 18 or older. Provided age: {age}")
    else:
        print("Age is valid.")

# Example usage
try:
    check_age(15)  # This will raise the custom exception
except AgeRestrictionError as e:
    print("Caught an exception:", e)

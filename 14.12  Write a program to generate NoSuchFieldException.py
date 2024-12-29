#14.12  Write a program to generate NoSuchFieldException

class MyClass:
    def __init__(self):
        self.existing_field = "This is an existing field"

try:
    # Trying to access a non-existent attribute 'non_existent_field'
    obj = MyClass()
    value = obj.non_existent_field  # This will raise an AttributeError
except AttributeError as e:
    # Catching and printing the AttributeError
    print(f"AttributeError occurred: {e}")

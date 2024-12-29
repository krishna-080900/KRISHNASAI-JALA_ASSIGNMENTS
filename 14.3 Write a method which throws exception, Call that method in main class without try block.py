#14.3 Write a method which throws exception, Call that method in main class without try block

# Method that throws an exception
def throw_exception():
    # This will raise a ZeroDivisionError
    result = 10 / 0

# Main function
def main():
    # Calling the method without try-except block
    throw_exception()

    print("This line will not be executed.")

if __name__ == "__main__":
    main()

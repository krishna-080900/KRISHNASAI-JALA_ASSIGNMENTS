#14.4 Write a program with multiple catch blocks

def multiple_catch_example():
    try:
        # Input from the user
        number = int(input("Enter an integer: "))

        # Division operation (may raise ZeroDivisionError)
        result = 10 / number
        print(f"Result of 10 divided by {number} is: {result}")

        # File handling (may raise FileNotFoundError)
        file_path = input("Enter a file path: ")
        with open(file_path, 'r') as file:
            file_content = file.read()
        print("File content read successfully.")

    except ValueError:
        # Catches invalid input that cannot be converted to an integer
        print("Error: Invalid input! Please enter a valid integer.")

    except ZeroDivisionError:
        # Catches division by zero error
        print("Error: Cannot divide by zero.")

    except FileNotFoundError:
        # Catches file not found error
        print("Error: File not found. Please check the file path.")

    except Exception as e:
        # Catches any other unexpected exceptions
        print(f"An unexpected error occurred: {e}")

    finally:
        print("Execution completed.")


# Calling the function to demonstrate multiple catch blocks
multiple_catch_example()

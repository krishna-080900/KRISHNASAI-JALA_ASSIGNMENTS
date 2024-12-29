#14.9 Write a program to generate FileNotFoundException

try:
    # Attempt to open a file that doesn't exist
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    # Handle the exception and print an error message
    print(f"File not found: {e}")

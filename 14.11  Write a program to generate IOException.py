#14.11  Write a program to generate IOException

try:
    # Attempting to open a non-existent file for reading
    with open('nonexistentfile.txt', 'r') as file:
        file.read()
except OSError as e:
    # Catching and printing the OSError
    print(f"IOException occurred: {e}")

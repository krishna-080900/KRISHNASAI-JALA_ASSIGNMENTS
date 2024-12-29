#11.1 Write a program to read text file

# Define the file path
file_path = 'example.txt'  # Replace with the path to your text file

# Open the file in read mode
try:
    with open(file_path, 'r') as file:
        # Read the content of the file
        content = file.read()
        # Print the content
        print(content)
except FileNotFoundError:
    print(f"The file at {file_path} does not exist.")
except IOError:
    print("An error occurred while trying to read the file.")

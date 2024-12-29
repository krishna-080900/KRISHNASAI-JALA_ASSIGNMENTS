#11.2 Write a program to write text to .txt file using  InputStream

# Open the file in write mode
file_path = 'output.txt'  # Specify your desired file path

# Using input() to simulate InputStream (taking user input)
with open(file_path, 'w') as file:
    print("Enter the text you want to write to the file (type 'exit' to stop):")

    while True:
        # Read input from the user (simulating an InputStream)
        user_input = input()

        # Check if the user wants to stop the input
        if user_input.lower() == 'exit':
            break

        # Write the user input to the file
        file.write(user_input + '\n')

print(f"Text has been written to {file_path}")

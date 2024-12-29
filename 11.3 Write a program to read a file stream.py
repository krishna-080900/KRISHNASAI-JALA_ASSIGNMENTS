#11.3 Write a program to read a file stream

# Open the file in binary or text read mode
file_path = 'example.txt'  # Specify your file path

# Open the file in binary or text read mode
try:
    with open(file_path, 'r') as file:
        # Read the file in chunks
        print("Reading the file content:")
        chunk_size = 1024  # Set the chunk size (in bytes)

        while True:
            # Read a chunk of the file
            chunk = file.read(chunk_size)

            # If chunk is empty, we reached the end of the file
            if not chunk:
                break

            # Print the chunk (or process it as needed)
            print(chunk)
except FileNotFoundError:
    print(f"The file at {file_path} does not exist.")
except IOError as e:
    print(f"An error occurred while reading the file: {e}")

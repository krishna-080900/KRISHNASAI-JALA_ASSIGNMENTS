#11.4 Write a program to read a file stream supports random access

# Function to read a file with random access
def random_access_file(file_path, position, size):
    try:
        # Open the file in binary mode ('rb') to support random access
        with open(file_path, 'rb') as file:
            # Seek to the specified position in the file
            file.seek(position)
            # Read the specified number of bytes from the current position
            data = file.read(size)
            return data
    except Exception as e:
        print(f"Error reading file: {e}")
        return None


# Example usage
if __name__ == "__main__":
    file_path = 'example.txt'  # Specify the path to your file
    position = 10  # The byte position to start reading
    size = 20  # Number of bytes to read from the specified position

    data = random_access_file(file_path, position, size)

    if data is not None:
        print(f"Data read from position {position} to {position + size}:")
        print(data.decode('utf-8', errors='ignore'))  # Decoding bytes to string
    else:
        print("Could not read the file.")

#11.5 Write a program to read a file a just to a particular index using seek()

# Function to read from a file at a particular index using seek()
def read_at_index(file_path, index, size):
    try:
        # Open the file in binary mode ('rb') to support byte-level access
        with open(file_path, 'rb') as file:
            # Seek to the specified index (byte position)
            file.seek(index)

            # Read the specified number of bytes from the index
            data = file.read(size)

            # Return the data read from the file
            return data
    except Exception as e:
        print(f"Error: {e}")
        return None


# Example usage
if __name__ == "__main__":
    file_path = 'example.txt'  # Specify the path to your file
    index = 10  # The byte position to adjust the reading pointer to
    size = 20  # Number of bytes to read after the specified index

    # Call the function to read at the specified index
    data = read_at_index(file_path, index, size)

    if data is not None:
        print(f"Data read from index {index} (size {size}):")
        print(data.decode('utf-8', errors='ignore'))  # Decode bytes to string
    else:
        print("Failed to read data from the file.")

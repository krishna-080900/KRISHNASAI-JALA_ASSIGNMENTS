#11.6 Write a program to check whether a file is having read access and write access permissions

import os


# Function to check read and write access of a file
def check_file_permissions(file_path):
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"The file '{file_path}' does not exist.")
            return

        # Check read access
        can_read = os.access(file_path, os.R_OK)
        # Check write access
        can_write = os.access(file_path, os.W_OK)

        # Display the results
        if can_read:
            print(f"The file '{file_path}' has read access.")
        else:
            print(f"The file '{file_path}' does not have read access.")

        if can_write:
            print(f"The file '{file_path}' has write access.")
        else:
            print(f"The file '{file_path}' does not have write access.")

    except Exception as e:
        print(f"Error: {e}")


# Example usage
if __name__ == "__main__":
    file_path = 'example.txt'  # Specify the path to your file
    check_file_permissions(file_path)

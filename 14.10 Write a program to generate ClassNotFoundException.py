#14.10 Write a program to generate ClassNotFoundException

try:
    # Attempting to import a non-existent module
    __import__('nonexistent_module')
except ImportError as e:
    # Catching and printing the ImportError
    print(f"Module not found: {e}")

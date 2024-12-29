#7.4 Create a class with main method. Create an object for each class A, B and C in main method and call every method of each class using its own object/instance.

class A:
    def method_a(self):
        print("Method A is called")

class B:
    def method_b(self):
        print("Method B is called")

class C:
    def method_c(self):
        print("Method C is called")

def main():
    # Create objects for each class
    a = A()
    b = B()
    c = C()

    # Call methods using the respective objects
    a.method_a()  # Calling method from class A
    b.method_b()  # Calling method from class B
    c.method_c()  # Calling method from class C

# Ensure the main method is called
if __name__ == "__main__":
    main()

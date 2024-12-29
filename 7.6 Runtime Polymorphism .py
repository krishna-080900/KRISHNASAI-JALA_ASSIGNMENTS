#7.6 Runtime Polymorphism with Data Members/Instance variables, Repeat the above process only for data members

class B:
    # Data member in class B
    def __init__(self):
        self.name = "Class B"

class C(B):
    # Overridden data member in class C
    def __init__(self):
        super().__init__()  # Initialize the superclass constructor
        self.name = "Class C"  # Overriding the instance variable

# Creating objects of B and C
objB = B()  # Object of class B
objC = C()  # Object of class C

# Accessing data members
print(objB.name)  # Output: Class B
print(objC.name)  # Output: Class C

# Using superclass reference
objB_ref = B()
objC_ref = C()

# Accessing data members using superclass references
print(objB_ref.name)  # Output: Class B
print(objC_ref.name)  # Output: Class C

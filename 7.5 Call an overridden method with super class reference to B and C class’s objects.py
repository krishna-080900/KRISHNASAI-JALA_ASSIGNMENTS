#7.5 Call an overridden method with super class reference to B and C class’s objects

class B:
    # Method in class B
    def display(self):
        print("Class B display method")

class C(B):
    # Overridden method in class C
    def display(self):
        print("Class C display method")

# Creating objects of B and C
objB = B()  # Object of class B
objC = C()  # Object of class C

# Calling overridden methods
objB.display()  # Output: Class B display method
objC.display()  # Output: Class C display method

# Using superclass reference
objB_ref = B()
objC_ref = C()

# Calling overridden methods using superclass references
objB_ref.display()  # Output: Class B display method
objC_ref.display()  # Output: Class C display method

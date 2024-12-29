#7.1 A, B and C are classes

# Class A (Base Class)
class A:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name} from Class A."


# Class B (Inheriting from A)
class B(A):
    def __init__(self, name, age):
        super().__init__(name)  # Call constructor of class A
        self.age = age

    def greet(self):
        return f"Hello, I am {self.name}, {self.age} years old, from Class B."


# Class C (Inheriting from A)
class C(A):
    def __init__(self, name, country):
        super().__init__(name)  # Call constructor of class A
        self.country = country

    def greet(self):
        return f"Hello, I am {self.name} from {self.country}, and I am from Class C."


# Example Usage:

# Creating an instance of class B
b = B("shanthu", 25)
print(b.greet())  # Output: Hello, I am Alice, 25 years old, from Class B.

# Creating an instance of class C
c = C("apoo", "USA")
print(c.greet())  # Output: Hello, I am Bob from USA, and I am from Class C.

# Creating an instance of class A
a = A("Krishna")
print(a.greet())  # Output: Hello, I am Charlie from Class A.

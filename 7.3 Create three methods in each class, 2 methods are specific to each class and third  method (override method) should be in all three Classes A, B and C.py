#7.3 Create three methods in each class, 2 methods are specific to each class and third  method (override method) should be in all three Classes A, B and C

class A:
    def method1(self):
        print("Method 1 of Class A")

    def method2(self):
        print("Method 2 of Class A")

    def overridden_method(self):
        print("Overridden method in Class A")


class B(A):  # Class B inherits from A
    def method1(self):
        print("Method 1 of Class B")

    def method2(self):
        print("Method 2 of Class B")

    def overridden_method(self):
        print("Overridden method in Class B")


class C(A):  # Class C inherits from A
    def method1(self):
        print("Method 1 of Class C")

    def method2(self):
        print("Method 2 of Class C")

    def overridden_method(self):
        print("Overridden method in Class C")


# Creating objects of each class
a = A()
b = B()
c = C()

# Calling methods from each class
a.method1()  # Calls method1 of Class A
a.method2()  # Calls method2 of Class A
a.overridden_method()  # Calls overridden method of Class A

b.method1()  # Calls method1 of Class B
b.method2()  # Calls method2 of Class B
b.overridden_method()  # Calls overridden method of Class B

c.method1()  # Calls method1 of Class C
c.method2()  # Calls method2 of Class C
c.overridden_method()  # Calls overridden method of Class C



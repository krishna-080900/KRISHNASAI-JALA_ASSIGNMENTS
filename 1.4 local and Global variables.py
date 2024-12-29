# 1.4 Define the local and Global variables with the same name and print both variables and understand the scope of the variables

# Global variable (variables that declares outside the function)
a = 10

def test_scope():
    # Local variable (variable that declares inside a function)
    a = 20
    print("Local variable a :", a)

# Call the function to check the local scope
test_scope()

# Print the global variable outside the function
print("Global variable a :", a)

#14.2 Handle the Arithmetic exception using try-catch block

try:
    # Division by zero will raise a ZeroDivisionError
    result = 9 / 0
    print("Result:", result)
except ZeroDivisionError as e:
    # Catching and handling the exception
    print("Error: Cannot divide by zero!")
    print("Exception message:", e)

#6.8 equalsIgnoreCase(), startsWith(), endsWith() and compareTo()

#equal
string1 = "Hello"
string2 = "hello"

#In python there is no equalIgnoreCase(), but can achieve using the same functionality by using str.lower() or str.casefold() to convert both strings to the same case and then comparing them.
# Using lower() for case-insensitive comparison
print(string1.lower() == string2.lower())  # True

#startswith()
string = "Python is awesome!"

# Checking if the string starts with a specific prefix
print(string.startswith("Python"))
print(string.startswith("Java"))

#endswith()
string = "Python is awesome!"

# Checking if the string ends with a specific suffix
print(string.endswith("awesome!"))
print(string.endswith("is"))


#compareTO()
string1 = "apple"
string2 = "banana"

print(string1 < string2)
print(string1 > string2)
print(string1 == string2)


if string1 < string2:
    print(f"{string1} is  smaller than {string2}")
elif string1 > string2:
    print(f"{string1} is greater than {string2}")
else:
    print(f"{string1} and {string2} are equal")



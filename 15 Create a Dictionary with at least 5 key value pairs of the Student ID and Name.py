# 15 Create a Dictionary with at least 5 key value pairs of the Student ID and Name

#1.1. Adding the values in dictionary
#1.2. Updating the values in dictionary
#1.3. Accessing the value in dictionary
#1.4. Create a nested loop dictionary
#1.5. Access the values of nested loop dictionary
#1.6. Print the keys present in a particular dictionary
#1.7. Delete a value from a dictionary

# Creating a dictionary with 5 key-value pairs
# Creating a dictionary with 5 key-value pairs
students = {
    101: "Krishna",
    102: "Apoo",
    103: "Shanthu",
}

# Adding a new student ID and name
students[104] = "shanthan"

print(students)

# Updating the values in dictionary
# Creating a dictionary with 6 key-value pairs
students = {
    101: "Krishna",
    102: "Apoo",
    103: "Shanthu",
    104: "Shanthan",
}

# Updating the name of the student with ID 102
students[102] = "Kumar"
print(students)

#Accessing the value in dictionary
student_name = students[103]
print(student_name)  # Output will be "Charlie"

#Create a nested loop dictionary
nested_students = {
    101: {"name": "Krishna", "age": 24, "grades": {"math": 85, "english": 90}},
    102: {"name": "Kumar", "age": 23, "grades": {"math": 78, "english": 85}},
    103: {"name": "Shanthu", "age": 21, "grades": {"math": 92, "english": 88}},
    104: {"name": "Shanthan", "age": 23, "grades": {"math": 81, "english": 89}},
}
print(students)

#Access the values of nested loop dictionary
math_grade = nested_students[102]["grades"]["math"]
print(math_grade)  # Output will be 78

#Print the keys present in a particular dictionary
keys = students.keys()
print(keys)  # Output will be dict_keys([101, 102, 103, 104, 105])

# Delete a value from a dictionary
del students[104]
print(students)  # The student with ID 104 will be removed



#3.5 Write a program to print largest number among three numbers

n=[40, 50, 90]


largest = n[0]


for num in n:
    if num > largest:
        largest = num  # Update the largest if a larger number is found

# Print the largest number
print("Largest number is:", largest)

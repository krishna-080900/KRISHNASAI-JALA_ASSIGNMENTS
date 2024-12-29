#4.1 Write a function to add integer values of an array


arr = [10, 20, 30, 40]
total_sum = 0  # Renamed to avoid conflict with the built-in sum function

# Loop through the array to calculate sum of elements
for i in range(0, len(arr)):
    total_sum += arr[i]  # Same as total_sum = total_sum + arr[i]

print("Sum of all integer values in array:", total_sum)

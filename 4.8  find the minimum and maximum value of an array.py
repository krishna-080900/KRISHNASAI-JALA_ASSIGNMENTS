#4.8 Write a function to find the minimum and maximum value of an array

def find_min_max(arr):
    minimum_value = min(arr)
    maximum_value = max(arr)
    return minimum_value, maximum_value

array=[1, 5, 3, 9, 2, 8]

# Find the minimum and maximum values
minimum_val, maximum_val = find_min_max(array)

print("Minimum value:", minimum_val)
print("Maximum value:", maximum_val)

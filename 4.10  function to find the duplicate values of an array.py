#4.10 Write a function to find the duplicate values of an array

array=[11, 22, 33, 44, 33]

# Using a set to track duplicates
seen=set()

for i in range(len(array)):
    if array[i] in seen:
        print("Duplicate element in given array:", array[i])
    else:
        seen.add(array[i])

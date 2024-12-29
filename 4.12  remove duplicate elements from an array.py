#4.12  Write a method to remove duplicate elements from an array

array=[21,11,31,13,11,31,21]
def remove_duplicates(array):
    # Using a set to track seen elements while filtering
    return list(dict.fromkeys(array))

unique_elements=remove_duplicates(array)

print("Arrays after removing duplicates:", unique_elements)

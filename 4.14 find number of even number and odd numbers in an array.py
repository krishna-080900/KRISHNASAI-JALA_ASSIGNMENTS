#4.14 Write a method to find number of even number and odd numbers in an array

array=[11,22,33,44,55,66,77,88,99,110]
evennumbers = 0
oddnumbers  = 0
#using loop to find even and odd numbers in array
for i in array:
    if i % 2==0:
        evennumbers += 1
    else:
        oddnumbers += 1
print("Even Numbers in given array:",evennumbers)
print("Odd Numbers in given array:",oddnumbers)

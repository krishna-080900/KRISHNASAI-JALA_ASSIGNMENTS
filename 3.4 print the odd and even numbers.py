#3.4  Write a program to print the odd and even numbers.
n=[1,2,3,4,5,6,7,8,9,10]
print("Even Numbers: ")  
for i in n:
    if i % 2 == 0:       
        print(i)
print("\nOdd Numbers:")
for i in n:
    if i % 2 != 0:
        print(i)

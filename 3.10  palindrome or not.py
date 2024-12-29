# 3.10 Write a program to palindrome or not

rev=0
n=int(input("enter the value"))
n1=n
while n!=0:
    rev=rev*10+n%10
    n=n//10
if rev==n1:
    print("it is palindrome")
else:
    print(" not a palindrome")
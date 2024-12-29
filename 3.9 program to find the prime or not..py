# 3.9 Write a program to find the prime or not

i=1
fact=0
n=int(input("enter a value"))
while i<=n:
    if n%i==0:
        fact=fact+1
    i=i+1
if fact==2:
    print("it is a prime")
else:
    print("it is not a prime")
# Write a program to find Armstrong number or not


x=0
sum=0
n=int(input("enter a value"))
n1=n
while n!=0:
    x=n%10
    sum=sum+(x*x*x)
    n=n//10
if sum==n1:
    print("it is armstrong no.")
else:
    print("not a armstrong no.")





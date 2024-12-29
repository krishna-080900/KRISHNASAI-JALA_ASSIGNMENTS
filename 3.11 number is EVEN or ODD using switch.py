# 3.11  Program to check whether a number is EVEN or ODD using switch

a=int(input("enter a value"))
switch={
    0:"even",
    1:"odd",
}
if a%2==0:
    print("it is even")
else:
    print("it is odd")
# 3.7 Write a program to print 1 to 10 using the do-while loop statement

#Python does not have a native do-while loop like some other languages, but you can simulate it using a while loop.

i = 1
while True:
    print(i)  # Print the value of i
    i=i+1  # Increment i
    if i > 10:
        break  # Exit the loop when i exceeds 10

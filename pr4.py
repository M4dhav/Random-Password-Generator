print("Test for Even/Odd: \n\n")
a = int(input("Enter a number: \n"))
if a%4 == 0:
    print("This number is a multiple of 4")
elif a%2 != 0:
    print("This number is odd")

else:
    print("This number is even")
print("Test for Divisibility: \n\n")
a = int(input("Enter the number to check for divisibility: \n"))
b = int(input("Enter the number to check for divisible by: \n"))
if a%b == 0:
    print("The given numbers are divisible")
else:
    print("The given numbers are not divisible")
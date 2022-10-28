a = int(input('Enter the number to check for divisors: \n'))
print("The divisors are: ")
for i in range(1, a+1):
    if a%i == 0:
        print(i)
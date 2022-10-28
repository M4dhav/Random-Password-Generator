a = int(input('Enter a number to check for prime: \n'))
prime = False
if a == 1:
    print("This is neither prime nor composite")
else:
    for i in range(2, a):
        if a%i == 0:
            prime = False
            break
        else:
            prime = True
if prime == True:
    print("This number is a prime")
else:
    print("This number is not a prime")

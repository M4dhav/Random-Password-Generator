num = int(input("Enter the number you want to sort the list by: \n"))
a = [1,1,2,3,5,8,13,21,34,55,89]
b = []
for i in a:
    if i <= num:
        b.append(i)
b = set(b)
print(b)
import random
a = int(input('How many elements do you want to generate?\n'))
l1 = []
l2 = []
for i in range(0, a):    
    l1.append(random.randint(0, 100))
    l2.append(random.randint(0, 200))
l1, l2 = set(l1), set(l2)
print("Your lists are: ")
print("list 1 ===>", l1)
print("list 2 ===>", l2)
l3 = l1.intersection(l2)
print("Their intersection is:")
if len(l3) == 0:
    print(None)
else:
    print(l3)

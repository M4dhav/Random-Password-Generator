n = int(input("How many elements do you want the list to have?\n"))
l = []
for i in range(n):
    l.append(input("Enter your element: "))
def duplicheck(list):
    l1 = []
    for i in list:
        if i not in l1:
            l1.append(i)
    return l1
def dupliset(list):
    list = set(list)
    return list
while True:
    method = input("What method would you like to use to eliminate Duplicates? (Loop/Set):\n").lower()
    if method == "loop":
        print(duplicheck(l))
        break
    elif method == "set":
        print(dupliset(l))
        break
    else:
        print("Please enter a valid argument.")

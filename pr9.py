num = int(input("How big do you want the list to be?\n"))
l1 = []
for i in range(0,num):
    n1 = int(input("Enter a number: \n"))
    l1.append(n1)
def l_ends(list):
    x = list[0]
    y = list[-1]
    return x, y
print(l_ends(l1))
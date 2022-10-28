a = input("Enter a word: \n")
palin = False
l1 = a[::]
l2 = a[::-1]
if l1 == l2:
    palin = True
# for i in a[::]:
#     for j in a[::-1]:
#         print(i, j)
#         if i == j:
#             palin = True
#         else:
#             palin = False
#             break
#     if palin == False:
#         break
if palin == True:
    print("This word is a Palindrome")
else:
    print("This word is not a palindrome")
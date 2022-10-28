def reverser(string):
    r = string.split()
    for i in r[::-1]:
        print(i, end = " ")
sent = input("Enter the sentence to be reversed:\n")
reverser(sent)
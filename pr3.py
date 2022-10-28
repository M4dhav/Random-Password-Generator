name = input("Enter your name: \n").capitalize()
age = int(input("Enter your age: \n"))
num = int(input("How many copies of the message do you want to print?\n"))
diff = 100 - age
print("Hey {}, You will turn 100 in the year {}\n".format(name, 2022+ diff)*num)
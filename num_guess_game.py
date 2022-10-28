import random
num = random.randint(0, 100)
guesses = 0
while True:
    user = (input("Enter your Guess: \n"))
    guesses += 1
    if int(user) > num:
        print("Enter a Lower Number!")
    elif int(user) < num:
        print("Enter a Higher Number!")
    elif user == "exit":
        print("Sorry to see you go! You took {} Tries".format(guesses))
        print("The correct number was {}".format(num))
        break
    else:
        print("Congratulations! You have guessed the number.")
        print("You took {} tries".format(guesses))
        break
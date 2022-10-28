import random
import functools
def gen(l, c):
    passw = []
    if c == "":
        char = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#&()–[{]}:;$‘,?/*"
    elif c == "A":
        char = "ABCDEFGHIJKLMNOPQRSTUVWXYZqwertyuiopasdfghjklzxcvbnm"
    elif c == "A1":
        char = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    for i in range(0, l):
        passw.append(random.choice(char))
    return passw
length = int(input("How long do you want the password to be?\n"))
chars = input("What characters do you want the Password to include?(A --> Alphabets, A1 --> Alphanumeric Characters, leave blank for all characters:\n")
password = gen(length, chars)
print(functools.reduce(lambda x, y: x+y, password))

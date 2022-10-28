import functools
num = int(input("How many numbers do you want to generate? \n"))
def fibo(x):
    fib = 1
    out = []
    if x == 1:
        out.append(1)
    elif x>1:
        for i in range(1, x+1):
            out.append(fibo(x-1))
    print(out)
fibo(num)

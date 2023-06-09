def fib(n):
    if n<3:
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(1,30,1):
    print(fib(i))
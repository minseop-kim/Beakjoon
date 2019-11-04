def fib(n, list):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return list[n-1] + list[n-2]

from sys import stdin

n = int(stdin.readline())

fibo = [0]*(n+1)

for i in range(n+1):
    fibo[i] = fib(i, fibo)

if n == 0:
    print('0')
else:
    print(fibo[-1])
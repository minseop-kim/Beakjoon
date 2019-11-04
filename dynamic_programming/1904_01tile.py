from sys import stdin

n = int(stdin.readline())

fib = [1, 1]

for i in range(2, n):
     fib[i%2]= (fib[0] + fib[1]) % 15746

if n<3:
    print('1')
else:
    print((fib[0] + fib[1]) % 15746)
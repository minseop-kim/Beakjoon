from sys import stdin

n = int(stdin.readline())
number =[0 for _ in range(10001)]

for _ in range(n):
    tn = int(stdin.readline())
    number[tn] += 1

for i, num in enumerate(number):
    if num !=0:
        for _ in range(num):
            print(i)

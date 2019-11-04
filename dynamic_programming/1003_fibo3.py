def fib(n, list):
    if n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1
    else:
        return list[n-1][0] + list[n-2][0], list[n-1][1] + list[n-2][1]

from sys import stdin

n = int(stdin.readline())

value = []
for _ in range(n):
    tn = int(stdin.readline())
    value.append(tn)

for n in value:
    if n == 0:
        print('1 0')
    elif n == 1:
        print('0 1')
    else:

        count = []
        count.append([1, 0])
        count.append([0, 1])

        for i in range(2, n+1):
            count.append(list(fib(i, count)))

        print(count[-1][0], count[-1][1])
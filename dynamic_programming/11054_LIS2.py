import sys

number = int(sys.stdin.readline())

suyol = list(map(int, sys.stdin.readline()[:-1].split(' ')))

inc = [1 for _ in range(number)]
dec = [1 for _ in range(number)]
res = [0 for _ in range(number)]

for i in range(number):
    for j in range(i):
        if suyol[i] > suyol[j] and inc[i] < inc[j]+1:
            inc[i] += 1

for i in range(number-1, -1, -1):
    for j in range(number-1, i-1, -1):
        if suyol[i] > suyol[j] and dec[i] < dec[j]+1:
            dec[i] += 1
    res[i] = inc[i] + dec[i]

print(max(res)-1)
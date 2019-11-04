import sys

n, k = map(int, sys.stdin.readline().split(' '))

dongjun = []
for _ in range(n):
    v = int(sys.stdin.readline())
    dongjun.append(v)

geasu = 0
for i in range(len(dongjun)-1, -1, -1):
    if dongjun[i] <= k:
        mok =  k // dongjun[i]
        k -= (dongjun[i]*mok)
        geasu += mok

print(geasu)


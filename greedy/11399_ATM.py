import sys

n = int(sys.stdin.readline())
time = list(map(int, sys.stdin.readline().split(' ')))

time = sorted(time)
incul = 0
deagi = 0

for v in time:
    incul += deagi + v
    deagi += v


print (incul)
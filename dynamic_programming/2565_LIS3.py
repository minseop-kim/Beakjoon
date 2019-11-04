import sys

number = int(sys.stdin.readline())

line = [0 for _ in range(501)]

for _ in range(number):
    jul = list(map(int, sys.stdin.readline()[:-1].split(' ')))
    line[jul[0]] = jul[1]

junbotdea = []
for v in line:
    if v != 0:
        junbotdea.append(v)

length = len(junbotdea)
inc = [1 for _ in range(length)]
for i in range(length):
    for j in range(i):
        if junbotdea[i] > junbotdea[j] and inc[i] < inc[j]+1:
            inc[i] += 1

print(length - max(inc))
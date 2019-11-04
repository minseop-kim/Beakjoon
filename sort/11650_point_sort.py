from sys import stdin

n = int(stdin.readline())

point = []

for _ in range(n):
    tx, ty = map(int, stdin.readline()[:-1].split(' '))
    point.append([tx, ty])

point = sorted(point, key= lambda x : (x[0],x[1]))

for x, y in point:
    print(x, y)
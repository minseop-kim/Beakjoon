from sys import stdin

n = int(stdin.readline())

member = []

for _ in range(n):
    age, name = stdin.readline()[:-1].split(' ')
    age = int(age)
    member.append([age, name])

member = sorted(member, key= lambda  x:x[0])

for age, name in member:
    print(age, name)
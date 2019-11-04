from sys import stdin

number = int(stdin.readline())

su = [1] * 10
su[0] = 0

for i in range(1, number):
    sub_su = []
    for j in range(10):
        if j == 0:
            sub_su.append(su[j+1])
        elif j == 9:
            sub_su.append(su[j-1])
        else:
            sub_su.append(su[j+1]+su[j-1] % 1000000000)
    su = sub_su

print(sum(su) %1000000000)
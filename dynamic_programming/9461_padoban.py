from sys import stdin

tc = int(stdin.readline())
n = []
maxi = 0
for _ in range(tc):
    tn = int(stdin.readline())
    if tn >maxi:
        maxi = tn
    n.append(tn)

padoban = [1, 1, 1, 2, 2]

for i in range(5, maxi):
    padoban.append( padoban[-1] + padoban[-5])

for v in n:
    print(padoban[v-1])
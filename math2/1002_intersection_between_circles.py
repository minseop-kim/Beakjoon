banbock = int(input())

x1 =[]
y1 =[]
r1 =[]
x2 =[]
y2 =[]
r2 =[]

for _ in range(banbock):
    tx, ty, tr, tx2, ty2, tr2 = map(int, input().split(' '))
    x1.append(tx)
    y1.append(ty)
    r1.append(tr)
    x2.append(tx2)
    y2.append(ty2)
    r2.append(tr2)

for i in range(banbock):
    if x1[i] == x2[i] and y1[i] == y2[i] and r1[i] == r2[i]:
        print('-1')
        continue

    if r1[i] < r2[i]:
        lr = r2[i]
        sr = r1[i]
    else:
        lr = r1[i]
        sr = r2[i]

    geori = ((x1[i] - x2[i])**2 + (y1[i] - y2[i])**2)**(1/2)
    sum_answer = r1[i] + r2[i]

    if geori == sum_answer or  geori == lr-sr:
        print('1')
    elif geori < lr-sr or geori > sum_answer:
        print('0')
    else:
        print('2')
x = []

while True:
    tx, ty, tz = map(int, input().split(' '))
    if tx == 0 and ty == 0 and tz == 0:
        break
    x.append([tx, ty, tz])

for i in range(len(x)):
    maxi = 0
    max_idex = 0

    for index, v in enumerate(x[i]):
        if v > maxi:
            max_idex = index
            maxi = v

    x[i].pop(max_idex)
    x[i].append(maxi)

    if x[i][0] + x[i][1] > x[i][2] and x[i][0] ** 2 + x[i][1] ** 2 == x[i][2] ** 2:
        print('right')
    else:
        print('wrong')
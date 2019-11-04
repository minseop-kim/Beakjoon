x =[]
y =[]
for i in range(3):
    tx, ty = map(int, input().split(' '))
    x.append(tx)
    y.append(ty)

for i in range(len(x)):
    if x.count(x[i]) == 2 and y.count(y[i]) == 2:
        bx = x.pop(i)
        by = y.pop(i)
        break

for i in range(len(x)):
    if bx != x[i] and by == y[i]:
        incx = x[i] - bx
    if bx == x[i] and by != y[i]:
        incy = y[i] - by


print(bx + incx, by + incy)
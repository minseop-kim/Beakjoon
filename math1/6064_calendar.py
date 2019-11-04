tc = int(input())
m, n, x, y = [], [], [], []
for i in range(tc):
    tm, tn, tx, ty = map(int, input().split(' '))
    m.append(tm)
    n.append(tn)
    x.append(tx)
    y.append(ty)


def gcd(a, b):
    while b != 0:
        r = a % b
        a, b = b, r
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


for i in range(tc):
    maxi = lcm(m[i], n[i])

    while x[i] <= maxi:
        if (x[i] - y[i]) % n[i] == 0:
            break
        x[i] += m[i]

    if x[i] > maxi:
        x[i] = -1

    print(x[i])
m, n = map(int, input().split(' '))

sosu = [0 for i in range(n+1)]

for i in range(2, n+1):
    if sosu[i] == 0:
        sosu[i] = 1
    else:
        continue

    for j in range(2, n):
        if i*j > n:
            break
        else:
            sosu[i*j] = 2

for i in range(m, n+1):
    if sosu[i] == 1:
        print(i)
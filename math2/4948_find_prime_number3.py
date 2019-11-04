n = []
while True:
    su  = int(input())
    if su == 0:
        break
    n.append(su)

big_one = max(n)

sosu = [0 for i in range(2*big_one+1)]

for i in range(2, 2*big_one+1):
    if sosu[i] == 0:
        sosu[i] = 1
    else:
        continue

    for j in range(2, 2*big_one+1):
        if i*j > 2*big_one:
            break
        else:
            sosu[i*j] = 2

for i in range(len(n)):
    count = 0
    for j in range(n[i]+1, 2*n[i]+1):
        if sosu[j] == 1:
            count += 1
    print(count)
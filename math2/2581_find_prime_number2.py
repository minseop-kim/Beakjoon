m = int(input())
n = int(input())

sosu = [0 for i in range(n-m+1)]

def check_sosu(n):
    if n == 1:
        return 0
    else:
        for i in range(2, n):
            if n % i == 0:
                return 0
        return 1

for i in range(len(sosu)):
    sosu[i] = check_sosu(i+m)

if 1 not in sosu:
    print('-1')
else:
    sum = 0
    for i in range(len(sosu)):
        if sosu[i] == 1:
            sum += (i+m)
    print(sum)
    print(sosu.index(1)+m,end='')
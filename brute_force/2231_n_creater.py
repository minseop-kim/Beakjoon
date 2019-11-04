n = int(input())

hap=0
for i in range(1, n):
    hap = i + sum(map(int,list(str(i))))
    if hap == n:
        break

if hap != n:
    print('0')
else:
    print(i)
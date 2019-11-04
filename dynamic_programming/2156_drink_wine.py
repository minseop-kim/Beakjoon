from sys import stdin

number = int(stdin.readline())
podoju = []

for _ in range(number):
    podoju.append(int(stdin.readline()))

dp=[]

if number == 1:
    dp.append(podoju[0])
elif number == 2:
    dp.append(podoju[0] + podoju[1])
elif number == 3 :
    tmp = podoju[0]+ podoju[1] + podoju[2]
    dp.append(max(tmp - podoju[0],tmp - podoju[1],tmp - podoju[2]))
else:
    dp.append(podoju[0])
    dp.append(podoju[0] + podoju[1])
    tmp = podoju[0]+ podoju[1] + podoju[2]
    dp.append(max(tmp - podoju[0], tmp - podoju[1], tmp - podoju[2]))
    for i in range(3,number):
        dp.append(max(dp[-2] + podoju[i], dp[-3] + podoju[i-1] + podoju[i], dp[-1]))
print(dp[-1])
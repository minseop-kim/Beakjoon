number = int(input())
last = []

def geacha(n):
    if n == 1:
        return 1
    else:
        return n + last[n-2]

i = 1
while True:
    last.append(geacha(i))
    if number <= last[-1]:
        break
    i += 1

if number > 1:
    start = last[i-2]+1
    if i % 2 == 0:
        boonja = 1 + number - start
        boonmo = i - number + start
    else:
        boonja = i - number + start
        boonmo = 1 + number - start
else:
    boonja = 1
    boonmo = 1

print(str(boonja)+'/'+str(boonmo),end='')
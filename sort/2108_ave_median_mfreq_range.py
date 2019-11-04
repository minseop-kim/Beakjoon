from sys import stdin

n = int(stdin.readline())

num =[0 for _ in range(8001)]

maxi = -4001
mini = 4001
sum_tn = 0
max_bindo =0
hana = True
for i in range(n):
    tn = int(stdin.readline())
    sum_tn += tn
    if tn < mini:
        mini = tn
    if tn > maxi:
        maxi = tn
    num[tn+4000] += 1
    if max_bindo < num[tn+4000]:
        max_bindo = num[tn+4000]
        max_index = tn+4000
        hana = True
    elif max_bindo == num[tn+4000] and hana:
        max_index = tn+4000
        hana = False

arithmatic_average = round(sum_tn / n)

sort_num = []
for i, v in enumerate(num):
    if v != 0:
        for _ in range(v):
            sort_num.append(i-4000)
    if len(sort_num) == n:
        break
median_value = sort_num[n>>1]

if hana:
    cheobin_value = max_index - 4000
else:
    c=0
    for i in range(8001):
        if num[i] == max_bindo:
            if c == 1:
                cheobin_value = i - 4000
                break
            c+=1

bomui = maxi - mini

print(arithmatic_average, median_value, cheobin_value, bomui, sep='\n', end='')
n = int(input())
number = []
for _ in range(n):
    number.append(int(input()))

maxi_sosu = max(number)

sosu = [0 for i in range(maxi_sosu+1)]
inc = 1
ah =(maxi_sosu>>1)+1
for i in range(2, maxi_sosu+1, inc):
    if i == 3:
        inc +=1
    if sosu[i] == 0:
        sosu[i] = 1
    else:
        continue

    for j in range(2, ah):
        if i*j > maxi_sosu:
            break
        else:
            sosu[i*j] = 2

for n in number:
    h_n = n>>1
    for i in range(h_n, -1, -1):
        if sosu[i]== 1 and sosu[n-i] == 1:
            break

    print(i, n-i)
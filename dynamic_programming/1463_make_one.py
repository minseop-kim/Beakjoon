from sys import stdin

number = int(stdin.readline())

dp = [0, 1, 1]

for i in range(4,number+1):
    if i % 2 == 0 and i % 3==0:
        count = min(1+dp[i//2-1], 1+dp[i//3-1])
    elif i % 2 == 0 and i % 3 !=0:
        count = min(1+dp[i//2-1], 1+dp[i-2])
    elif i % 2 != 0 and i % 3 ==0:
        count = min(1+dp[i//3-1], 1+dp[i-2])
    else:
        count = (1 +dp[i-2])
    dp.append(count)

if number <4:
    print(dp[number-1])
else:
    print(dp[-1])
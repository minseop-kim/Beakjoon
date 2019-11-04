from sys import stdin

number = int(stdin.readline())

suyol = list(map(int, stdin.readline()[:-1].split(' ')))

dp = []
dp.append(suyol[0])
for i in range(1, len(suyol)):
    if suyol[i] > dp[-1]:
        dp.append(suyol[i])
    else:
        start = 0
        end = len(dp)
        while start < end:
            mid = (start + end ) //2
            if suyol[i] <  dp[mid]:
                end = mid
            elif suyol[i] ==  dp[mid]:
                start = mid
                end = mid
            else:
                start = mid+1
        dp[start] = suyol[i]

print(len(dp))
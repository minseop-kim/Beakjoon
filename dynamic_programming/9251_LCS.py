import sys

txt = []

txt.append(sys.stdin.readline()[:-1])
txt.append(sys.stdin.readline()[:-1])

dp = [0 for _ in range(len(txt[0])+1)]
for i in range(len(txt[1])):
    count = [0 for _ in range(len(txt[0])+1)]
    for j in range(len(txt[0])):
        if txt[1][i] == txt[0][j]:
            count[j+1] = dp[j] +1
        else:
            count[j+1] = count[j] if count[j] > dp[j+1] else  dp[j+1]
    dp = count

print(dp[-1])
import sys

n, mw = map(int, sys.stdin.readline().split(' '))
w = []
v = []

for _ in range(n):
    tw, tv = map(int, sys.stdin.readline().split(' '))
    w.append(tw)
    v.append(tv)

dp = [[0 for _ in range(mw+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, mw+1):
        if w[i-1] > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v[i-1] + dp[i-1][j-w[i-1]], dp[i-1][j])

print(dp[n][mw])
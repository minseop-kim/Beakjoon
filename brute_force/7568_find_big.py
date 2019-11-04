n = int(input())
weight = []
height = []
for _ in range(n):
    tw, th = map(int, input().split(' '))
    weight.append(tw)
    height.append(th)

rank = [0] * n

for i in range(0, n):
    n_rank = 1
    for j in range(0, n):
        if (weight[j] > weight[i] and height[j] > height[i]):
            n_rank += 1
    rank[i] = n_rank

for rk in rank:
    print(rk, end=' ')
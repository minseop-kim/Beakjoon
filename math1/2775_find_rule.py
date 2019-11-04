tc = int(input())
# 0층 부터, 1 k 14
# 1호 부터, 1 n 14
# 0층의 i호에는 i명이 산다.
k, n = [], []
for i in range(tc):
    k.append(int(input()))
    n.append(int(input()))

for case in range(tc):
    floor = [i+1 for i in range(n[case])]
    for i in range(k[case]):
        for j in range(len(floor)):
            floor[len(floor)-j-1] = sum(floor[0:len(floor)-j])
            if i == k[case]-1:
                break
    print(floor[-1])
    floor.clear()
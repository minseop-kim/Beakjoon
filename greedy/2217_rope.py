# 백준 2217번 문제 로프
# 로프를 선택하지 않았을 경우를 고려하지 않아 1번 틀림
# 입출력에 관한건 사이트 참고

import sys

n = int(sys.stdin.readline())
rope = []
for _ in range(n):
    t = int(sys.stdin.readline())
    rope.append(t)

rope = sorted(rope)

maximum_weight = 0

for i, v in enumerate(rope):
    maximum_weight = max(v*(len(rope)-i), v, maximum_weight)

print(maximum_weight)
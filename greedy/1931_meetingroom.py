# 백준 1931번 문제 회의실배정
# 오타로인한 런타임에러 2번
# 시작하자 끝나는 회의도 한사람이 진행하고 있으면 다른 사람은 할 수 없다고 생각해서 조건을 넣었으나
# 시작하자 마자 끝나는게 동시간대에 가능해서 틀림

import sys

#n =1
n = int(sys.stdin.readline())
meeting = []
#meeting = [[2, 2],
#           [2, 2]]
#meeting = [[1, 4],
#           [0, 4],
#           [2, 4],
#           [4, 4],
#           [4, 4],
#           [4, 4],
#           [4, 4],
#           [3, 5],
#           [0, 6],
#           [5, 7],
#           [3, 8],
#           [5, 9],
#           [6, 10],
#           [8, 11],
#           [8, 12],
#           [2, 13],
#           [12, 14]]

for _ in range(n):
    term = list(map(int, sys.stdin.readline().split()))
    meeting.append(term)

meeting = sorted(meeting, key=lambda x:(x[1], x[0]))

pre_end = 0
count =0

for start, end in meeting:
    if pre_end <= start:
        count += 1
        pre_end = end

print(count)
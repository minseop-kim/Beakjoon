from sys import stdin

total_stair = int(stdin.readline())
number = []
for _ in range(total_stair):
    number.append(int(stdin.readline()))

answer = []
if total_stair == 1:
    answer.append(number[0])
elif total_stair == 2:
    answer.append(answer[0]+number[1])
elif total_stair == 3:
    answer.append(max(number[0], number[1]) + number[2])
else:
    answer.append(number[0])
    answer.append(answer[0]+number[1])
    answer.append(max(number[0], number[1]) + number[2])
    for i in range(3, total_stair):
        answer.append(max(answer[-2], answer[-3] + number[i-1])+number[i])

print(answer[-1])
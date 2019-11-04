from sys import stdin

tline = int(stdin.readline())
number = []
for _ in range(tline):
    number.append(list(map(int, stdin.readline()[:-1].split(' '))))

answer = []
answer.append(number[0][0])

for i in range(1, tline):
    sub_an = []
    for j in range(i+1):
        if j == 0:
            sub_an.append(answer[j]+number[i][j])
        elif j == i:
            sub_an.append(answer[j-1]+number[i][j])
        else:
            sub_an.append(max(answer[j-1], answer[j]) + number[i][j])
    answer = sub_an
print(max(answer))

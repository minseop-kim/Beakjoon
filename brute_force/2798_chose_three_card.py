n, m = map(int, input().split(' '))
txt = input().split(' ')
c = []
for i in range(n):
    c.append(int(txt[i]))
answer = []

for i in range(len(c)-2):
    for j in range(i+1, len(c)-1):
        for k in range(j+1, len(c)):
            o = c[i] + c[j] + c[k]
            if c[i] + c[j] + c[k] <= m:
                answer.append(o)

print(max(answer))
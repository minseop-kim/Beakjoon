text = input()
d = {}
n, c = 3, 0
for i in range(26):
    c += 1
    d[chr(65+i)] = n
    if c == 3:
        n, c = n+1, 0
d['S'], d['V'], d['Y'], d['Z'] = 8, 9, 10, 10

time = 0

for v in range(len(text)):
    time += d[text[v]]

print(time)
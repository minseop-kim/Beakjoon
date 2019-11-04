number = int(input())

last = []
def geacha(n):
    if n == 0:
        return 1
    else:
        return 6 * (n) + last[n - 1]

i = 0
while True:
    last.append(geacha(i))
    if number <= last[-1]:
        break
    i += 1

print(i+1)
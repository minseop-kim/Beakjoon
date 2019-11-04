banbock = int(input())
for i in range(banbock):
    text = input().split()
    for j in range(len(text[1])):
        for k in range(int(text[0])):
            print(text[1][j], end='')
    print()
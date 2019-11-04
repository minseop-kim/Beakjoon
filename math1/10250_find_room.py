banbock = int(input())
txt = []
for i in range(banbock):
    txt.append(input())

for case in txt:
    h, w, n = map(int, case.split(' '))

    namozi = n % h
    if namozi == 0:
        namozi = h
        mok = n // h
    else:
        mok = n // h + 1

    mok = str(mok).zfill(2)

    print(str(namozi)+mok)
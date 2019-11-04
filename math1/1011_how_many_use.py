banbock = int(input())
inn = []
for i in range(banbock):
    inn.append(input())

def hol_suyol(n, last):
    if n == 1:
        return 1
    else:
        return 2*n-1 + last[2*(n-2)]

def jjack_suyol(n, last):
    if n == 1:
        return 2
    else:
        return 2*n + last[2*(n-2)+1]

for case in inn:
    x, y = map(int, case.split(' '))
    diff = y-x
    last = []

    i=1
    while True:
        last.append(hol_suyol(i, last))
        if last[-1] >= diff:
            break
        last.append(jjack_suyol(i, last))
        if last[-1] >= diff:
            break
        i+=1

    print(len(last))

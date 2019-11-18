import sys

txt = sys.stdin.readline()[:-1]

minus_flag = False
yang = 0
um = 0
num = '0'

for i, v in enumerate(txt):
    if v == '+' or v == '-':
        if minus_flag:
            um += int(num)
        else:
            yang += int(num)

        if minus_flag==False and v == '-':
            minus_flag = True

        num = ''
    else:
        num += v
        if i == len(txt)-1:
            if minus_flag:
                um += int(num)
            else:
                yang += int(num)

print(yang-um)
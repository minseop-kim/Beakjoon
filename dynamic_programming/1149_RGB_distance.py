from sys import stdin

tc = int(stdin.readline())
rgb= []
for _ in range(tc):
    tr, tg, tb = map(int, stdin.readline(-1).split(' '))
    rgb.append([tr,tg,tb])

val = rgb[0]

for i in range(1, len(rgb)):
    val[0], val[1], val[2] = min(val[1], val[2]) + rgb[i][0],\
                            min(val[0], val[2]) + rgb[i][1],\
                            min(val[0], val[1]) + rgb[i][2]

print(min(val))
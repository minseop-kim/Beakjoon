text = str.upper(input())
a = 65

literature = []
out = []
for i in range(26):
    literature.append(text.count(chr(a+i)))

mcount = max(literature)
for i in range(26):
    if literature[i] == mcount:
        out.append(chr(a+i))

if len(out) > 1:
    print('?')
else:
    print(out[0])
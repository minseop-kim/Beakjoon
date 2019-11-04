banbock = int(input())
txt = []
for i in range(banbock):
    txt.append(input())

group_word = 0
for t in txt:
    pre_char = ''
    used_char = [0] * 26
    for i in range(len(t)):
        if pre_char != t[i]:
            used_char[ord(t[i])-ord('a')] += 1
        pre_char = t[i]

    if max(used_char) == 1:
        group_word += 1

print(group_word)

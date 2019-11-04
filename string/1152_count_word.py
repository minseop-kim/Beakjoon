text = str.strip(input())
li = text.split(' ')
pop_index = []
for i in range(len(li)-1,-1, -1):
    if li[i] == '':
        pop_index.append(i)

for i in pop_index:
    li.pop(i)

print(len(li))
text = input()
a = 97

for i in range(26):
    print(text.find(chr(a+i)), end=' ')
n = int(input())
count = 0
i = 665
while count != n:
    i+=1
    if str(i).count('666') > 0:
        count +=1
print(i)
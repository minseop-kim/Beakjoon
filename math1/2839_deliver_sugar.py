n_kg = int(input())

bongzi = [5, 3]
geasu = 0

i = 0
if n_kg % 5 == 0:
    geasu = n_kg // bongzi[0]
    n_kg -= geasu * bongzi[0]
else:
    while i*bongzi[0] < n_kg:
        if n_kg - (i*bongzi[0]) == 3:
            geasu += 1 + i
        if n_kg - (i * bongzi[0]) == 6:
            geasu += 2+ i
        if n_kg - (i * bongzi[0]) == 9:
            geasu += 3+ i
        if n_kg - (i * bongzi[0]) == 12:
            geasu += 4+ i
        if geasu != 0:
            n_kg =0
            break
        i+=1

if n_kg != 0:
    print('-1')
else:
    print(geasu)
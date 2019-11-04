total_case = int(input())
su = map(int, input().split(' '))

def check_sosu(n):
    if n == 1:
        return 0
    else:
        sosu = 1
        for i in range(2, n):
            if n % i == 0:
                return 0
        return sosu

geasu = 0;
for susja in su:
    geasu += check_sosu(susja)

print(geasu)
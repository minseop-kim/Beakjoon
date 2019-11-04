n = int(input())
number = []

for _ in range(n):
    number.append(int(input()))

# Python의 경우 Timsort 최악(n lg n), 최선(n)
number.sort()

for i in number:
    print(i)
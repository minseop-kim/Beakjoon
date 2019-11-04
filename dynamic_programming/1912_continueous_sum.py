import sys

number = int(sys.stdin.readline().strip())

number_list = list(map(int, sys.stdin.readline().strip().split(' ')))

dp = number_list[0]
sub_sum = number_list[0]

for i in range(1, len(number_list)):
    sub_sum += number_list[i]
    dp = max(dp, sub_sum, number_list[i])

    if sub_sum < 0:
        sub_sum = 0

print(dp)
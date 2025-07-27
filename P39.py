n = int(input())
coins = list(map(int, input().split()))

coins.sort(reverse=True)
my_sum = 0
total_sum = sum(coins)
count = 0

for coin in coins:
    my_sum += coin
    total_sum -= coin
    count += 1
    if my_sum > total_sum:
        break

print(count)

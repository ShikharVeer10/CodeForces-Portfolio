t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    odd = [x for x in a if x % 2 == 1]
    even = [x for x in a if x % 2 == 0]

    result = odd + even
    print(*result)


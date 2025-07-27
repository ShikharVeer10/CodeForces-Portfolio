t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    insertions = 0

    for i in range(n - 1):
        x = a[i]
        y = a[i + 1]
        small = min(x, y)
        big = max(x, y)

        while big > 2 * small:
            small *= 2
            insertions += 1

    print(insertions)

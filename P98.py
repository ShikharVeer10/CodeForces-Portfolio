t = int(input())
for _ in range(t):
    x, n, m = map(int, input().split())
    while n > 0 and x > 20:
        x = x // 2 + 10
        n -= 1
    x -= m * 10
    if x <= 0:
        print("YES")
    else:
        print("NO")

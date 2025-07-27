t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print(2)
    elif n % 3 == 0:
        print(n // 3)
    elif n % 3 == 1:
        print((n // 3 - 1) + 2)
    else:
        print((n // 3) + 1)

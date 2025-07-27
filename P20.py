def odd_divisor(n):
    return "NO" if n & (n-1) == 0 else "YES"

t=int(input())
for _ in range(t):
    n=int(input())
    print(odd_divisor(n))


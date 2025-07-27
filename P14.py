def max_gcd(n):
    return n//2

t=int(input())

for _ in range(t):
    n1, n2, n3 = map(int, input().split())
    print(max_gcd(n1), max_gcd(n2), max_gcd(n3))
t = int(input())
for _ in range(t):
    expr = input()
    a, b = expr.split('+')
    print(int(a) + int(b))
